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
- heterogeneity: the number of virtual nodes for a server is proprotional to the server capacity. For example, servers wit hhigher capacity are assigned with more vitual nodes

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
