# Design web crawler

Characteristics of good web crawler

- Scalability: web crawler should use parallelizaiton
- Robustness: The web crawler should handle bad HTML, unresponsive servers, crashes
- Politeness: shouldn't make too many request to a website within short period of time
- Extensibility: system is flexible to add new requirement

**different component of a web crawler**

Seed Urls

- The general strategy is to divide the entire URL space into smaller ones. The first proposed apprach is based on locality as different countries may have different popular websites. Or choose by topics, like fashion, healthcare and sports etc.

URL Frontier

- The component that stores URLs to be downloaded is called URL Frontier. This is FIFO queue.

HTML Downloader

- downloads web pages from the internet

DNS Resolver

- URL must be translated into an IP address.

Content parser

- after a web page is downloaded, it must be parsed and validated because malformed web page could provoke problems and waste resources. Having content parser in crawl server will slow things down, and that's why it's a separate component

Content seens?

- since page could be duplicated, and we want to avoid them. We could compare them char by char, but it's too slow. The solution is to compare the hashvalue of these two pages.

Content storages

- most of content is stored on disk becauswe the data set is too big to fit in memory
- popular content is kept in memory to reduce latency

URL extractor

- extra links from HTML pages

URL filter

- excludes certain content types, file extentsions, error links and blacklisted URL

URL seen?

- data structure that keep track of URLs that are visited before or already in the Frontier. Bloom filter and hash table are common techniques to implement the URL seen? component

URL Storage

- store already visted URLs

DFS vs BFS

DFS is usually not a good option as the depth could be very deep.
BFS is used by web crawlers and is implemented by queue. Two problems could arise

- Most links for the same web page are linked back to the same host. The host will be flooded with requests. Thus impolite
- The standard BFS doesn't take the priority of a URL into consideration. not very page has the salve level of quality and importantce. We may want to prioritize based on page ranks

URL Frontier

is a data strucutre that stores URLs to be downloaded. The URL frontier is an important component to ensure politeness, URL prioritization and freshness.

- Front queue: manage prioritization
- back queue: maange politeness

- Politeness
  the general idea of enfocing politeness is to download one page at a time from the same host. A delay can add between two downloaded tasks. The politeness constraint is implemented by maintain a mapping from website hostnames to download threads. Each downloader thread has a separate FIFO queue and only downloads URLs obtained from that queue.

  ```
  queue router ------> mapping table

            b1| b2| b3|
            x| x| x|
            x| x| x|
            query selector

    worker      worker     worker
    thread1     thread2    thread3
  ```

  - queue router: ensures each queue (b1, b2,..., bn) only contains URLs from the same host
  - mapping table: it maps each host to a queue
  - FIFO queues b1, b2 to bn: each queue contains URLs from the same host
  - Queue selector: each worker thread is mapped to a FIFO queue, and it only downloads URLs from that queue. it manages queue selection logic
  - Worker thread downloads pages one by one from the same host. A delay can be added between two download tasks.

- Priority
  - prioritizer: takes URLs as input and computes the priorites
  - Queue f1 to fn: each queue has an assigned priority. queue with high priority are slected wit hhigher probability
  - queue selector: randomly choose a queue with a bias towards quues with higher priority

Storage for URL Frontier

since memory is expensive and the number of URLs are huge. Putting to memory is not durable or scalable. Keeping in the disk is undesirable either b/c it's slow, and it can be bottleneck for crawler.

we will take a hybrid mode. Maintains a buffer in memory to enqueu and dequeue, and periodically write to the disk

Performance Optimization

1. Distributed crawl
   crawl jobs are distributed into multiple servers, and each server runs multiple threads. The URL space is partitioned into smaller peices; each downloader is responsible for a subset of URLs.

2. Cache DNS Resolver
   It could take from 10ms to 200 ms. To avoid this, we need keep a DNS cache for speed optimization. Our DNS cache keeps the domain name to IP address mapping and is updated periodically by cron jobs

3. Locality
   Distribute crawl servers geographically. When crawl servers are close to website hosts, cralers experience faster download time.

4. Short timeout

If host doesn't response within a prefined time, the craler will stop the job and crawl other pages

Robustness

- consistent hashing: this helps to distribute loads among downloaders. A new downloader server can be added or removed using consistent hashing.
- save crawl states and data: to guard against failures, crawl states and data are written to a storage system. A distributed crawl can be restarted easily by loading saved states and data
- handle exceptions
- data validation
