# Design an unique id generator

Functional requrement

- IDs must be unique
- IDs are numerical values only
- IDs fits into 64 bit
- IDs are ordered by date
- ability to generate over 10,000 unique IDs per second

## Muti-master replication

This appraoch uses the databases auto_increament feature. In stead of increasing the next ID by 1, we increasing it by K, where K is the number of database servers in use. This solves some scalbility issues becasue IDs can scale with number of database servers. But there are drawbacks

- hard to scale with multiple data centers
- IDs do not go up with time cross multiple servers
- it doesn't scale well when a server is added or removed

## UUID

UUID is a 128 bit number used to indentify information in computer systems. UUID has a very low probablilit yof getting collision. UUIDs can be generated indepdently without coordination between servers.

In this design, eac hweb server contains an ID generator, each is to generate ID independently

Pros:

- generating UUIS is simple. No coordination between servers is needed so there is no synchronization
- The system is easy to scale because each web serer is responsible for generating IDs thye consume.

Cons:

- IDs are 128 bit long, but our requirement is 64 bit
- IDs do not go up with time
- IDs could be non-numeric

## Ticket server

The idea is to use a centralized auto_increament feature in a single database serer (ticket serer)

Pros:

- numeric IDs
- easy to implement, and it works for small to medium-scale applications

cons:

- single poitn of failure. If this server goes down, all other services relied on it will face issues. To avoid this, we can set up multiple ticket servers. However, there will be synchronization issues.

## Twitter snowflake approach

Divide and conquer is our friend. We divide an ID into different sections. Each sections is explained:

- sign bit: 1 bit. it will always be 0. This is reserved for future uses. can be used to distinguish between signed and unsigned numbers
- Timestamp: 41 bits. Milliseconds since the epoch.
- Datacenter ID: 5 bits, which gives us 32 datacenters
- Machine ID: 5 bits, 32 machines per datacenter
- Sequence number: 12 bits. For every ID generated on that machine/process, the sequence number is increamented by 1. The number is reset to 0 every milliseconds

## Design deep dive

Datacenter ID and machine ID are chosen at the startup time, generally fixed once the system is up running. Any change of datacenter ID and machine ID need to be reviewed since it could lead to conflict. Timestamp and sequence numbers are generated when ID generator is running

### Timestamp

the most important 41 bits make up the timestamp sections. As timestamp grow with time, IDs are sortable by time. The max timestamp that can eb represneted in 41 bits is 2 ^ 41 - 1 = 69 years. After 69 years, we will need a new epoch time oradpt other techniques to migrate IDs

### Sequence Number

Sequence number is 12 bits, 2 ^ 12 = 4096 combinations. This field is 0 unless more than one ID is genreated in a millisecond on the same server.

## Other talking points

- Clock synchronization. In our design, we assume ID generation servers have the same clock. This might not be true when a server is running on multiple cores. The same challenge exists in multi-machine scenarios. Network time procotol is the most popular solution to this problem

- Seciton length tunning. Fewer sequence number but more timestamp bits are effective for low concurrency and long-term applciaitons

- High availability. Since an ID generator is a mission ciritical system, it must be highly available
