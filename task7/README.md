# Task 7 - Setting up replication and testing MongoDB fault tolerance

Protocol
-- 
I Setting up replication
1. Set up replication in the configuration: Primary with Two Secondary Members (P-S-S)
```bash
docker compose up --build -d
[+] up 3/3
 ✔ Container mongo3 Started                                                                                                                                                                                            1.2s
 ✔ Container mongo1 Started                                                                                                                                                                                            1.0s
 ✔ Container mongo2 Started                                                                          
```
```bash
docker compose logs mongo1 --tail 15
mongo1  | {"t":{"$date":"2026-06-16T11:24:46.181+00:00"},"s":"I",  "c":"WTCHKPT",  "id":22430,   "ctx":"Checkpointer","msg":"WiredTiger message","attr":{"message":{"ts_sec":1781609086,"ts_usec":181138,"thread":"1:0x781726f57640","session_name":"WT_SESSION.checkpoint","category":"WT_VERB_CHECKPOINT_PROGRESS","category_id":6,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"saving checkpoint snapshot min: 297, snapshot max: 297 snapshot count: 0, oldest timestamp: (1781608776, 1) , meta checkpoint timestamp: (1781609076, 1) base write gen: 1128"}}}
mongo1  | {"t":{"$date":"2026-06-16T11:24:54.817+00:00"},"s":"I",  "c":"CONNPOOL", "id":22576,   "ctx":"ReplNetwork","msg":"Connecting","attr":{"hostAndPort":"mongo3:27019"}}
mongo1  | {"t":{"$date":"2026-06-16T11:25:46.237+00:00"},"s":"I",  "c":"WTCHKPT",  "id":22430,   "ctx":"Checkpointer","msg":"WiredTiger message","attr":{"message":{"ts_sec":1781609146,"ts_usec":237162,"thread":"1:0x781726f57640","session_name":"WT_SESSION.checkpoint","category":"WT_VERB_CHECKPOINT_PROGRESS","category_id":6,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"saving checkpoint snapshot min: 311, snapshot max: 311 snapshot count: 0, oldest timestamp: (1781608836, 1) , meta checkpoint timestamp: (1781609136, 1) base write gen: 1128"}}}
mongo1  | {"t":{"$date":"2026-06-16T11:26:46.306+00:00"},"s":"I",  "c":"WTCHKPT",  "id":22430,   "ctx":"Checkpointer","msg":"WiredTiger message","attr":{"message":{"ts_sec":1781609206,"ts_usec":306727,"thread":"1:0x781726f57640","session_name":"WT_SESSION.checkpoint","category":"WT_VERB_CHECKPOINT_PROGRESS","category_id":6,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"saving checkpoint snapshot min: 325, snapshot max: 325 snapshot count: 0, oldest timestamp: (1781608896, 1) , meta checkpoint timestamp: (1781609196, 1) base write gen: 1128"}}}
mongo1  | {"t":{"$date":"2026-06-16T11:27:46.357+00:00"},"s":"I",  "c":"WTCHKPT",  "id":22430,   "ctx":"Checkpointer","msg":"WiredTiger message","attr":{"message":{"ts_sec":1781609266,"ts_usec":357529,"thread":"1:0x781726f57640","session_name":"WT_SESSION.checkpoint","category":"WT_VERB_CHECKPOINT_PROGRESS","category_id":6,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"saving checkpoint snapshot min: 339, snapshot max: 339 snapshot count: 0, oldest timestamp: (1781608956, 1) , meta checkpoint timestamp: (1781609256, 1) base write gen: 1128"}}}
mongo1  | {"t":{"$date":"2026-06-16T11:28:46.429+00:00"},"s":"I",  "c":"WTCHKPT",  "id":22430,   "ctx":"Checkpointer","msg":"WiredTiger message","attr":{"message":{"ts_sec":1781609326,"ts_usec":428956,"thread":"1:0x781726f57640","session_name":"WT_SESSION.checkpoint","category":"WT_VERB_CHECKPOINT_PROGRESS","category_id":6,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"saving checkpoint snapshot min: 353, snapshot max: 353 snapshot count: 0, oldest timestamp: (1781609016, 1) , meta checkpoint timestamp: (1781609316, 1) base write gen: 1128"}}}
mongo1  | {"t":{"$date":"2026-06-16T11:29:46.478+00:00"},"s":"I",  "c":"WTCHKPT",  "id":22430,   "ctx":"Checkpointer","msg":"WiredTiger message","attr":{"message":{"ts_sec":1781609386,"ts_usec":478439,"thread":"1:0x781726f57640","session_name":"WT_SESSION.checkpoint","category":"WT_VERB_CHECKPOINT_PROGRESS","category_id":6,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"saving checkpoint snapshot min: 369, snapshot max: 369 snapshot count: 0, oldest timestamp: (1781609086, 1) , meta checkpoint timestamp: (1781609386, 1) base write gen: 1128"}}}
mongo1  | {"t":{"$date":"2026-06-16T11:30:11.009+00:00"},"s":"I",  "c":"NETWORK",  "id":6496702, "ctx":"ReplCoord-12","msg":"Acquired connection for remote operation and completed writing to wire","attr":{"durationMicros":1045}}
mongo1  | {"t":{"$date":"2026-06-16T11:30:17.008+00:00"},"s":"I",  "c":"NETWORK",  "id":6496702, "ctx":"ReplCoord-10","msg":"Acquired connection for remote operation and completed writing to wire","attr":{"durationMicros":1181}}
mongo1  | {"t":{"$date":"2026-06-16T11:30:37.017+00:00"},"s":"I",  "c":"NETWORK",  "id":6496702, "ctx":"ReplCoord-12","msg":"Acquired connection for remote operation and completed writing to wire","attr":{"durationMicros":1079}}
mongo1  | {"t":{"$date":"2026-06-16T11:30:46.534+00:00"},"s":"I",  "c":"WTCHKPT",  "id":22430,   "ctx":"Checkpointer","msg":"WiredTiger message","attr":{"message":{"ts_sec":1781609446,"ts_usec":534405,"thread":"1:0x781726f57640","session_name":"WT_SESSION.checkpoint","category":"WT_VERB_CHECKPOINT_PROGRESS","category_id":6,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"saving checkpoint snapshot min: 383, snapshot max: 383 snapshot count: 0, oldest timestamp: (1781609146, 1) , meta checkpoint timestamp: (1781609446, 1) base write gen: 1128"}}}
mongo1  | {"t":{"$date":"2026-06-16T11:31:17.036+00:00"},"s":"I",  "c":"NETWORK",  "id":6496702, "ctx":"ReplCoord-12","msg":"Acquired connection for remote operation and completed writing to wire","attr":{"durationMicros":1021}}
mongo1  | {"t":{"$date":"2026-06-16T11:31:33.015+00:00"},"s":"I",  "c":"CONNPOOL", "id":22567,   "ctx":"ReplNetwork","msg":"Ending idle connection because the pool meets constraints","attr":{"hostAndPort":"mongo3:27019","numOpenConns":1}}
mongo1  | {"t":{"$date":"2026-06-16T11:31:46.592+00:00"},"s":"I",  "c":"WTCHKPT",  "id":22430,   "ctx":"Checkpointer","msg":"WiredTiger message","attr":{"message":{"ts_sec":1781609506,"ts_usec":592569,"thread":"1:0x781726f57640","session_name":"WT_SESSION.checkpoint","category":"WT_VERB_CHECKPOINT_PROGRESS","category_id":6,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"saving checkpoint snapshot min: 397, snapshot max: 397 snapshot count: 0, oldest timestamp: (1781609206, 1) , meta checkpoint timestamp: (1781609506, 1) base write gen: 1128"}}}
mongo1  | {"t":{"$date":"2026-06-16T11:31:47.026+00:00"},"s":"I",  "c":"CONNPOOL", "id":22567,   "ctx":"ReplNetwork","msg":"Ending idle connection because the pool meets constraints","attr":{"hostAndPort":"mongo2:27018","numOpenConns":1}}
```
2. Try to write with one node down and write concern level 3 and infinite timeout. Try to turn on the disconnected node during the timeout
```bash
docker compose stop mongo2
[+] stop 1/1
 ✔ Container mongo2 Stopped                                                                           
docker compose exec mongo1 mongosh --eval 'db.test.insertOne({name: "test", value: 1}, {writeConcern: {w: 3, wtimeout: 0}})'
{
  acknowledged: true,
  insertedId: ObjectId('6a31363a223052039e8563b1')
}
# the command above will hang until the write concern is satisfied. While it is hanging, start the mongo2 node again:
docker compose start mongo2
[+] start 1/1
 ✔ Container mongo2 Started                                                                          
```
3. Similarly to the previous point, but set a finite timeout and wait for it to expire. Check if the data was written and if it is available for reading with readConcern: "majority"
```bash
docker compose stop mongo2
[+] stop 1/1
 ✔ Container mongo2 Stopped
docker compose exec mongo1 mongosh --eval 'db.test.insertOne({name: "test2", value: 2}, {writeConcern: {w: 3, wtimeout: 5000}})'
MongoWriteConcernError: waiting for replication timed out

docker compose exec mongo1 mongosh --eval 'db.test.find({name: "test2"}).readConcern("majority")'
[
  {
    _id: ObjectId('6a31380f84178d6ce28563b1'),
    name: 'test2',
    value: 2
  }
]
```
3. Demonstrate primary node elections by disconnecting the current primary (Replica Set Elections)

