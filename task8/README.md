# Task 8 - Replication in Cassandra

Protocol
--

## Cluster Setup

### 1. Start the 3-node Cassandra cluster
```bash
docker compose up -d
[+] up 15/16
 ✔ Image cassandra:5.0          Pulled                                                                                                                                                                               19.2ss
 ✔ Network task8_cassandra-net  Created                                                                                                                                                                              0.4ss
 ✔ Volume task8_cassandra3-data Created                                                                                                                                                                              0.0ss
 ✔ Volume task8_cassandra1-data Created                                                                                                                                                                              0.0ss
 ✔ Volume task8_cassandra2-data Created                                                                                                                                                                              0.0ss
 ✔ Container cassandra1         Healthy                                                                                                                                                                              96.4ss
 ⠦ Container cassandra2         Waiting                                                                                                                                                                              163.8s
 ✔ Container cassandra3         Created                                                                                                                                                                              0.1ss
```

### 2. Verify cluster health with `nodetool status`
```bash
docker compose exec cassandra1 nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load        Tokens  Owns (effective)  Host ID                               Rack 
UJ  172.19.0.4  30.9 KiB    16      ?                 7c191c80-5617-45f5-9fb1-9210bee8cf44  rack1
UN  172.19.0.2  119.83 KiB  16      100.0%            eea6c0bf-0d56-4631-8ab8-8768f93fc029  rack1
UN  172.19.0.3  85.09 KiB   16      100.0%            9d6891f5-8d92-4713-ae2f-6f5fcf0fb3e6  rack1
```

---

## Keyspaces and Tables

### 3. Create three Keyspaces with RF = 1, 2, 3 using `cqlsh`
```bash
docker compose exec cassandra1 cqlsh

ATTENTION: All commands will be saved to history file: /root/.cassandra/cqlsh_history
This may include sensitive information such as passwords.
To disable history, use --disable-history or set 'disabled = true' in the [history] section of cqlshrc.
See https://cassandra.apache.org/doc/latest/tools/cqlsh.html for more information.

Connected to MyCluster at 127.0.0.1:9042
[cqlsh 6.2.0 | Cassandra 5.0.8 | CQL spec 3.4.7 | Native protocol v5]
Use HELP for help.
cqlsh> -- RF = 1
cqlsh> CREATE KEYSPACE ks_rf1
   ...   WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
cqlsh> 
cqlsh> -- RF = 2
cqlsh> CREATE KEYSPACE ks_rf2
   ...   WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 2};
cqlsh> 
cqlsh> -- RF = 3
cqlsh> CREATE KEYSPACE ks_rf3
   ...   WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
cqlsh> 
cqlsh> DESCRIBE KEYSPACES;

ks_rf1  ks_rf3  system_auth         system_schema  system_views         
ks_rf2  system  system_distributed  system_traces  system_virtual_schema
```

### 4. Create a table in each keyspace
```sql
cqlsh> USE ks_rf1;
cqlsh:ks_rf1> CREATE TABLE users (id UUID PRIMARY KEY, name TEXT, email TEXT);
cqlsh:ks_rf1> 
cqlsh:ks_rf1> USE ks_rf2;
cqlsh:ks_rf2> CREATE TABLE users (id UUID PRIMARY KEY, name TEXT, email TEXT);
cqlsh:ks_rf2> 
cqlsh:ks_rf2> USE ks_rf3;
cqlsh:ks_rf3> CREATE TABLE users (id UUID PRIMARY KEY, name TEXT, email TEXT);
cqlsh:ks_rf3> DESCRIBE TABLES;

users
```

