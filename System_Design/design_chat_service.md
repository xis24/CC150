# design chat service

sender <-> chat service <-> receiver

When sender sends a meesage to the receiver via the chat service, it uses time-based HTTP protocol. In this case, client opens a HTTP conneciton with chat service and sends the message, informing the service to send the message to the receiver. The keep-alive is efficent for this becasue keep-alive header allow a client to maintain a persisitent connection with chat service. It reduces the number of TCP handshakes. HTTP is fine option on the sender side.

Receiver side is bit complicated. Many techniques are used to simulate a server-initiated connection: polling, long polling, and websocket.

Polling
a technique that the clietn periodically asks the server if trhere are messages available. Depending on polling frequency, polling could be costly. connection is terminated after the message send out.

Long polling
a client holds the connection open until there are new messages avialable or a timeout threshold has been reached. Once the client receives new messages, it immediately sends another request to the server, restarting the process. Drawbacks:

- sender and receiver may not connect to the same chat server. HTTP based server are usually stateless. If you use round round for LB, the server receives the message might not have a long-polling connection with client who receives the message

- A server has no good way to tell if client is terminated
- It's insufficient. If a user doesn't chat much, long polling still makes periodic connections after timeouts.

WebSocket
WebSocket connection is initiated by the client. It's bi-directional and persistent. It starts its life as HTTP connection and could be upgraded via well-defined hadnshake to a WebSocket connection.
Websocket is bidirection. By using websockets for both sending and receiving, it simplifies the design and makes implementaiton on both clietn adn server more straightforward. Since websocket conenctions are persistent, efficient connection managment is critical on server side.

the chat system is broken down into three major categories:

- stateless services
- stateful services
- third-party integration

1. chat servers facilitate message sending/receiving
2. presence servers manage online/offline status
3. API servers handle everything inlcuding user login, signup, change profile etc
4. Notification servers send push notificaiton
5. Key value store is used to stoer chat history. When an offline user comes online, she will see all her previous chat history

## Storage

Two types of data exist in a typical chat system.

1. generic data, such as user profile, settings, user friends list. These data are storeed in robust and reliable relational database. Replicate and sharding are common techinques to satisfy availability and scalability requiremenets

2. The second is unique to chat system: chat history data.

- The amount of data is enormaouse for chat systems
- only recent chats are accessed frequently. User do not usually lookup chat history
- user might use features that require random access of data, such as search, view your mentions, jump to specific message.
- the read to write ratio is about 1:1 for one to one chat app

We recommend the key-value stores for the following reasons:

- key value allow easy horizontal scaling
- provide very low latency to acess data
- relational database do not handle long tail of data well. When the indees grow large, random acess is expensive
- key-value stores are adopted by other proven reliable chat applcaiton. FB uses HBase, discord uses canssandra.

## Data Models

### message table for 1-1 chat

The primary key is message_id, which helps to decided message sequence

| Message      |           |
| ------------ | --------- |
| message_id   | bigint    |
| message_from | bigint    |
| message_to   | bigint    |
| content      | text      |
| created_at   | timestamp |

### Message table for group chat

the composite primary key is (channel_id, message_id)

| Group_Message |           |
| ------------- | --------- |
| channel_id    | bigint    |
| message_id    | bigint    |
| user_id       | bigint    |
| content       | text      |
| created_at    | timestamp |

### Message_Id

how to generate message_id ?
Requirements:

- ID must be unique
- ID should be sortable by time, meaning new rows have higher IDs that old ones

1. first come to mind is auto_increment in MySQL. However, NoSQL usually do not provide such a feature
2. use a global 64-bit sequence number generator like Snowflake.
3. The final approach is to use loca sequence number generator. local means ID are unique within a gourp. The reason why Local works is that maintaining message sequence within one-one channel or group channel is good enough. It's easier to implement

## Design deep dive

### service discovery

the primary role of service discoery is to recommend the best chat server for a client based on teh criterial like geogrpahical locaiton, server capacity etc. Apache Zookeeper is a popular open-source solution for service discovery. It registers all the available chat servers and picks the best chat server for a client based on the predfined criteria.

### Message flows

1. User A sends chat message to chat server 1
2. chat server 1 obtains a message ID from the ID generator
3. chat server 1 sneds the message to the message sync queue
4. the message is stored in key-value store
5. a. if user B is online, the message is forwarded to chat server 2 where User B is connected
   b. if user is offline, a push notificaiton is sent from push notification servers
6. chat server 2 forwards the message to user B. There is persistent Websocket connection between user B and chat Server2

### Message synchronization across multiple devices

When user logs in to the chat app with her phone, it establishes a WebSocket connection with Chat server1. Similarly, there is connection between the laptop and chat server1

each device maintains a variable called cuir_max_message_id, which kepps track of the latest message ID on the device. Message that satify the following are considered as new msg:

- the recipient ID is equal to the currently logged-in user ID
- Message ID in the key-value store is larger than cur_max_message_id

With distinct cur_max_message_id on each device, message synchronization is esy as each device can get new messages from the KV store

### small group chat flow

User A sends a message in a group chat

1. message is copied to each group member's message sync queue (which acts like a inbox), this is good because:

- it simplifies message sync flow as each client only needs to check its own inbox to get new messages
- when group is small, storing a copy is not too expensive.

On the receipient side, a recipient can receive mesage from multiple users. Each receipient has message sync queue which contains message from different senders.

### Online presence

Presence servers are responsible for managing online status and communicating with clients through websockets. There are a few folow that will trigger online status change.

#### user login

After a websocket connection is built between the client and the real-time service, user A's online status and last_active_at timestamp are saved in KV store

#### user logout

The online status chagned to offline in the KV store.

#### user diconnection

when user disconnects from the internet, the persistent conneciton between the client and server is lost. A naive way to handler user disconnection is to makr the user as offline and change the stauts to online when re-establishes. But it has major flaws:if the internet is not stable, update online statuson every disconnect/reconnect would make the indicator change too often, resulting poor experience.

We introduce a heartbeat mechanism to solve this problem. Periodically,oneline client sends a heartbeat event to presence servers. if presence servers receives a heartbeat within certain time, it considers as online.

#### Online status fanout

How do user A's friends know about the status changes?
Presence servers uses a publish-subscriber model in which each feidnd pair maintains a channel. When user A online stautsw chagnes, it publishes the event to channels.

This solution is ok for small group like 500. But for large group, it would be too expensive. To solve this issue for large group, we can fetch online status only when a user enters a group or mannually refreshes the frirend list
