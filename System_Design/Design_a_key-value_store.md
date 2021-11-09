# Design a key-value store

## Functional requirement

- the size of a key-value pair is mall: less than 10 KB
- ability to store big data
- high availability: the system responds quickly, even during failures
- high scalability: the system can be sacled to support large data set
- automatic scaling : the additon/deletion of servers should be automatic based on traffic
- Tunable consistency
- low latency

## Distributed key-value store

also called distributed hash table, which distribute key-value pairs across many servers. When designing distributed syste, it's important to understand, CAP (consistency, availability, parition tolerence) theorem

### CAP Theorem

- consistency: consitency means all clients see the same data at the same time no matter which node they connect to
- availability: availability means any client which requests data gets a response enen if some of the nodes are down
- partition tolerence: a partition indicates a communication break between two nodes. Parititon tolerence means the system continues to operate despite network partitions

CAP theorem states that one of the three properties must be sacrificed to support 2 of the 3 properites.

Since in real world, network partition is unavoidable, so there is only CP and AP system, but NO CA system.

## System components

- Data partition
- Data replication
- Consistency
- Inconsistency resolution
- Handling failures
- System architecture diagram
- Write path
- Read path

## Data partition

there are two challenges when partitoning data

- distribute data across multiple servers evenly
- minimize data movement when nodes are added or removed

This when consistent hashing comes to play, and bring the following advantages

- automatic scaling: servers could be added and removed automaticlaly depending on the load
- heterogeneity: the number of virtual nodes for a server is proprotional to the server capacity. For example, servers wit higher capacity are assigned with more vitual nodes

## Data replication

to achieve high availability and reliability, data must be replicated asynchronously over N server. The N servers are chosen: after a key is mapped to a hash ring, walk clockwise from the that poistion and count **unique** server (since there might virtual servers)

Node in the same data center might fail at the same time, and we probably want to have replica in another data center which is connected by high speed network.

## Consistency

Since data is replicated at multiple nodes, it must be synchronized across replicas. Quorum consensus can guarantee consistency for both read and write opertiaons.

N = number of replicas
W = A write quorum of size W. For a write operation to be considered as successful, write operation must be acknowledged from W replicas
R = A read quorum of size R. similar as W, read operations must be acknowledged from R replicas

The configuraiton of W, R and N is a typical tradeoff between latency and consistency. If W = 1 or R =1, latency is low because a coordinator only needs to wait for a response. If we have higher number, we can have better consistency but higher latency.

Possible setups:

- If R = 1 and W = N, the system is optmized for fast read
- If R = N and W = 1, the system is optimized for fast write
- If W + R > N, strong consistency is guaranteed
- If W + R <= N, strong consistency is not guaranteed

### Consistency model

- Strong consistency: any read operation return a value corresponding to the result of the most updated write data item. A client never see outdated data
- Weak consistency: subsequent read operations may not see the most updated value
- Eventual consistency: this is one form of weak consistency. Given enough time, all updates are propagated, and all replicas are consistent

Strong consistency is usually achieved by blocking new read/write until every replica has aggreed on current write. This is not good for highly available system. Dynamo and Cassandra adopt eventual consistency.

### Inconsistency resolution: versioning

A vector clock is [sever, version] pair associated with a data item. IT can be used to check if one version preced, succeedss or in conlflict with others.

cons of vector clock:

- vector clocks add complexity to the client because it needs to implement conflict resolution logic
- [sever:version] pairs in the vector clock could grow rapidly. To fix this problem, we set a threshold for the length, and if it exceeds the limit, the oldest pairs are removed. This might not work in theory, but Amazon Dynamo DB has not found issue in PROD

### Failure dections

All-to-all multicasting is a straightforward solution. However, this is inefficient when many servers are in the system.

A better solution is to use decentralized failure dection, gossip protocol:

- each node maintains a node memerbship list, which contains member ID and heartbeat counters
- each node periodically increments its heartbeat counter
- each node periodically sends heartbeats to a set of random nodes, which in turn propagate to another set of nodes.
- once nodes reveives the heartbeats, membership list is updated
- If the heartbeat has not increased for a more than predefined periods, the memeber is considered offline

### Handling temporary failures

After failures have been detected through the gossip protocol, we need mechanism to ensure availability. We could use sloppy quorum to improve availability in stead of quorum consensus (which could block read/write)
System choose first W health servers for write and R server for read and ignore offlined

Hinted handoff: If server is offline, another server will process the request temporarily. And when down server is back up, changes will be pushed back to achieve data consistency.

### Handling permannet failures

ordered systems tend toward a higher rate of entropy over time; therefore, higher the entropy, the greater the disorder.

Anti-entropy involves comparing each peice of data on replicas and updating each replcia t othe newest verison. A Merkle tree/hash tree isued for inconsistency detection and minimizing the amount of data transfered.

To compare two Merkle trees, start by comparing the root hashes. If root hashes match, both servers have the same data. If root hashes disagree, then the left child hashes are compared followed by right child hashes. You can traverse the tree to find which buckets are not synchronized and syncrhonize those buckets only.

Using Merkle tree, the amount of data needed to be synchronized is proportional to the diff between replicas, and not the amount of data it contains.

### Handling data center outage

use multiple data center

## System architecture diagram

main features of the architecture

- clients communicate with key-value store through simple API: get(key) and put(key, value)
- A coordinator is a node that acts as a proxy between the client and the key-value store
- Nodes are distributed on a ring using consistent hashing
- The system is completely decentralized so adding and moving nodes can be automatic
- data is replicated at multiple nodes
- there is no single point of failure as every node has the same set of responsibilities.

## Write Path

1. write request is persisted on a commit log file
2. data is saved in the memory cache
3. When the memory cache is full or reaches a predefined threshhold, data is flushed to a SSTable (sorted string table which is a sorted list of <key, value> pairs)

## Read Path

1. System first checks if data is in memory.
2. If data is not in memory, the system checks the bloom filter
3. The bloom filter is used to figure out which SSTables might contain the key
4. SSTables return the result of the data set
5. The result of the data set is retuende to the clietn

| goal/problems               | technique                                             |
| --------------------------- | ----------------------------------------------------- |
| ability to store big data   | use consistent hasing to spread load across servers   |
| high availability reads     | data replication; multi-datacenter setup              |
| highly available writes     | versioning and conflict resolution with vector clocks |
| dataset partition           | consistent hashing                                    |
| increamental scalability    | consistent hashing                                    |
| Heterogeneity               | consistent hashing                                    |
| Tunable consistency         | quorum consensus                                      |
| handling temporary failures | sloppy quorum and hinted handoff                      |
| handling permanent failures | merkle tree                                           |
| handling data center outage | cross-datacenter replication                          |