### 5. Write and read from different nodes
```bash
# Insert data via cassandra1
ocker compose exec cassandra1 cqlsh

ATTENTION: All commands will be saved to history file: /root/.cassandra/cqlsh_history
This may include sensitive information such as passwords.
To disable history, use --disable-history or set 'disabled = true' in the [history] section of cqlshrc.
See https://cassandra.apache.org/doc/latest/tools/cqlsh.html for more information.

Connected to MyCluster at 127.0.0.1:9042
[cqlsh 6.2.0 | Cassandra 5.0.8 | CQL spec 3.4.7 | Native protocol v5]
Use HELP for help.
cqlsh> INSERT INTO ks_rf3.users (id, name, email) VALUES (uuid(), 'Alice', 'alice@example.com');
cqlsh> INSERT INTO ks_rf3.users (id, name, email) VALUES (uuid(), 'Bob',   'bob@example.com');
cqlsh> INSERT INTO ks_rf3.users (id, name, email) VALUES (uuid(), 'Carol', 'carol@example.com');
cqlsh> USE ks_rf3;
cqlsh:ks_rf3> SELECT * FROM users;

 id                                   | email             | name
--------------------------------------+-------------------+-------
 f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a |   bob@example.com |   Bob
 d703d279-6299-40ef-84c1-8172d821db56 | alice@example.com | Alice
 0bdf4385-4e29-4c38-9b46-b5560364ba00 | carol@example.com | Carol

(3 rows)
cqlsh:ks_rf3> 

docker compose exec cassandra2 cqlsh -e "SELECT * FROM ks_rf3.users;"

 id                                   | email             | name
--------------------------------------+-------------------+-------
 f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a |   bob@example.com |   Bob
 d703d279-6299-40ef-84c1-8172d821db56 | alice@example.com | Alice
 0bdf4385-4e29-4c38-9b46-b5560364ba00 | carol@example.com | Carol

(3 rows)

docker compose exec cassandra3 cqlsh -e "SELECT * FROM ks_rf3.users;"

 id                                   | email             | name
--------------------------------------+-------------------+-------
 f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a |   bob@example.com |   Bob
 d703d279-6299-40ef-84c1-8172d821db56 | alice@example.com | Alice
 0bdf4385-4e29-4c38-9b46-b5560364ba00 | carol@example.com | Carol

(3 rows)
```

### 6. Check data distribution with `nodetool status`
```bash
docker compose exec cassandra1 nodetool status ks_rf1
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load        Tokens  Owns (effective)  Host ID                               Rack 
UN  172.19.0.4  185.4 KiB   16      35.7%             7c191c80-5617-45f5-9fb1-9210bee8cf44  rack1
UN  172.19.0.2  170.31 KiB  16      32.7%             eea6c0bf-0d56-4631-8ab8-8768f93fc029  rack1
UN  172.19.0.3  190.76 KiB  16      31.6%             9d6891f5-8d92-4713-ae2f-6f5fcf0fb3e6  rack1

docker compose exec cassandra1 nodetool status ks_rf2
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load        Tokens  Owns (effective)  Host ID                               Rack 
UN  172.19.0.4  185.4 KiB   16      76.0%             7c191c80-5617-45f5-9fb1-9210bee8cf44  rack1
UN  172.19.0.2  170.31 KiB  16      64.7%             eea6c0bf-0d56-4631-8ab8-8768f93fc029  rack1
UN  172.19.0.3  190.76 KiB  16      59.3%             9d6891f5-8d92-4713-ae2f-6f5fcf0fb3e6  rack1

docker compose exec cassandra1 nodetool status ks_rf3
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load        Tokens  Owns (effective)  Host ID                               Rack 
UN  172.19.0.4  185.4 KiB   16      100.0%            7c191c80-5617-45f5-9fb1-9210bee8cf44  rack1
UN  172.19.0.2  170.31 KiB  16      100.0%            eea6c0bf-0d56-4631-8ab8-8768f93fc029  rack1
UN  172.19.0.3  190.76 KiB  16      100.0%            9d6891f5-8d92-4713-ae2f-6f5fcf0fb3e6  rack1


### 7. Show which nodes store a specific row (`nodetool getendpoints`)
```bash
docker compose exec cassandra1 nodetool getendpoints ks_rf1 users 9d6891f5-8d92-4713-ae2f-6f5fcf0fb3e6
172.19.0.4
docker compose exec cassandra1 nodetool getendpoints ks_rf2 users 9d6891f5-8d92-4713-ae2f-6f5fcf0fb3e6
172.19.0.4
172.19.0.3
docker compose exec cassandra1 nodetool getendpoints ks_rf3 users 9d6891f5-8d92-4713-ae2f-6f5fcf0fb3e6
172.19.0.4
172.19.0.3
172.19.0.2
```
> RF=1 → 1 IP; RF=2 → 2 IPs; RF=3 → 3 IPs

---

## Node Failure & Consistency Levels

### 8. Stop one node and test read/write with different consistency levels
```bash
docker compose stop cassandra3
[+] stop 1/1
 ✔ Container cassandra3 Stopped                                                                      
