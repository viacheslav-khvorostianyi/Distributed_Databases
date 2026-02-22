# Task 5 Cassandra workshop

### Items table schema design and CQL operations
```bash
onnected to MyCluster at 127.0.0.1:9042
[cqlsh 6.1.0 | Cassandra 4.1.10 | CQL spec 3.4.6 | Native protocol v5]
Use HELP for help.
# Keyspace creation and table setup
cqlsh> CREATE KEYSPACE IF NOT EXISTS shop
   ... WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
cqlsh> 
cqlsh> USE shop;
cqlsh:shop> drop table if exists items;
cqlsh:shop> CREATE TABLE items (
        ...     category TEXT,
        ...     price DECIMAL,
        ...     item_id UUID,
        ...     name TEXT,
        ...     producer TEXT,
        ...     description TEXT,
        ...     created_at TIMESTAMP,
        ...     attributes MAP<TEXT, TEXT>,
        ...     PRIMARY KEY (category, price, producer)
        ... ) WITH CLUSTERING ORDER BY (price ASC, producer ASC);
cqlsh:shop> 
cqlsh:shop> CREATE INDEX items_attributes_keys_idx ON items (KEYS(attributes));
cqlsh:shop> CREATE INDEX items_attributes_entries_idx ON items (ENTRIES(attributes));
cqlsh:shop> CREATE INDEX items_name_idx ON items (name);

# Table description and data manipulation
cqlsh:shop> describe table items;

CREATE TABLE shop.items (
    category text,
    price decimal,
    producer text,
    created_at timestamp,
    description text,
    item_id uuid,
    name text,
    attributes map<text, text>,
    PRIMARY KEY (category, price, producer)
) WITH CLUSTERING ORDER BY (price ASC, producer ASC)
    AND additional_write_policy = '99p'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND cdc = false
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '16', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND memtable = 'default'
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND extensions = {}
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99p';

CREATE INDEX items_attributes_entries_idx ON shop.items (entries(attributes));

CREATE INDEX items_attributes_keys_idx ON shop.items (keys(attributes));

# Basic select queries
cqlsh:shop> SELECT name,producer,price FROM items
        ... WHERE category = 'Electronics' AND name = 'iPhone 14 Pro';

 name          | producer | price
---------------+----------+----------
 iPhone 14 Pro |    Apple | 52000.00

(1 rows)
cqlsh:shop> SELECT name,producer,price from items WHERE category = 'Electronics'  AND price >= 10000 AND price <= 50000;

 name                  | producer | price
-----------------------+----------+----------
    Samsung Galaxy S23 |  Samsung | 38000.00
 Laptop HP Pavilion 15 |       HP | 45000.00

(2 rows)
cqlsh:shop> SELECT name,producer,price FROM items WHERE category = 'Electronics' AND producer='Apple' AND price = 89000.00;

 name           | producer | price
----------------+----------+----------
 MacBook Pro 14 |    Apple | 89000.00


# Select with map value condition
cqlsh:shop> SELECT name, producer, price 
        ... FROM items 
        ... WHERE category = 'Books' AND attributes CONTAINS KEY 'isbn';

 name                                  | producer       | price
---------------------------------------+----------------+---------
            Head First Design Patterns | O'Reilly Media |  720.00
                            Clean Code |  Prentice Hall |  850.00
              The Pragmatic Programmer | Addison-Wesley |  950.00
 Designing Data-Intensive Applications | O'Reilly Media | 1200.00
            Introduction to Algorithms |      MIT Press | 1800.00

(5 rows)

cqlsh:shop> select name,producer,price from items where category = 'Books' and attributes['author'] = 'Robert Martin';

 name       | producer      | price
------------+---------------+--------
 Clean Code | Prentice Hall | 850.00

# Update map value and verify
cqlsh:shop> UPDATE items
        ... SET attributes['pages'] = '500'
        ... WHERE category = 'Books' AND price = 850.00 AND producer = 'Prentice Hall';

cqlsh:shop> select name,producer,price, attributes['pages']  from items where category = 'Books' and attributes['author'] = 'Robert Martin';

 name       | producer      | price  | attributes['pages']
------------+---------------+--------+---------------------
 Clean Code | Prentice Hall | 850.00 |                 500

(1 rows)


cqlsh:shop> UPDATE items SET attributes = attributes + {'edition': '2nd', 'language': 'English'} WHERE category = 'Books' AND price = 850.00 AND producer = 'Prentice Hall';
cqlsh:shop> select name,producer,price, attributes  from items where category = 'Books' and attributes['author'] = 'Robert Martin';

 name       | producer      | price  | attributes
------------+---------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------
 Clean Code | Prentice Hall | 850.00 | {'author': 'Robert Martin', 'edition': '2nd', 'format': 'Paperback', 'isbn': '978-0132350884', 'language': 'English', 'pages': '500', 'year': '2008'}

cqlsh:shop> UPDATE items
        ... SET attributes = attributes - {'edition', 'language'}
        ... WHERE category = 'Books' AND price = 850.00 AND producer = 'Prentice Hall';
cqlsh:shop> select name,producer,price, attributes  from items where category = 'Books' and attributes['author'] = 'Robert Martin';

 name       | producer      | price  | attributes
------------+---------------+--------+--------------------------------------------------------------------------------------------------------------
 Clean Code | Prentice Hall | 850.00 | {'author': 'Robert Martin', 'format': 'Paperback', 'isbn': '978-0132350884', 'pages': '500', 'year': '2008'}

(1 rows)
cqlsh:shop> 
```
### Order table schema design and CQL operations
```bash
# Table creation and description
cqlsh:shop>  CREATE TABLE orders (
        ...     customer_name TEXT,
        ...     order_date TIMESTAMP,
        ...     order_id UUID,
        ...     item_ids LIST<UUID>,
        ...     total_amount DECIMAL,
        ...     status TEXT,
        ...     shipping_address TEXT,
        ...     PRIMARY KEY (customer_name, order_date, order_id)
        ... ) WITH CLUSTERING ORDER BY (order_date DESC, order_id ASC);
cqlsh:shop> describe table orders;

CREATE TABLE shop.orders (
    customer_name text,
    order_date timestamp,
    order_id uuid,
    shipping_address text,
    status text,
    total_amount decimal,
    item_ids list<uuid>,
    PRIMARY KEY (customer_name, order_date, order_id)
) WITH CLUSTERING ORDER BY (order_date DESC, order_id ASC)
    AND additional_write_policy = '99p'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND cdc = false
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '16', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND memtable = 'default'
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND extensions = {}
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99p';
cqlsh:shop> CREATE INDEX items_ids_idx ON orders (ITEMS(item_ids)); 

#Basics select queries
cqlsh:shop> select customer_name, order_date, order_id from orders where customer_name='John Doe';
 customer_name | order_date                      | order_id
---------------+---------------------------------+--------------------------------------
      John Doe | 2026-02-22 17:47:39.010000+0000 | 6cc2703c-f4b6-43c7-bad9-e2d3b765ae0b
      John Doe | 2026-02-22 17:45:44.298000+0000 | c6477658-f30f-4b03-b09d-b017e844a83a
      John Doe | 2026-02-22 17:40:19.054000+0000 | 478382e1-d278-46d9-b1e8-97eb72caa387
      
cqlsh:shop> select customer_name, order_date, order_id from orders where customer_name='John Doe' and item_ids CONTAINS 14658bb0-32ca-4f5a-a4e8-ba6b33ec5a93;

 customer_name | order_date                      | order_id
---------------+---------------------------------+--------------------------------------
      John Doe | 2026-02-22 17:48:57.769000+0000 | 9cddb47d-efee-4bf2-8345-9e6b0a33cdc9

cqlsh:shop> SELECT COUNT(*) as orders_count FROM orders WHERE customer_name = 'John Doe' AND order_date >= '2026-01-01' AND order_date <= '2026-12-31';

 orders_count
--------------
            4

cqlsh:shop> SELECT customer_name, SUM(total_amount) as total_spent
        ... FROM orders
        ... WHERE customer_name = 'John Doe';

 customer_name | total_spent
---------------+-------------
      John Doe |     7000.00

(1 rows)
cqlsh:shop> SELECT customer_name, SUM(total_amount) as total_spent FROM orders WHERE customer_name = 'Viacheslav Khvorostianyi';

 customer_name            | total_spent
--------------------------+-------------
 Viacheslav Khvorostianyi |      900.00
 
 
 cqlsh:shop> SELECT customer_name, MAX(total_amount) as max_order_amount
        ... FROM orders
        ... WHERE customer_name = 'John Doe';

 customer_name | max_order_amount
---------------+------------------
      John Doe |          1750.00
      
      
cqlsh:shop> SELECT customer_name, MAX(total_amount) as max_order_amount FROM orders WHERE customer_name = 'Viacheslav Khvorostianyi';

 customer_name            | max_order_amount
--------------------------+------------------
 Viacheslav Khvorostianyi |           900.00


# Update order status and verify

cqlsh:shop> UPDATE orders
        ... SET item_ids = item_ids + [41337a65-f169-44f2-a43d-09749426302a, 7805b494-97e1-44fb-820c-366f810537f9],
        ...     total_amount = 1500.00
        ... WHERE customer_name = 'John Doe'
        ... AND order_date = '2026-02-22 10:30:00'
        ... AND order_id = 9cddb47d-efee-4bf2-8345-9e6b0a33cdc9;

 customer_name | order_date                      | order_id                             | item_ids                                                                     | shipping_address | status | total_amount
---------------+---------------------------------+--------------------------------------+------------------------------------------------------------------------------+------------------+--------+--------------
      John Doe | 2026-02-22 10:30:00.000000+0000 | 9cddb47d-efee-4bf2-8345-9e6b0a33cdc9 | [41337a65-f169-44f2-a43d-09749426302a, 7805b494-97e1-44fb-820c-366f810537f9] |             null |   null |      1500.00

(1 rows)
cqlsh:shop> UPDATE orders
        ... SET status = 'Shipped'
        ... WHERE customer_name = 'John Doe'
        ... AND order_date = '2026-02-22 10:30:00'
        ... AND order_id = 9cddb47d-efee-4bf2-8345-9e6b0a33cdc9
        ... 
        ... ;
cqlsh:shop> select * from orders where customer_name='John Doe' and order_date='2026-02-22 10:30:00' and order_id = 9cddb47d-efee-4bf2-8345-9e6b0a33cdc9;

 customer_name | order_date                      | order_id                             | item_ids                                                                     | shipping_address | status  | total_amount
---------------+---------------------------------+--------------------------------------+------------------------------------------------------------------------------+------------------+---------+--------------
      John Doe | 2026-02-22 10:30:00.000000+0000 | 9cddb47d-efee-4bf2-8345-9e6b0a33cdc9 | [41337a65-f169-44f2-a43d-09749426302a, 7805b494-97e1-44fb-820c-366f810537f9] |             null | Shipped |      1500.00

cqlsh:shop> SELECT order_id, order_date, total_amount, 
        ...        WRITETIME(total_amount) as price_write_time
        ... FROM orders
        ... WHERE customer_name = 'John Doe';

 order_id                             | order_date                      | total_amount | price_write_time
--------------------------------------+---------------------------------+--------------+------------------
 9cddb47d-efee-4bf2-8345-9e6b0a33cdc9 | 2026-02-22 17:48:57.769000+0000 |      1750.00 | 1771782537758994
 6cc2703c-f4b6-43c7-bad9-e2d3b765ae0b | 2026-02-22 17:47:39.010000+0000 |      1750.00 | 1771782459006822
 c6477658-f30f-4b03-b09d-b017e844a83a | 2026-02-22 17:45:44.298000+0000 |      1750.00 | 1771782344296623
 478382e1-d278-46d9-b1e8-97eb72caa387 | 2026-02-22 17:40:19.054000+0000 |      1750.00 | 1771782019051886
 9cddb47d-efee-4bf2-8345-9e6b0a33cdc9 | 2026-02-22 10:30:00.000000+0000 |      1500.00 | 1771783643477816



cqlsh:shop> INSERT INTO orders (customer_name, order_date, order_id, item_ids, total_amount, status, shipping_address)
        ... VALUES ('Jane Smith', toTimestamp(now()), uuid(), 
        ...         [550e8400-e29b-41d4-a716-446655440000], 
        ...         500.00, 'pending', '123 Main St')
        ... USING TTL 2592000;
cqlsh:shop> SELECT order_id, order_date, TTL(total_amount) as remaining_ttl
        ... FROM orders
        ... WHERE customer_name = 'Jane Smith';

 order_id                             | order_date                      | remaining_ttl
--------------------------------------+---------------------------------+---------------
 d50a4d19-3875-4a3f-aba8-75d524a957d3 | 2026-02-22 18:12:54.392000+0000 |       2591988
```