```bash
docker compose exec mongo1 mongosh --eval 'rs.status().members.forEach(m => print(m.name, m.stateStr))'
mongo1:27017 PRIMARY
mongo2:27018 SECONDARY
mongo3:27019 SECONDARY
```

```bash
docker compose stop mongo1
[+] stop 1/1
 ✔ Container mongo1 Stopped
```
```bash 
docker compose exec mongo2 mongosh --port 27018 --eval 'rs.status().members.forEach(m => print(m.name, m.stateStr))'
mongo1:27017 (not reachable/healthy)
mongo2:27018 PRIMARY
mongo3:27019 SECONDARY
docker compose exec mongo2 mongosh --port 27018 --eval 'db.test.insertOne({name: "during_failover", value: 2})'
{
  acknowledged: true,
  insertedId: ObjectId('6a313a836a61d189238563b1')
}
```
```bash
docker compose start mongo1
[+] start 1/1
 ✔ Container mongo1 Started 
docker  compose exec mongo1 mongosh --eval 'rs.status().members.forEach(m => print(m.name, m.stateStr))'                                                                
mongo1:27017 PRIMARY
mongo2:27018 SECONDARY
mongo3:27019 SECONDARY
docker compose exec mongo1 mongosh --eval 'db.test.find({name: "during_failover"})'
[
  {
    _id: ObjectId('6a313a836a61d189238563b1'),
    name: 'during_failover',
    value: 2
  }
]
```
4. Inconsistent state simulation by disconnecting two secondary nodes, writing a value to the master with w:1, and checking its availability with different read concern levels
```bash
docker compose stop mongo2 mongo3
[+] stop 0/2
 ⠏ Container mongo3 Stopping                                                                                                                                                                                         
 ⠏ Container mongo2 Stopping    
docker compose exec mongo1 mongosh --eval 'db.test.insertOne({name: "inconsistent_test", value: 3}, {writeConcern: {w: 1}})'
docker compose exec mongo1 mongosh --eval 'db.test.insertOne({name: "inconsistent_value", value: 999}, {writeConcern: {w: 1}})'
{
  acknowledged: true,
  insertedId: ObjectId('6a313d8508f435736f8563b1')
}
docker compose exec mongo1 mongosh --eval 'db.test.find({name: "inconsistent_value"}).toArray()'
[
  {
    _id: ObjectId('6a313d045e1be98d718563b1'),
    name: 'inconsistent_value',
    value: 999
  }
]

docker  compose exec mongo1 mongosh --eval 'rs.status().members.forEach(m => print(m.name, m.stateStr))'            
mongo1:27017 SECONDARY
mongo2:27018 (not reachable/healthy)
mongo3:27019 (not reachable/healthy)

docker compose exec mongo1 mongosh --eval '                       
db.runCommand({
  find: "test",
  filter: {name: "inconsistent_value"},
  readConcern: {level: "local"}
})'
{
  cursor: {
    firstBatch: [
      {
        _id: ObjectId('6a313f18369150eb7b8563b1'),
        name: 'inconsistent_value',
        value: 999
      }
    ],
    id: Long('0'),
    ns: 'test.test'
  },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1781612324, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1781612324, i: 1 })
}

docker compose exec mongo1 mongosh --eval '                       
db.runCommand({
  find: "test",
  filter: {name: "inconsistent_value"},
  readConcern: {level: "majority"}
})'
{
  cursor: {
    firstBatch: [
      {
        _id: ObjectId('6a313f18369150eb7b8563b1'),
        name: 'inconsistent_value',
        value: 999
      }
    ],
    id: Long('0'),
    ns: 'test.test'
  },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1781612324, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1781612312, i: 1 })
}
ocker compose exec mongo1 mongosh --eval '
db.runCommand({
  find: "test",
  filter: {name: "inconsistent_value"},
  readConcern: {level: "linearizable"}
})'
MongoServerError: cannot satisfy linearizable read concern on non-primary node

docker compose stop mongo1
[+] stop 1/1
 ✔ Container mongo1 Stopped                                                                                                                                                                                           10.4s
docker compose start mongo2 mongo3
[+] start 2/2
 ✔ Container mongo2 Started                                                                                                                                                                                            0.7s
 ✔ Container mongo3 Started                                                                                                                                                                                            0.6s
docker compose start mongo1
[+] start 1/1
 ✔ Container mongo1 Started                                                                                   
docker compose exec mongo1 mongosh --eval 'db.test.find({name: "inconsistent_value"}).toArray()'
[] # the record is gone because the previous primary was not aware of the writes made while it was isolated from the other nodes.
```
5. Simulate eventual consistency by setting up replication delay for a replica
```bash
docker compose exec mongo1 mongosh --eval '
cfg = rs.conf()
// Find mongo3 member index
idx = cfg.members.findIndex(m => m.host.includes("mongo3"))
cfg.members[idx].priority = 0
cfg.members[idx].hidden = true
cfg.members[idx].secondaryDelaySecs = 60
rs.reconfig(cfg)
'
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1781613836, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1781613836, i: 1 })
}

docker compose exec mongo1 mongosh --eval 'rs.conf().members.forEach(m => print(m.host, "priority:", m.priority, "delay:", m.secondaryDelaySecs, "hidden:", m.hidden))'
mongo1:27017 priority: 2 delay: Long('0') hidden: false
mongo2:27018 priority: 1 delay: Long('0') hidden: false
mongo3:27019 priority: 0 delay: Long('60') hidden: true

docker compose stop mongo2
[+] stop 1/1
 ✔ Container mongo2 Stopped                                                                                                                                                                                           10.4s
vkhvorostianyi@vkhvorostianyi-Latitude-E6440:~/ssd/PycharmProjects/Distributed_Databases/task7$ docker compose exec mongo1 mongosh --eval '
db.test.insertMany([
  {name: "delayed_test_1", value: 1},
  {name: "delayed_test_2", value: 2},
  {name: "delayed_test_3", value: 3}
])'
# Waiting for the writes to be replicated (60 sec).
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a31457707fc40ea6d8563b1'),
    '1': ObjectId('6a31457707fc40ea6d8563b2'),
    '2': ObjectId('6a31457707fc40ea6d8563b3')
  }
}
docker compose exec mongo1 mongosh --eval '
db.runCommand({
  find: "test",
  filter: {name: "delayed_test_1"},
  readConcern: {level: "linearizable"},
  maxTimeMS: 10000
})'
MongoServerError: operation exceeded time limit
```
II Performance analysis and integrity check
1. Create a collection with a counter of likes, and run the code with writeConcern = 1
```bash
python perf_test.py --write-concern 1

=======================================================
 writeConcern = 1
=======================================================
Counter reset to 0
Starting 10 clients (10000 increments each)...
  [client-04] done
  [client-06] done
  [client-01] done
  [client-03] done
  [client-07] done
  [client-02] done
  [client-05] done
  [client-08] done
  [client-09] done
  [client-00] done

Time elapsed : 94.77s
Final value  : 100000
Expected     : 100000
Correct      : True
```
2. Run the same code with writeConcern = majority
```bash
python perf_test.py --write-concern majority

=======================================================
 writeConcern = majority
=======================================================
Counter reset to 0
Starting 10 clients (10000 increments each)...
  [client-07] done
  [client-03] done
  [client-01] done
  [client-08] done
  [client-09] done
  [client-04] done
  [client-05] done
  [client-02] done
  [client-00] done
  [client-06] done

Time elapsed : 165.02s
Final value  : 100000
Expected     : 100000
Correct      : True
```
3. Run the code with writeConcern = 1, but disconnect the Primary node during execution
```bash
python perf_test.py --write-concern 1

=======================================================
 writeConcern = 1
=======================================================
Counter reset to 0
Starting 10 clients (10000 increments each)...
  [client-08] done
  [client-05] done
  [client-00] done
  [client-04] done
  [client-09] done
  [client-07] done
  [client-01] done
  [client-02] done
  [client-06] done
  [client-03] done

Time elapsed : 88.14s
Final value  : 100000
Expected     : 100000
Correct      : True
```
4. Run the code with writeConcern = majority, but disconnect the Primary node during execution
```bash
python perf_test.py --write-concern majority

=======================================================
 writeConcern = majority
=======================================================
Counter reset to 0
Starting 10 clients (10000 increments each)...
  [client-01] done
  [client-02] done
  [client-00] done
  [client-09] done
  [client-04] done
  [client-07] done
  [client-08] done
  [client-06] done
  [client-03] done
  [client-05] done

Time elapsed : 152.25s
Final value  : 100000
Expected     : 100000
Correct      : True
```