```

#### ks_rf1 — only CONSISTENCY ONE works
```bash
docker compose exec cassandra1 cqlsh
```
```sql
cqlsh> CONSISTENCY ONE;
Consistency level set to ONE.
cqlsh> SELECT * FROM ks_rf1.users;
NoHostAvailable: ('Unable to complete the operation against any hosts', {<Host: 127.0.0.1:9042 datacenter1>: Unavailable('Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level ONE" info={\'consistency\': \'ONE\', \'required_replicas\': 1, \'alive_replicas\': 0}')})                                                                                                                                    
cqlsh> INSERT INTO ks_rf1.users (id, name, email) VALUES (uuid(), 'D', 'd@x.com');
cqlsh> CONSISTENCY ONE;
Consistency level set to ONE.
cqlsh> CONSISTENCY TWO;
Consistency level set to TWO.
cqlsh> select * from ks_rf1.users;
NoHostAvailable: ('Unable to complete the operation against any hosts', {<Host: 127.0.0.1:9042 datacenter1>: Unavailable('Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level TWO" info={\'consistency\': \'TWO\', \'required_replicas\': 2, \'alive_replicas\': 1}')})      
```

#### ks_rf2 — CONSISTENCY ONE and TWO work (2 surviving nodes ≥ 2)
```sql
set to ONE.
cqlsh> SELECT * FROM ks_rf2.users;

 id                                   | email           | name
--------------------------------------+-----------------+------
 7186d5fa-b54a-410f-919c-42e640e6357f | bob@example.com |  Bob

(1 rows)
cqlsh> 
cqlsh> CONSISTENCY TWO;
Consistency level set to TWO.
cqlsh> SELECT * FROM ks_rf2.users;         -- OK (both surviving nodes respond)
NoHostAvailable: ('Unable to complete the operation against any hosts', {<Host: 127.0.0.1:9042 datacenter1>: Unavailable('Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level TWO" info={\'consistency\': \'TWO\', \'required_replicas\': 2, \'alive_replicas\': 1}')})                                                                                                                                    
cqlsh> 
cqlsh> CONSISTENCY THREE;
Consistency level set to THREE.
cqlsh> SELECT * FROM ks_rf2.users;    
NoHostAvailable: ('Unable to complete the operation against any hosts', {<Host: 127.0.0.1:9042 datacenter1>: Unavailable('Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level THREE" info={\'consistency\': \'THREE\', \'required_replicas\': 3, \'alive_replicas\': 2}')})                                                                                                                                
cqlsh> SELECT * FROM ks_rf1.users;    
NoHostAvailable: ('Unable to complete the operation against any hosts', {<Host: 127.0.0.1:9042 datacenter1>: Unavailable('Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level THREE" info={\'consistency\': \'THREE\', \'required_replicas\': 3, \'alive_replicas\': 1}')})                                                                                                                                

```

#### ks_rf3 — CONSISTENCY ONE, TWO, THREE all work (3 replicas, 2 nodes alive)
```sql
cqlsh> CONSISTENCY ONE;
Consistency level set to ONE.
cqlsh> SELECT * FROM ks_rf3.users;         -- OK

 id                                   | email             | name
--------------------------------------+-------------------+-------
 f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a |   bob@example.com |   Bob
 d703d279-6299-40ef-84c1-8172d821db56 | alice@example.com | Alice
 0bdf4385-4e29-4c38-9b46-b5560364ba00 | carol@example.com | Carol

(3 rows)
cqlsh> 
cqlsh> CONSISTENCY TWO;
Consistency level set to TWO.
cqlsh> SELECT * FROM ks_rf3.users;         -- OK

 id                                   | email             | name
