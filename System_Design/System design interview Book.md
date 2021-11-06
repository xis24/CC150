# System design interview Book

NoSQL might be right choice if

- your app requires super low latency
- your data are unstructured or you do not have any relational data
- you only need to serialize and deserialize data
- you need to store a massive amount of data

## Vertical scaling vs Horizontal Scaling

Vertical scaling:
pro:

- simplicity
  con:
- has limitation cuz CPU and memory has limit
- doesn’t have failover and redundancy.

Horizontal scaling:
pro:

- large scal application
  con:
- not easy to manage

## loadbalancer:

- evenly distribute the traffic to server
  A private IP: an IP address that is only reachable within a network.
  For a security purpose, A private IP is used between servers. Load balancer communicates with web servers through private IPs.

## Database replication

- can be used in many database management systems, usually with master/slave relationship between original and copies
- master database supported write operations, and slaves get copies of the data from the master database and supports only read operations.
- Most of system are read heavy, and there usually more slaves that master

### Pro:

1. Better performance: writes happen in master, and read are distrbutes across slave nodes. IT allows more queries to be processed in parallel
2. Reliability: if one of server is failed, you don't need to worry because data is replicated across multiple locations
3. High avaialbility: By relicating data across difference locations, your website remained operation even if a database is offline as you can aces data stored another database server

- In case of only slave goes off online, and master node can temporarily take read operation. Once the issue is found out, new slave will replace the old one. In case of multiple slaves, we just route read operation to healthy slaves.
- If the master database goes offline, a slave database will be promoted to be the new master. All opertaions will be temporarily routed to the new master. New slave database will replace the old one for replcations. In production system, since the slaves database might not be up to date, we might need to run data recovery script.

## Cache

Cache tier
pros:

- better system performance
- ability to reduce database worklaods
- the ability to scale the cache tier independently

Considerations for using cache:

- Decide when to use cache. Using cache for data that is read frequently, but modified infrequently. Since cache is stored in volatile memory, it will be lost once server restart
- Expiration plicy: It's good practice to implement an expiration policy
- Consistency: This involves keeping the data store and the cache in sync. When scaling across multiple regions, maintaining consistency between the data store and cache is challenging.
- Mitigating failures: A single cache server presents a potential single point of failure. As a multiple cache servers across different data centers are recommended to avoid SPOF. Another recommended approach is to overprovision the required memory by certain percentage.
- Eviction policy: once cache is full, any request to additems to the cache migth cause existing items to be removed. LRU,. LFU, FIFO

## CDN

a network of geogrpahically dispered servers used to deliver static content.
Here is how CDN works at high-level: when a user visits a website, a CDN server cloest to the user will deliver static content. The CDN will improve the load speed.

### considerations of using a CDN

- Cost:
- Setting an appropriate cache expiry: For time-sensitive content, setting a cache expiry time is important.
- CDN fallback: If CDN fails, client should be able to get resources from the origin

## Stateless web tier

### Stateful architecture

a stateful server remembers client dat afrom on request to the next. Basically, this info sits together with server.
Cons:

- every request from the same client must be routed to the same server. This adds overhead
- adding and removing server is difficult
- can't handle server failure

### Stateless architecture

In this stateless architecture, HTTP requests from users can be sent to any web serves, which fetch state data from a shared data store. A stateless system is simpler, more robust and scalable.

## Data center

users are geoDNS-routed, geo-routed to the cloest data center, which allows domain name to be resolved to IP addresses based on the location of a user.

### Technical challenges

- Traffic redirection: GeoDNS service can be used
- Data synchronization: users from different regions could use different local databases or caches. In failover cases, traffic might be routed to a data center where data is unavailable
- Test and deployment: automated tools are vital

## Message queue

A message queue is a durable component, stored in memoery, that supports asynchronouse communication. It serves as a buffer and distributes asynchronous request. Input services, called producer/publishers, create message and public them into a message queue. Other services or servers, called consumers/subscribers, connect to the queue, and perform actions defined by the messages.

Decoupling makes teh message quee a preferred architecture for building a scalable and reliable applications. So when consumer is not avialable, producer can post message to the queue, and consumer can read from the queue even when producer is not available.

## Logging, metrics, automation

## Database scaling

### Vertical scaling

serious drawbacks:

- there are harware limits in CPU and RAM. If you have large user base, single server is not enough
- greater risk of single poit of failure
- cost of vertical is high. Powerful server are much more expensive

### Horizontal scaling

also known as sharding, is the practice of adding more servers. Sharding sperates large databse into smaller more easily managed parts called shards. Each shard shares the same schema

The most important factor to consider when implementing a sharding strategy is the choice of the sharding key. Sharding key (partition key)
consists of one or more columns that determin how data is distributed.

Cons:

- Resharding data: is needed when

1. a single shard can't no longer hold more data due to rapid growth
2. certain shars might experience shard exhaustion faster than others due to uneven data distribution. When shard exhaustion happens, it requires update the sharding function and move data around. Consitent hashing is used to solve this

- Celebrity problem: To solve this problem, we may need to allocate a shard for each celebrity. Each shard might even require further partition.

- Join and de-normalization: once database is sharded to multiple server, it is hard to perform join operation across from different shards. A common workaround is to de-normalize the dtabse.

## Back of the envelope estimation

A byte is a seuqnce of 8 bits. An ASCII character uses one byte of memory.

| power | approximate value | short name |
| ----- | ----------------- | ---------- |
| 10    | 1000              | 1KB        |
| 20    | 1000,000          | 1MB        |
| 30    | 1000000000        | 1GB        |
| 40    | 1 trillion        | 1TB        |
| 50    | 1 Quadrillion     | 1PB        |

- memory is fast but the disk is slow
- avoid disk seeks if possible
- simple compression algroithms are fast
- compress data before sending it over the internet if possible
- data centers are usually in different regions, and it takes time to send data beteween them

### Availability numbers

A service level aggreement (SLA) is a commonly used term for service providers. It defines the level of uptime your service will deliver

| availability | downtime per day |
| ------------ | ---------------- |
| 99%          | 14.4 minutes     |
| 99.9%        | 1.44 minutes     |
| 99.99%       | 8.64 seconds     |
| 99.999%      | 864 milliseconds |