### Part 2 performance testing
```bash
(.venv) vkhvorostianyi@vkhvorostianyi-Latitude-E6440:~/PycharmProjects/Distributed_Databases/task5$ python perf_test.py 
Running primary test configuration...

================================================================================
Cassandra Counter Performance Test
================================================================================
Configuration:
  - Clients:              10
  - Requests per client:  10,000
  - Total requests:       100,000
  - Counter name:         performance_test_10c_10k
================================================================================

Initial counter value: 0
Starting test at: 2026-02-22 20:28:14


================================================================================
Individual Client Results:
================================================================================

Client     Time (s)     Successful   Failed     Req/s       
------------------------------------------------------------------
1          43.45        10,000       0          230.15      
2          38.82        10,000       0          257.57      
3          42.75        10,000       0          233.93      
4          38.53        10,000       0          259.55      
5          44.84        10,000       0          223.03      
6          39.93        10,000       0          250.45      
7          38.03        10,000       0          262.97      
8          39.21        10,000       0          255.02      
9          44.84        10,000       0          223.02      
10         41.71        10,000       0          239.73      

================================================================================
Performance Summary:
================================================================================
Total requests:           100,000
Successful requests:      100,000
Failed requests:          0
Success rate:             100.00%

Counter Statistics:
Expected counter value:   100,000
Actual counter value:     100,000
Counter accuracy:         100.0000%
Missing increments:       0

Timing:
Total execution time:     48.41 seconds
Overall throughput:       2065.65 req/s
Average time per client:  48.41 seconds
Average latency:          0.48 ms/request
================================================================================
```

**Run Performance Test:**
```
pip install -r requirements.txt
```
```bash
python perf_test.py
```