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
