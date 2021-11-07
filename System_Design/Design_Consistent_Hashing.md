# Design Consistent Hashing

## Rehashing problem

We typically use hash(key) % N, wher N is the size of the server pool. This works fine when the size of server is pool is fixed, and data distribution is even. However, problem arises when a server is added or removed.

## Consistent Hashing

Special hashing when a hash table is resized and consistent hashing is used. Only k/n keys need to be remapped on average, where k is the number of keys, and n is the numebr opf slots.

### Hash space and hash ring

Assume SHA-1 is used as a hash function. SHA-1 hash space goes from 0 to 2^160 - 1. By connecting both ends, we get a hash ring.

### Server lookup

To determin which server a key is stoed on, we go clockwise from the key position on the ring until a server is found. Going clockwise, key0 is stoed on server 0, key1 is stored on server 1, key2 is stored on server 2 and key3 is stored on server 3

### Add a server or remove a server

only fraction of servers are afffect, say we are doing the clockwise finding, then we will always find the next available server on the ring

### Two issues in the basic approach

1. it's impossibile to keep the same size of partitions on the ring for all servers considering a server can be added or removed. A parititon is the hash space between adjacent server. It's possible that the size of the partitions on the ring assigned to eac hserver is very small or faily large.

2.It's possible to have non-uniform key distribution on the ring.

### Virtual nodes

Virtual node refers to the real node, and eac hserver is represented by multiple virtual nodes on the ring. With virtual nodes, each server is responsible for multiple partitions.
As the number of virtual node increases, the distribution of keys becomes more balanced.