--------------------------------------+-------------------+-------
 f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a |   bob@example.com |   Bob
 d703d279-6299-40ef-84c1-8172d821db56 | alice@example.com | Alice
 0bdf4385-4e29-4c38-9b46-b5560364ba00 | carol@example.com | Carol

(3 rows)
cqlsh> 
cqlsh> CONSISTENCY THREE;
Consistency level set to THREE.
cqlsh> SELECT * FROM ks_rf3.users;  
NoHostAvailable: ('Unable to complete the operation against any hosts', {<Host: 127.0.0.1:9042 datacenter1>: Unavailable('Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level THREE" info={\'consistency\': \'THREE\', \'required_replicas\': 3, \'alive_replicas\': 2}')})                                                                                                                                  -- UnavailableException (need all 3, only 2 alive)
```

```bash
# Restore the cluster
docker compose start cassandra3
```

---

## Network Partition & Conflict Resolution (Last Write Wins)

### 9. Isolate all three nodes from each other
```bash
docker network disconnect task8_cassandra-net cassandra1
docker network disconnect task8_cassandra-net cassandra2
docker network disconnect task8_cassandra-net cassandra3
docker network create net1
docker network create net2
docker network create net3
174f1cd30195d7a49ca35b544d9774a5dea87cb1714a064294b192be384bdeed
051928d6af96f31a169467f3bf6b056b98a581adc85aa496b6723990c0e69199
7b3c9cb40a85f3826e02b15dce48fce6f55311239d39cd95f65ba419560f5d6c
docker network connect net1 cassandra1
docker network connect net2 cassandra2
docker network connect net3 cassandra3
```

### 10. Insert conflicting rows (same PK, different values) on each isolated node
```bash
# cassandra1 — write value 'from_node1'  (timestamp T1)
docker compose exec cassandra1 cqlsh
cqlsh> CONSISTENCY ONE;
Consistency level set to ONE.
cqlsh> UPDATE ks_rf3.users SET name='from_node1' WHERE id=f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a;

# cassandra2 — write value 'from_node2'  (timestamp T2 > T1)
docker compose exec cassandra2 cqlsh
cqlsh> CONSISTENCY ONE;
Consistency level set to ONE.
cqlsh> UPDATE ks_rf3.users SET name='from_node2' WHERE id=f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a;

# cassandra3 — write value 'from_node3'  (timestamp T3 > T2)
docker compose exec cassandra3 cqlsh 
cqlsh> CONSISTENCY ONE;
Consistency level set to ONE.
cqlsh> UPDATE ks_rf3.users SET name='from_node3' WHERE id=f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a;
```

### 11. Restore connectivity and observe conflict resolution
```bash
docker network connect task8_cassandra-net cassandra1
docker network connect task8_cassandra-net cassandra2
docker network connect task8_cassandra-net cassandra3

# Wait for gossip to propagate (~30 s), then read
docker compose exec cassandra1 cqlsh

ATTENTION: All commands will be saved to history file: /root/.cassandra/cqlsh_history
This may include sensitive information such as passwords.
To disable history, use --disable-history or set 'disabled = true' in the [history] section of cqlshrc.
See https://cassandra.apache.org/doc/latest/tools/cqlsh.html for more information.

Connected to MyCluster at 127.0.0.1:9042
[cqlsh 6.2.0 | Cassandra 5.0.8 | CQL spec 3.4.7 | Native protocol v5]
Use HELP for help.
cqlsh> CONSISTENCY ONE;
Consistency level set to ONE.
cqlsh> SELECT id, name, writetime(name) FROM ks_rf3.users WHERE id=f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a;

 id                                   | name       | writetime(name)
--------------------------------------+------------+------------------
 f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a | from_node3 | 1781619965367279

(1 rows)
cqlsh> 
```
> **Result:** Cassandra resolves conflicts with **Last Write Wins (LWW)** using the
> client-supplied or server-generated write timestamp (microsecond precision).
> The row with the highest `writetime` survives on all nodes after repair/read-repair.

---

## Lightweight Transactions (LWT / Paxos)

### 12. LWT in a healthy cluster (all 3 nodes up)
```sql
-- INSERT ... IF NOT EXISTS — atomic compare-and-insert
cqlsh> INSERT INTO ks_rf3.users (id, name, email)
   ... VALUES (f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a, 'LWT_user', 'lwt@example.com')
   ... IF NOT EXISTS;

 [applied] | id                                   | email           | name
