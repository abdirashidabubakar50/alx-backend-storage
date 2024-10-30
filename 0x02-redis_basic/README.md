## REDIS

#### What is Redis?

Redis is an open source in-memory data structure store whch can be used tas a database and/or cache  message broker.

Redis generally supports the following data types.
 - Strings
 -  Lists
 - Sets (Unordered collection of strings)
 - Sorted Sets (Non-repeating collection of strings)
 - Hashes (Basically key-value pairs, Perfect for representing objects)
 - Bitmaps
 - Hyperlogs
 - Geospatial Indexes

 #### Advantages of Redis
  - Very flexible - In terms of storing data, unlike structured relational databases no need to define schemas, columns etc.
  - Very Fast: can perform around 110,000 sets per second, about 81,000 GETs per second.
  - It has a Rich Datatype support
 
 ### Setting up Redis on Ubuntu:
  
  `sudo apt-get update`

  `sudo apt-get upgrade`

  `sudo apt-get -y install redis-server`

   `redis-cli`


### Basic commands

`ping` - test to see if there is a connection alive

`ECHO` - EX. `ECHO 'Hello world', it will echo 'Hello world' in the output.

`QUIT` - Close the connection

`SET foo 100` - Sets a key value pair here 100 to key foo

`GET foo` - get the value of foo set in the command above. output will be 100

`INCR foo` - will increment the value of foo.

`DECR foo` - will decrement the value of foo

`EXISTS foo` - checks if a key exists in this case foo. return 1 if exist else 0

`DEL foo` - Deletes a key-value pair, in this example foo will be deleted.

`FLUSHALL` - clear everything out entirely

we can also set values to expire at a certain point. ex
 - `EXPIRE foo 50` - expires foo in 50 seconds
 - `TTL foo`- will give the amount of time remains for foo to expire.
 