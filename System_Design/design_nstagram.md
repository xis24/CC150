# Design Instagram

## Requirement

### Functional

- upload/download/view photos
- user can perform searches based on photo/video titles
- user can follow other users
- news feed consisting of top photos from all the people user follows

### Non-functional Requirements

1. service needs to be high available
2. acceptable latency of sytem is 200 ms for News feed generation
3. Consistency can take a hit (to trade of availablity) if user doesn't a photo for a while; it should be fine
4. The system should be high relaible; any uloaded photos or video should never be lost

Not in the scope: adding tags, search photos on tags, commenting on photos, tagging users to photos.

## Some design considerations

The system would be read-heavy, and the goal is to build system that can retrieve photos quickly.

1. user should be able to upload as many photos as they like. Therefore, efficient managemetn of storage should be a crucial factor
2. low latency is expected when viewing photos
3. data should be 100% relaible. Photo shouldn't be lost
