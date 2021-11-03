# Best Storage Solutions

## Cache

key - value
Redis

## Image and Videos

blob storage

- Amazon S3 + along with storage, CDN which distributed to across

## Text searching

text serach engine
Elastic serach and Solr

- provided level of fuzzy search
- shouldn't be used for primary database

## Time series

influx DB
Open TSDB

## Data warehousing storage solution

Hadoop

## Database

- structure of data
- query pattern
- amount of scale that you need to handle

Yes, structural data

- yes
  - Need ACID: RDBMS: Mysql, Postgres

No structured data

- data Type, queries

  - Document DB: Mongo DB, Couchbase

- ever increasing data + finite queries (less variety)
  - columnar DB:
    - Cassandra: lighter to deploy, nit deletes are not handled very efficiently
    - HBase: built on top of Hadoop, setup takes time
