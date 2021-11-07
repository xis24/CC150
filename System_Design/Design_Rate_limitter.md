# Design Rate limitter

Example of usage:

- a user can write no more than 2 posts per second
- you can create a maximum of 10 accounts per day from the same IP address
- You can claim rewards no more than 5 times per week from the same device

Benefits of using an API rate limiter:

- prevent resource starvation caused by DOS attach
- Reduce cost: less server, less third party calls
- prevent server overloaded

## Functional requirement

- accurately limit excessive requests
- low latency.
- use as little memory as possible
- Distributed rate limiting. The rate limiter can be shared across multiple servers or processes
- Exception handling
- High fault tolerance. It shouldn't affect the entire system if rate limiter service has issues