-----------+--------------------------------------+-----------------+------------
     False | f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a | bob@example.com | from_node3
 
-- UPDATE ... IF condition
cqlsh> UPDATE ks_rf3.users SET name = 'LWT_updated'
   ... WHERE id = f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a
   ... IF name = 'LWT_user';

 [applied] | name
-----------+------------
     False | from_node3
 
cqlsh> select * from ks_rf3.users ;

 id                                   | email             | name
--------------------------------------+-------------------+------------
 f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a |   bob@example.com | from_node3
 d703d279-6299-40ef-84c1-8172d821db56 | alice@example.com |      Alice
 0bdf4385-4e29-4c38-9b46-b5560364ba00 | carol@example.com |      Carol
```

### 13. LWT during network partition (nodes isolated)
```bash
# Isolate cassandra2 and cassandra3 again
docker network disconnect task8_cassandra-net cassandra2
docker network disconnect task8_cassandra-net cassandra3
```
```sql
-- On cassandra1 alone — Paxos quorum (2/3) cannot be reached
cqlsh> INSERT INTO ks_rf3.users (id, name, email)
   ... VALUES (uuid(), 'LWT_partition', 'p@x.com')
   ... IF NOT EXISTS;
NoHostAvailable: ('Unable to complete the operation against any hosts', {<Host: 127.0.0.1:9042 datacenter1>: Unavailable('Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level SERIAL" info={\'consistency\': \'SERIAL\', \'required_replicas\': 2, \'alive_replicas\': 1}')})                
-- WriteFailure / UnavailableException: Paxos requires quorum
```
```bash
# Restore
docker network connect task8_cassandra-net cassandra2
docker network connect task8_cassandra-net cassandra3
```
```sql
-- After restoring connectivity, Paxos can succeed again
cqlsh> INSERT INTO ks_rf3.users (id, name, email) VALUES (uuid(), 'LWT_partition', 'p@x.com') IF NOT EXISTS;

 [applied]
-----------
      True

cqlsh> select * from ks_rf3.users ;

 id                                   | email             | name
--------------------------------------+-------------------+---------------
 f1d9d4a5-335a-4afc-ba4a-d1af700b3e2a |   bob@example.com |    from_node3
 acce5703-4b70-4282-9657-a311d2ee85f0 |           p@x.com | LWT_partition
 d703d279-6299-40ef-84c1-8172d821db56 | alice@example.com |         Alice
 0bdf4385-4e29-4c38-9b46-b5560364ba00 | carol@example.com |         Carol

(4 rows)

---

## Performance Analysis & Integrity Check

### 14. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 15. Run with Consistency Level ONE
```bash
python perf_test.py --consistency one
```
```bash
python perf_test.py --consistency one

=======================================================
 Consistency Level = ONE
=======================================================
Schema setup done, counter reset to 0.
Starting 10 clients (10000 increments each)...
  [client-03] done
  [client-01] done
  [client-00] done
  [client-02] done
  [client-04] done
  [client-08] done
  [client-05] done
  [client-07] done
  [client-06] done
  [client-09] done

Time elapsed : 118.78s
Final value  : 100000
Expected     : 100000
Correct      : True
```

### 16. Run with Consistency Level QUORUM
```bash
python perf_test.py --consistency quorum
```
```bash
python perf_test.py --consistency quorum

=======================================================
 Consistency Level = QUORUM
=======================================================
Schema setup done, counter reset to 0.
Starting 10 clients (10000 increments each)...
  [client-00] done
  [client-03] done
  [client-09] done
  [client-05] done
  [client-06] done
  [client-02] done
  [client-01] done
  [client-08] done
  [client-04] done
  [client-07] done

Time elapsed : 78.43s
Final value  : 100000
Expected     : 100000
Correct      : True
```

