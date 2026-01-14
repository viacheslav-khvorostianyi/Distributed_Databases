```bash
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker-compose logs
Attaching to counter-client, hazelcast-node1, hazelcast-node3, hazelcast-node2
hazelcast-node3    | ########################################
hazelcast-node3    | # JAVA=/usr/bin/java
hazelcast-node3    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node3    | ########################################
hazelcast-node3    | 2026-01-14 18:50:34,045 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node3    | 2026-01-14 18:50:34,075 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | 2026-01-14 18:50:39,778 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node3    | 2026-01-14 18:50:40,212 [ INFO] [main] [c.h.s.logo]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node3    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node3    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node3    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node3    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node3    | 2026-01-14 18:50:40,212 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node3    | 2026-01-14 18:50:40,265 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.13]:5701
hazelcast-node3    | 2026-01-14 18:50:40,265 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node3    | 2026-01-14 18:50:40,266 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node3    | 2026-01-14 18:50:40,287 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node3    | To enable the Jet engine on the members, do one of the following:
hazelcast-node3    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node3    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node3    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    | 2026-01-14 18:50:48,226 [ INFO] [main] [c.h.s.security]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node3    | 2026-01-14 18:50:48,758 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node3    | 2026-01-14 18:50:48,785 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node3    | 2026-01-14 18:50:50,210 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node3    | 2026-01-14 18:50:50,242 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTING
hazelcast-node3    | 2026-01-14 18:50:50,515 [ INFO] [hz.wonderful_hertz.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.11:46037
hazelcast-node3    | 2026-01-14 18:50:50,756 [ INFO] [hz.wonderful_hertz.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:35989 and /172.28.0.11:5701
hazelcast-node3    | 2026-01-14 18:50:50,866 [ INFO] [hz.wonderful_hertz.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.12:43771
hazelcast-node3    | 2026-01-14 18:50:50,940 [ INFO] [hz.wonderful_hertz.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:57489 and /172.28.0.12:5701
hazelcast-node3    | 2026-01-14 18:50:55,584 [ INFO] [hz.wonderful_hertz.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:2, ver:2} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67 this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:50:55,619 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTED
hazelcast-node3    | 2026-01-14 18:50:55,782 [ INFO] [hz.wonderful_hertz.generic-operation.thread-1] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node1    | ########################################
hazelcast-node1    | # JAVA=/usr/bin/java
hazelcast-node1    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node1    | ########################################
hazelcast-node1    | 2026-01-14 18:50:34,256 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node1    | 2026-01-14 18:50:34,280 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | 2026-01-14 18:50:40,292 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node1    | 2026-01-14 18:50:40,546 [ INFO] [main] [c.h.s.logo]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node1    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node1    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node1    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node1    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node1    | 2026-01-14 18:50:40,547 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node1    | 2026-01-14 18:50:40,584 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.11]:5701
hazelcast-node1    | 2026-01-14 18:50:40,585 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node1    | 2026-01-14 18:50:40,586 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node1    | 2026-01-14 18:50:40,603 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node1    | To enable the Jet engine on the members, do one of the following:
hazelcast-node1    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node1    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node1    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    | 2026-01-14 18:50:48,214 [ INFO] [main] [c.h.s.security]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node1    | 2026-01-14 18:50:48,519 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node1    | 2026-01-14 18:50:48,533 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node1    | 2026-01-14 18:50:50,140 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node1    | 2026-01-14 18:50:50,179 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTING
hazelcast-node1    | 2026-01-14 18:50:50,713 [ INFO] [hz.epic_einstein.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:46037 and /172.28.0.13:5701
hazelcast-node1    | 2026-01-14 18:50:50,737 [ INFO] [hz.epic_einstein.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.13:35989
hazelcast-node1    | 2026-01-14 18:50:50,914 [ INFO] [hz.epic_einstein.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:60145 and /172.28.0.12:5701
hazelcast-node1    | 2026-01-14 18:50:50,916 [ INFO] [hz.epic_einstein.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.12:60437
hazelcast-node1    | 2026-01-14 18:50:55,440 [ INFO] [main] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:1, ver:1} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node3    | Members {size:3, ver:3} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67 this
hazelcast-node3    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:50:56,168 [ INFO] [hz.wonderful_hertz.cached.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupId
Seed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node3    | 2026-01-14 18:50:56,300 [ INFO] [hz.wonderful_hertz.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'}, RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}]
hazelcast-node3    | 2026-01-14 18:50:56,695 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node3    | 2026-01-14 18:50:58,854 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node3    | 2026-01-14 18:50:58,973 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node3    | 2026-01-14 18:50:59,042 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Moving to new term: 1 from current term: 0 after VoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 18:50:59,043 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:50:59,043 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 18:50:59,049 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}. currently voted-for: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node3    | 2026-01-14 18:50:59,175 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node3    | 2026-01-14 18:50:59,177 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    | 2026-01-14 18:50:55,464 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTED
hazelcast-node1    | 2026-01-14 18:50:55,551 [ INFO] [hz.epic_einstein.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:2, ver:2} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 this
hazelcast-node1    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:55,764 [ INFO] [hz.epic_einstein.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:3, ver:3} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 this
hazelcast-node1    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67
hazelcast-node1    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node2    | ########################################
hazelcast-node2    | # JAVA=/usr/bin/java
hazelcast-node2    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node2    | ########################################
hazelcast-node2    | 2026-01-14 18:50:33,866 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node2    | 2026-01-14 18:50:33,891 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | 2026-01-14 18:50:39,938 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node2    | 2026-01-14 18:50:40,199 [ INFO] [main] [c.h.s.logo]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node2    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node2    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node2    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node2    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node2    | 2026-01-14 18:50:40,200 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node2    | 2026-01-14 18:50:40,254 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.12]:5701
hazelcast-node2    | 2026-01-14 18:50:40,255 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node2    | 2026-01-14 18:50:40,266 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node2    | 2026-01-14 18:50:40,304 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node2    | To enable the Jet engine on the members, do one of the following:
hazelcast-node2    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node2    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node2    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node2    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node2    | 2026-01-14 18:50:48,595 [ INFO] [main] [c.h.s.security]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node2    | 2026-01-14 18:50:49,079 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node2    | 2026-01-14 18:50:49,096 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node2    | 2026-01-14 18:50:50,409 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node2    | 2026-01-14 18:50:50,471 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTING
hazelcast-node2    | 2026-01-14 18:50:50,859 [ INFO] [hz.goofy_joliot.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.11:60145
hazelcast-node2    | 2026-01-14 18:50:50,864 [ INFO] [hz.goofy_joliot.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.13:57489
hazelcast-node2    | 2026-01-14 18:50:50,909 [ INFO] [hz.goofy_joliot.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:43771 and /172.28.0.13:5701
hazelcast-node2    | 2026-01-14 18:50:50,919 [ INFO] [hz.goofy_joliot.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:60437 and /172.28.0.11:5701
hazelcast-node2    | 2026-01-14 18:50:55,795 [ INFO] [hz.goofy_joliot.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | Members {size:3, ver:3} [
hazelcast-node2    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node2    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67
hazelcast-node2    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644 this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:50:55,848 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTED
hazelcast-node2    | 2026-01-14 18:50:56,374 [ INFO] [hz.goofy_joliot.cached.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupIdSee
d=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 18:50:56,506 [ INFO] [hz.goofy_joliot.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'}, RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}]
hazelcast-node2    | 2026-01-14 18:50:56,516 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node2    | 2026-01-14 18:50:58,797 [ WARN] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are FOLLOWER and there is no current leader. Will start new election round...
hazelcast-node2    | 2026-01-14 18:50:58,807 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 18:50:58,807 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:0, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - FOLLOWER this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:50:59,012 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 18:50:59,013 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node2    | 2026-01-14 18:50:59,017 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Leader election started for term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 18:50:59,017 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - CANDIDATE this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:50:59,056 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored PreVoteResponse{voter=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, term=1, granted=true}. We are not FOLLOWER anymore.
hazelcast-node2    | 2026-01-14 18:50:59,078 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node2    | 2026-01-14 18:50:59,116 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}. currently voted-for: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node2    | 2026-01-14 18:50:59,130 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 18:50:59,131 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are the LEADER!
hazelcast-node2    | 2026-01-14 18:50:59,144 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - LEADER this
hazelcast-node2    | ]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - LEADER
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:51:00,118 [ INFO] [hz.wonderful_hertz.cached.thread-1] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]        
hazelcast-node3    | 2026-01-14 18:51:00,262 [ INFO] [hz.wonderful_hertz.generic-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985
c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node3    | 2026-01-14 18:51:14,636 [ INFO] [hz.wonderful_hertz.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id
=5, /172.28.0.13:5701->/172.28.0.3:52900, qualifier=null, endpoint=[172.28.0.3]:52900, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: df20191c-422e-4159-87bd-a3a81c7e93ee, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:51:22,493 [ INFO] [hz.wonderful_hertz.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.13:35989->/172.28.0.11:5701, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:22,495 [ INFO] [hz.wonderful_hertz.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=1, /172.28.0.13:5701->/172.28.0.11:46037, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:22,554 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:22,560 [ INFO] [hz.wonderful_hertz.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:22,566 [ INFO] [hz.wonderful_hertz.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:22,570 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:22,680 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:22,717 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:22,921 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:32,932 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connect timed out to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:33,036 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:35,515 [ INFO] [hz.wonderful_hertz.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=5, /172.28.0.13:5701->/172.28.0.3:52900, qualifier=null, endpoint=[172.28.0.3]:52900, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:35,542 [ INFO] [hz.wonderful_hertz.event-3] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=5, /172.28.0.13:5
701->/172.28.0.3:52900, qualifier=null, endpoint=[172.28.0.3]:52900, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416674615, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:51:43,046 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connect timed out to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:43,047 [ WARN] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.11]:5701 Cause => java.io.IOException {Connect timed out to address /172.28.0.11:5701}, Error-Count: 5
hazelcast-node3    | 2026-01-14 18:51:43,049 [ WARN] [hz.wonderful_hertz.cached.thread-5] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 is suspected to be dead for reason: No connection
hazelcast-node3    | 2026-01-14 18:51:43,049 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Starting mastership claim process...
hazelcast-node3    | 2026-01-14 18:51:43,056 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Local MembersView{version=3, members=[MemberInfo{address=[172.
28.0.11]:5701, uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, cpMemberUUID=null, liteMember=false, memberListJoinVersion=1}, MemberInfo{address=[172.28.0.13]:5701, uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, cpMemberUUID=null, liteMe
mber=false, memberListJoinVersion=2}, MemberInfo{address=[172.28.0.12]:5701, uuid=221562ed-985c-4023-8a45-56144f59f644, cpMemberUUID=null, liteMember=false, memberListJoinVersion=3}]} with suspected members: [Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239] and initial addresses to ask: [Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644]
hazelcast-node3    | 2026-01-14 18:51:43,071 [ INFO] [hz.wonderful_hertz.cached.thread-4] [c.h.i.p.i.PartitionStateManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    | 2026-01-14 18:51:43,074 [ INFO] [hz.wonderful_hertz.cached.thread-4] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:2, ver:4} [
hazelcast-node3    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67 this
hazelcast-node3    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:51:43,076 [ INFO] [hz.wonderful_hertz.cached.thread-4] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Mastership is claimed with: MembersView{version=4, members=[Me
mberInfo{address=[172.28.0.13]:5701, uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, cpMemberUUID=null, liteMember=false, memberListJoinVersion=2}, MemberInfo{address=[172.28.0.12]:5701, uuid=221562ed-985c-4023-8a45-56144f59f644, cpMemberUUID=null, liteMember=false, memberListJoinVersion=3}]}
hazelcast-node1    | 2026-01-14 18:50:56,098 [ INFO] [hz.epic_einstein.cached.thread-4] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupIdSe
ed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node1    | 2026-01-14 18:50:56,239 [ INFO] [hz.epic_einstein.cached.thread-4] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'}, RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}]
hazelcast-node1    | 2026-01-14 18:50:56,245 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node1    | 2026-01-14 18:50:56,329 [ INFO] [hz.epic_einstein.priority-generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initializing cluster partition table arrangement...
hazelcast-node1    | 2026-01-14 18:50:58,941 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node1    | 2026-01-14 18:50:58,953 [ WARN] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] We are FOLLOWER and there is no current leader. Will start new election round...
hazelcast-node1    | 2026-01-14 18:50:58,971 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 1, last log index: 0, last log term: 0
hazelcast-node1    | 2026-01-14 18:50:58,972 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:0, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:59,009 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'} for term: 1, number of votes: 2, majority: 2
hazelcast-node1    | 2026-01-14 18:50:59,010 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node1    | 2026-01-14 18:50:59,043 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Leader election started for term: 1, last log index: 0, last log term: 0
hazelcast-node1    | 2026-01-14 18:50:59,043 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} - CANDIDATE this
hazelcast-node1    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:59,163 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}. currently voted-for: RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}
hazelcast-node1    | 2026-01-14 18:50:59,228 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Ignored PreVoteResponse{voter=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, term=1, granted=true}. We are not FOLLOWER anymore.
hazelcast-node1    | 2026-01-14 18:50:59,244 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Demoting to FOLLOWER from current role: CANDIDATE, term: 1 to new term: 1 and leader: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node1    | 2026-01-14 18:50:59,246 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:59,249 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node1    | 2026-01-14 18:50:59,250 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - LEADER
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:51:00,014 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985
c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node1    | 2026-01-14 18:51:00,087 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=2}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985
c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node1    | 2026-01-14 18:51:00,199 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=3}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985
c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node1    | 2026-01-14 18:51:00,204 [ INFO] [hz.epic_einstein.cached.thread-4] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]
hazelcast-node1    | 2026-01-14 18:51:14,683 [ INFO] [hz.epic_einstein.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5
, /172.28.0.11:5701->/172.28.0.3:36718, qualifier=null, endpoint=[172.28.0.3]:36718, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: df20191c-422e-4159-87bd-a3a81c7e93ee, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | ########################################
hazelcast-node1    | # JAVA=/usr/bin/java
hazelcast-node1    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node1    | ########################################
hazelcast-node1    | 2026-01-14 18:52:19,182 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node1    | 2026-01-14 18:52:19,198 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | 2026-01-14 18:52:25,723 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node1    | 2026-01-14 18:52:26,088 [ INFO] [main] [c.h.s.logo]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] 
hazelcast-node1    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node1    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node1    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node1    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node2    |
hazelcast-node3    | 2026-01-14 18:51:43,084 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.t.TransactionManagerService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.11]:5701, UUID: e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    | 2026-01-14 18:51:43,094 [ WARN] [hz.wonderful_hertz.cached.thread-5] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node3    | 2026-01-14 18:51:43,328 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.InternalPartitionService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Fetching partition tables from cluster to determine the most recent one... Local stamp: 8082085890800019451
hazelcast-node3    | 2026-01-14 18:51:43,336 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.InternalPartitionService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Most recent partition table is determined.
hazelcast-node3    | 2026-01-14 18:51:43,336 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.InternalPartitionService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Applying the most recent of partition state...
hazelcast-node3    | 2026-01-14 18:51:43,351 [ WARN] [hz.wonderful_hertz.migration] [c.h.i.p.InternalPartitionService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Following unknown addresses are found in partition table sent from master[[172.28.0.13]:5701]. (Probably they have recently joined or left the cluster.) {
hazelcast-node3    |    [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    | }
hazelcast-node3    | 2026-01-14 18:51:43,568 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Repartitioning cluster data. Migration tasks count: 184
hazelcast-node3    | 2026-01-14 18:51:45,103 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] All migration tasks have been completed. (repartitionTime=Wed Jan 14 18:51:43 GMT 2026, plannedMigrations=184, completedMigrations=184, remainingMigrations=0, totalCompletedMigrations=184)
hazelcast-node3    | 2026-01-14 18:51:53,929 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Running shutdown hook... Current node state: ACTIVE
hazelcast-node3    | 2026-01-14 18:51:53,933 [ INFO] [hz.ShutdownThread] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is SHUTTING_DOWN
hazelcast-node1    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node1    | 2026-01-14 18:52:26,088 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node1    | 2026-01-14 18:52:26,165 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.11]:5701
hazelcast-node1    | 2026-01-14 18:52:26,166 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster                                                                                
hazelcast-node1    | 2026-01-14 18:52:26,166 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node1    | 2026-01-14 18:52:26,175 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node1    | To enable the Jet engine on the members, do one of the following:
hazelcast-node1    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node1    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node1    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    | 2026-01-14 18:52:32,054 [ INFO] [main] [c.h.s.security]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node1    | 2026-01-14 18:52:32,536 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node1    | 2026-01-14 18:52:32,553 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node1    | 2026-01-14 18:52:34,042 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node1    | 2026-01-14 18:52:34,090 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTING
hazelcast-node1    | 2026-01-14 18:52:34,769 [ INFO] [hz.compassionate_agnesi.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.13:33817
hazelcast-node1    | 2026-01-14 18:52:34,771 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:57505 and /172.28.0.13:5701
hazelcast-node1    | 2026-01-14 18:52:36,414 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.12:57023
hazelcast-node2    | 2026-01-14 18:50:59,183 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored VoteResponse{voter=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, term=1, granted=false}. We are not CANDIDATE anymore.
hazelcast-node2    | 2026-01-14 18:50:59,929 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c
-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 18:51:00,081 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=2}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c
-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 18:51:00,098 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=3}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c
-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 18:51:00,120 [ INFO] [hz.goofy_joliot.cached.thread-1] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]
hazelcast-node2    | 2026-01-14 18:51:14,769 [ INFO] [hz.goofy_joliot.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5, /172.28.
0.12:5701->/172.28.0.3:37202, qualifier=null, endpoint=[172.28.0.3]:37202, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: df20191c-422e-4159-87bd-a3a81c7e93ee, client name: hz.client_0, client version: 5.4.0
hazelcast-node2    | 2026-01-14 18:51:22,487 [ INFO] [hz.goofy_joliot.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=1, /172.28.0.12:5701->/172.28.0.11:60145, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node2    | 2026-01-14 18:51:22,499 [ INFO] [hz.goofy_joliot.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=3, /172.28.0.12:60437->/172.28.0.11:5701, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node2    | 2026-01-14 18:51:22,518 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:22,539 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:22,644 [ INFO] [hz.goofy_joliot.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:22,646 [ INFO] [hz.goofy_joliot.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:22,749 [ INFO] [hz.goofy_joliot.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:22,755 [ INFO] [hz.goofy_joliot.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:22,856 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:22,858 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:22,859 [ WARN] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.11]:5701 Cause => java.io.IOException {Connection refused to address /172.28.0.11:5701}, Error-Count: 5
hazelcast-node2    | 2026-01-14 18:51:22,860 [ WARN] [hz.goofy_joliot.cached.thread-3] [c.h.i.c.i.MembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 is suspected to be dead for reason: No connection
hazelcast-node2    | 2026-01-14 18:51:22,960 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:32,970 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connect timed out to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:32,971 [ WARN] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.11]:5701 Cause => java.io.IOException {Connect timed out to address /172.28.0.11:5701}, Error-Count: 6
hazelcast-node3    | 2026-01-14 18:51:53,933 [ INFO] [hz.wonderful_hertz.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.13:5701->/172.28.0.12:43771, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=221562ed-985c-4023-8a45-56144f59f644, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:53,936 [ WARN] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Terminating forcefully...
hazelcast-node3    | 2026-01-14 18:51:53,936 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Shutting down connection manager...
hazelcast-node3    | 2026-01-14 18:51:53,937 [ INFO] [hz.wonderful_hertz.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=3, /172.28.0.13:57489->/172.28.0.12:5701, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=221562ed-985c-4023-8a45-56144f59f644, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:53,942 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:53,944 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:51:53,944 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.c.i.TcpIpJoiner]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is added to the blacklist.
hazelcast-node3    | 2026-01-14 18:51:53,961 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Shutting down node engine...
hazelcast-node3    | 2026-01-14 18:51:54,015 [ INFO] [hz.ShutdownThread] [c.h.i.i.NodeExtension]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying node NodeExtension.
hazelcast-node3    | 2026-01-14 18:51:54,017 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Hazelcast Shutdown is completed in 82 ms.
hazelcast-node3    | ########################################
hazelcast-node3    | # JAVA=/usr/bin/java
hazelcast-node3    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node3    | ########################################
hazelcast-node3    | 2026-01-14 18:52:19,556 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node3    | 2026-01-14 18:52:19,566 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | 2026-01-14 18:52:25,699 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node3    | 2026-01-14 18:52:26,089 [ INFO] [main] [c.h.s.logo]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node3    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node3    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node3    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node3    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node3    | 2026-01-14 18:52:26,090 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node3    | 2026-01-14 18:52:26,128 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.13]:5701
hazelcast-node3    | 2026-01-14 18:52:26,143 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node3    | 2026-01-14 18:52:26,143 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node3    | 2026-01-14 18:52:26,149 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node3    | To enable the Jet engine on the members, do one of the following:
hazelcast-node3    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node3    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node3    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    | 2026-01-14 18:52:32,733 [ INFO] [main] [c.h.s.security]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node3    | 2026-01-14 18:52:33,033 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node3    | 2026-01-14 18:52:33,049 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node3    | 2026-01-14 18:52:34,206 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node2    | 2026-01-14 18:51:35,515 [ INFO] [hz.goofy_joliot.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=5, /172.28.0.12:5701->/172.28.0.3:37202, qualifier=null, endpoint=[172.28.0.3]:37202, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node2    | 2026-01-14 18:51:35,532 [ INFO] [hz.goofy_joliot.event-1] [c.h.c.i.ClientEndpointManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=5, /172.28.0.12:5701
->/172.28.0.3:37202, qualifier=null, endpoint=[172.28.0.3]:37202, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416674724, latest clientAttributes=null, labels=[]}
hazelcast-node2    | 2026-01-14 18:51:43,068 [ WARN] [hz.goofy_joliot.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Mastership of [172.28.0.13]:5701 is accepted. Resp
onse: MembersView{version=3, members=[MemberInfo{address=[172.28.0.13]:5701, uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, cpMemberUUID=null, liteMember=false, memberListJoinVersion=2}, MemberInfo{address=[172.28.0.12]:5701, uuid=221562ed-985c-4023-8a45-56144f59f644, cpMemberUUID=null, liteMember=false, memberListJoinVersion=3}]}
hazelcast-node2    | 2026-01-14 18:51:43,078 [ INFO] [hz.goofy_joliot.generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node2    | 2026-01-14 18:51:43,083 [ INFO] [hz.goofy_joliot.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | Members {size:2, ver:4} [
hazelcast-node2    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67
hazelcast-node2    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644 this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:51:43,088 [ INFO] [hz.goofy_joliot.cached.thread-4] [c.h.t.TransactionManagerService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.11]:5701, UUID: e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node2    | 2026-01-14 18:51:43,095 [ WARN] [hz.goofy_joliot.cached.thread-4] [c.h.c.i.RaftService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node2    | 2026-01-14 18:51:43,385 [ WARN] [hz.goofy_joliot.generic-operation.thread-0] [c.h.i.p.InternalPartitionService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Following unknown addresses are found in partition table sent from master[[172.28.0.13]:5701]. (Probably they have recently joined or left the cluster.) {
hazelcast-node2    |    [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node2    | }
hazelcast-node2    | 2026-01-14 18:51:53,922 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Running shutdown hook... Current node state: ACTIVE
hazelcast-node2    | 2026-01-14 18:51:53,923 [ INFO] [hz.ShutdownThread] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is SHUTTING_DOWN
hazelcast-node2    | 2026-01-14 18:51:53,925 [ WARN] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Terminating forcefully...
hazelcast-node2    | 2026-01-14 18:51:53,926 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Shutting down connection manager...
hazelcast-node2    | 2026-01-14 18:51:53,928 [ INFO] [hz.ShutdownThread] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.12:43771->/172.28.0.13:5701, qualifier=null, endpoint=[172.28.0.13]:5701, remoteUuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: TcpServer is stopping
hazelcast-node2    | 2026-01-14 18:51:53,937 [ INFO] [hz.ShutdownThread] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.12:5701->/172.28.0.13:57489, qualifier=null, endpoint=[172.28.0.13]:5701, remoteUuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: TcpServer is stopping
hazelcast-node3    | 2026-01-14 18:52:34,235 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTING
hazelcast-node3    | 2026-01-14 18:52:34,737 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.11:57505
hazelcast-node3    | 2026-01-14 18:52:34,826 [ INFO] [hz.jovial_lewin.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:33817 and /172.28.0.11:5701
hazelcast-node3    | 2026-01-14 18:52:36,409 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.12:49803
hazelcast-node3    | 2026-01-14 18:52:36,464 [ INFO] [hz.jovial_lewin.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:56483 and /172.28.0.12:5701
hazelcast-node1    | 2026-01-14 18:52:36,430 [ INFO] [hz.compassionate_agnesi.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:59043 and /172.28.0.12:5701
hazelcast-node1    | 2026-01-14 18:52:39,299 [ INFO] [main] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:1, ver:1} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:39,329 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTED
hazelcast-node3    | 2026-01-14 18:52:39,815 [ INFO] [hz.jovial_lewin.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node1    | 2026-01-14 18:52:39,452 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node2    | 2026-01-14 18:51:53,941 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Shutting down node engine...
hazelcast-node1    | Members {size:2, ver:2} [
hazelcast-node3    | Members {size:3, ver:3} [
hazelcast-node2    | 2026-01-14 18:51:54,000 [ INFO] [hz.ShutdownThread] [c.h.i.i.NodeExtension]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Destroying node NodeExtension.
hazelcast-node1    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f this
hazelcast-node3    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f
hazelcast-node2    | 2026-01-14 18:51:54,003 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Hazelcast Shutdown is completed in 76 ms.
hazelcast-node1    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node3    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node2    | ########################################
hazelcast-node1    | ]
hazelcast-node3    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86 this
hazelcast-node2    | # JAVA=/usr/bin/java
hazelcast-node1    |
hazelcast-node3    | ]
hazelcast-node2    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | 2026-01-14 18:52:39,678 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node2    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node1    |
hazelcast-node3    | 2026-01-14 18:52:39,817 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node2    | ########################################
hazelcast-node1    | Members {size:3, ver:3} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f this
hazelcast-node1    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node2    | 2026-01-14 18:52:20,463 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node2    | 2026-01-14 18:52:20,494 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | 2026-01-14 18:52:27,437 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node2    | 2026-01-14 18:52:27,783 [ INFO] [main] [c.h.s.logo]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node2    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node2    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node2    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node2    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node2    | 2026-01-14 18:52:27,794 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node2    | 2026-01-14 18:52:27,840 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.12]:5701
hazelcast-node3    | 2026-01-14 18:52:39,818 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node3    | 2026-01-14 18:52:39,819 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node1    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86
hazelcast-node3    | 2026-01-14 18:52:39,954 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTED
hazelcast-node2    | 2026-01-14 18:52:27,860 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node2    | 2026-01-14 18:52:27,872 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node3    | 2026-01-14 18:52:40,322 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupIdSee
d=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node2    | 2026-01-14 18:52:27,891 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node1    | ]
hazelcast-node3    | 2026-01-14 18:52:40,689 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}]
hazelcast-node2    | To enable the Jet engine on the members, do one of the following:
hazelcast-node1    |
hazelcast-node3    | 2026-01-14 18:52:40,729 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node2    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node1    | 2026-01-14 18:52:39,991 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{gr
oupIdSeed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node3    | 2026-01-14 18:52:40,777 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5, /172.28.
0.13:5701->/172.28.0.3:38150, qualifier=null, endpoint=[172.28.0.3]:38150, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: bac00adb-5981-4f88-82a1-65cd53999c6f, client name: hz.client_0, client version: 5.4.0
hazelcast-node2    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node1    | 2026-01-14 18:52:40,243 [ INFO] [hz.compassionate_agnesi.generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5, 
/172.28.0.11:5701->/172.28.0.3:43868, qualifier=null, endpoint=[172.28.0.3]:43868, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: bac00adb-5981-4f88-82a1-65cd53999c6f, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:52:42,437 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node2    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    | 2026-01-14 18:52:40,256 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initializing cluster partition table arrangement...
hazelcast-node3    | 2026-01-14 18:52:42,501 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Moving to new term: 1 from current term: 0 after VoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node2    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    | 2026-01-14 18:52:40,286 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}]
hazelcast-node3    | 2026-01-14 18:52:42,502 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    | 2026-01-14 18:52:34,067 [ INFO] [main] [c.h.s.security]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node1    | 2026-01-14 18:52:40,291 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node3    |
hazelcast-node2    | 2026-01-14 18:52:34,427 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node1    | 2026-01-14 18:52:42,417 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node1    | 2026-01-14 18:52:42,492 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Moving to new term: 1 from current term: 0 after VoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node2    | 2026-01-14 18:52:34,454 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node1    | 2026-01-14 18:52:42,494 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    | 2026-01-14 18:52:35,962 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node1    |
hazelcast-node2    | 2026-01-14 18:52:36,061 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTING
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    | 2026-01-14 18:52:36,418 [ INFO] [hz.inspiring_swirles.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.11:59043
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node2    | 2026-01-14 18:52:36,455 [ INFO] [hz.inspiring_swirles.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.13:56483
hazelcast-node2    | 2026-01-14 18:52:36,456 [ INFO] [hz.inspiring_swirles.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:49803 and /172.28.0.13:5701
hazelcast-node2    | 2026-01-14 18:52:36,460 [ INFO] [hz.inspiring_swirles.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:57023 and /172.28.0.11:5701
hazelcast-node2    | 2026-01-14 18:52:39,506 [ INFO] [hz.inspiring_swirles.generic-operation.thread-1] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node2    | Members {size:2, ver:2} [
hazelcast-node1    | 2026-01-14 18:52:42,494 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node2    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f
hazelcast-node1    | 2026-01-14 18:52:42,576 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}
hazelcast-node3    | ]
hazelcast-node2    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee this
hazelcast-node1    | 2026-01-14 18:52:42,577 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node3    | 2026-01-14 18:52:42,503 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 18:52:42,558 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}
hazelcast-node3    | 2026-01-14 18:52:42,558 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - LEADER
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:43,225 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]
hazelcast-node3    | 2026-01-14 18:52:43,257 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6
-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node3    | 2026-01-14 18:52:43,271 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=2}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6
-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node3    | 2026-01-14 18:52:43,272 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=3}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6
-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node3    | 2026-01-14 18:52:44,431 [ INFO] [hz.jovial_lewin.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.13:56483->/172.28.0.12:5701, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:52:44,452 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.13:5701->/172.28.0.12:49803, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:52:44,537 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true 
hazelcast-node3    | 2026-01-14 18:52:44,539 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:52:44,647 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true 
hazelcast-node3    | 2026-01-14 18:52:44,648 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:52:44,760 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true 
hazelcast-node3    | 2026-01-14 18:52:44,761 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:52:44,891 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true 
hazelcast-node3    | 2026-01-14 18:52:44,903 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:52:44,904 [ WARN] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.12]:5701 Cause => java.io.IOException {Connection refused to address /172.28.0.12:5701}, Error-Count: 5
hazelcast-node3    | 2026-01-14 18:52:44,906 [ WARN] [hz.jovial_lewin.cached.thread-1] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee is suspected to be dead for reason: No connection
hazelcast-node3    | 2026-01-14 18:52:44,947 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node3    | 2026-01-14 18:52:44,983 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:2, ver:4} [
hazelcast-node2    | 2026-01-14 18:52:39,508 [ INFO] [hz.inspiring_swirles.generic-operation.thread-0] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node1    |
hazelcast-node3    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f
hazelcast-node2    | 2026-01-14 18:52:39,529 [ INFO] [hz.inspiring_swirles.generic-operation.thread-0] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node2    | 2026-01-14 18:52:39,563 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTED
hazelcast-node3    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86 this
hazelcast-node2    | 2026-01-14 18:52:39,724 [ INFO] [hz.inspiring_swirles.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    | ]
hazelcast-node2    |
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - LEADER
hazelcast-node3    |
hazelcast-node2    | Members {size:3, ver:3} [
hazelcast-node2    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f
hazelcast-node3    | 2026-01-14 18:52:45,006 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.t.TransactionManagerService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.12]:5701, UUID: 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node3    | 2026-01-14 18:52:45,024 [ WARN] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node3    | 2026-01-14 18:52:45,253 [ WARN] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leader RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'} is not reachable. Will start new election round...
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node3    | 2026-01-14 18:52:45,260 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    | 2026-01-14 18:52:43,213 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]   
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:45,344 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 2, last log index: 4, last log term: 1
hazelcast-node3    | 2026-01-14 18:52:45,346 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:45,378 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, nextTerm=2, lastLogTerm=1, lastLogIndex=4}
hazelcast-node2    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee this
hazelcast-node2    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86
hazelcast-node1    | 2026-01-14 18:52:43,215 [ INFO] [hz.compassionate_agnesi.generic-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMember
sVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b
8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node2    | ]
hazelcast-node3    | 2026-01-14 18:52:45,502 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'} for term: 2, number of votes: 2, majority: 2
hazelcast-node1    | 2026-01-14 18:52:44,416 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.11:5701->/172.28.0.12:57023, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node2    |
hazelcast-node3    | 2026-01-14 18:52:45,518 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node2    | 2026-01-14 18:52:39,829 [ INFO] [hz.inspiring_swirles.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Received auth from Connection[
id=3, /172.28.0.12:5701->/172.28.0.3:51614, qualifier=null, endpoint=[172.28.0.3]:51614, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: bac00adb-5981-4f88-82a1-65cd53999c6f, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:52:44,403 [ WARN] [hz.compassionate_agnesi.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.11:59043->/172.28.0.12:5701, 
qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Exception in Connection[id=2, /172.28.0.11:59043->/172.28.0.12:5701, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=true, connectionType=MEMBER, planeIndex=0], thread=hz.compassionate_agnesi.IO.thread-in-1
hazelcast-node1    | java.net.SocketException: Connection reset
hazelcast-node3    | 2026-01-14 18:52:45,521 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Leader election started for term: 2, last log index: 4, last log term: 1
hazelcast-node1    |    at java.base/sun.nio.ch.SocketChannelImpl.throwConnectionReset(SocketChannelImpl.java:401) ~[?:?]
hazelcast-node1    |    at java.base/sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:434) ~[?:?]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioInboundPipeline.process(NioInboundPipeline.java:115) ~[hazelcast-5.4.0.jar:5.4.0]
hazelcast-node3    | 2026-01-14 18:52:45,522 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.processSelectionKey(NioThread.java:383) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.processSelectionKeys(NioThread.java:368) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.selectLoop(NioThread.java:294) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node3    |
hazelcast-node2    | 2026-01-14 18:52:39,966 [ INFO] [hz.inspiring_swirles.cached.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{group
IdSeed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.executeRun(NioThread.java:249) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:2, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - CANDIDATE this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:45,574 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, term=2, lastLogTerm=1, lastLogIndex=4, disruptive=false}. currently voted-for: RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}
hazelcast-node3    | 2026-01-14 18:52:47,553 [ WARN] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTimeoutTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Leader election for term: 2 has timed out!
hazelcast-node3    | 2026-01-14 18:52:47,554 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Leader election started for term: 3, last log index: 4, last log term: 1
hazelcast-node3    | 2026-01-14 18:52:47,555 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:3, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - CANDIDATE this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:47,639 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'} for term: 3, number of votes: 2, majority: 2
hazelcast-node3    | 2026-01-14 18:52:47,646 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] We are the LEADER!
hazelcast-node3    | 2026-01-14 18:52:47,651 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:3, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - LEADER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:53:44,494 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:53:44,497 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:53:44,509 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:53:44,510 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:53:44,512 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 18:53:44,513 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:53:44,518 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:53:44,518 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:53:44,519 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 18:54:45,735 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:54:45,736 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:54:45,738 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:54:45,739 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node2    | 2026-01-14 18:52:40,139 [ INFO] [hz.inspiring_swirles.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}]
hazelcast-node1    |    at com.hazelcast.internal.util.executor.HazelcastManagedThread.run(HazelcastManagedThread.java:111) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:54:45,739 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node2    | 2026-01-14 18:52:40,216 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node2    | 2026-01-14 18:52:42,315 [ WARN] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are FOLLOWER and there is no current leader. Will start new election round...
hazelcast-node3    | 2026-01-14 18:54:45,739 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node1    | 2026-01-14 18:52:44,715 [ INFO] [hz.compassionate_agnesi.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node2    | 2026-01-14 18:52:42,363 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 18:52:42,364 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:0, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - FOLLOWER this
hazelcast-node1    | 2026-01-14 18:52:44,761 [ INFO] [hz.compassionate_agnesi.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node2    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node1    | 2026-01-14 18:52:44,873 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node2    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node3    | 2026-01-14 18:54:45,741 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node1    | 2026-01-14 18:52:44,916 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node2    | ]
hazelcast-node3    | 2026-01-14 18:54:45,742 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node1    | 2026-01-14 18:52:44,917 [ WARN] [hz.compassionate_agnesi.cached.thread-6] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.12]:5701 Cause => java.io.IOException {Connection refused to address /172.28.0.12:5701}, Error-Count: 5
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:52:42,446 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 18:52:42,446 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node1    | 2026-01-14 18:52:44,930 [ INFO] [hz.compassionate_agnesi.cached.thread-1] [c.h.i.c.i.MembershipManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Removing Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node2    | 2026-01-14 18:52:42,449 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Leader election started for term: 1, last log index: 0, last log term: 0
hazelcast-node1    | 2026-01-14 18:52:44,933 [ INFO] [hz.compassionate_agnesi.cached.thread-1] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node1    | 2026-01-14 18:52:44,958 [ INFO] [hz.compassionate_agnesi.cached.thread-1] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node2    | 2026-01-14 18:52:42,449 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node1    | Members {size:2, ver:4} [
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    | 2026-01-14 18:54:45,742 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node1    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f this
hazelcast-node1    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86
hazelcast-node2    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - CANDIDATE this
hazelcast-node3    | 2026-01-14 18:55:46,989 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node1    | ]
hazelcast-node2    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    | 2026-01-14 18:55:46,990 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node1    |
hazelcast-node2    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node1    | 2026-01-14 18:52:44,962 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.t.TransactionManagerService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.12]:5701, UUID: 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node2    | ]
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:55:46,997 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    |
hazelcast-node3    | 2026-01-14 18:55:47,000 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node1    | 2026-01-14 18:52:44,981 [ WARN] [hz.compassionate_agnesi.cached.thread-6] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node2    | 2026-01-14 18:52:42,516 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored PreVoteResponse{voter=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=1, granted=true}. We are not FOLLOWER anymore.
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node1    | 2026-01-14 18:52:45,336 [ WARN] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Current leader RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'} is not reachable. Will start new election round...
hazelcast-node2    | 2026-01-14 18:52:42,519 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'} for term: 1, number of votes: 2, majority: 2
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node1    | 2026-01-14 18:52:45,337 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node2    | 2026-01-14 18:52:42,532 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are the LEADER!
hazelcast-node3    | 2026-01-14 18:55:47,000 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node2    | 2026-01-14 18:52:42,545 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    | 2026-01-14 18:55:47,001 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:55:47,003 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    |
hazelcast-node3    | 2026-01-14 18:55:47,004 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node1    | 2026-01-14 18:52:45,364 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 2, last log index: 4, last log term: 1
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - LEADER this
hazelcast-node2    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | 2026-01-14 18:52:45,365 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    | ]
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    | 2026-01-14 18:55:47,004 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 18:56:01,148 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=6,
 /172.28.0.13:5701->/172.28.0.2:40174, qualifier=null, endpoint=[172.28.0.2]:40174, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: ee8e5ceb-efd1-46e3-8da4-307725c6be3d, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:56:01,192 [ INFO] [hz.jovial_lewin.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=6, /172.28.0.13:5701->/172.28.0.2:40174, qualifier=null, endpoint=[172.28.0.2]:40174, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:56:01,264 [ INFO] [hz.jovial_lewin.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=6, /172.28.0.13:5701
->/172.28.0.2:40174, qualifier=null, endpoint=[172.28.0.2]:40174, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416961147, latest clientAttributes=null, labels=[]}
hazelcast-node2    |
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    | 2026-01-14 18:56:21,116 [ INFO] [hz.jovial_lewin.generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=7, /172.28.
0.13:5701->/172.28.0.2:52902, qualifier=null, endpoint=[172.28.0.2]:52902, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: d4864eff-b7b5-4cf1-981d-90546a3dbad0, client name: hz.client_0, client version: 5.4.0
hazelcast-node2    | 2026-01-14 18:52:42,549 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored VoteResponse{voter=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=1, granted=true}. We are not CANDIDATE anymore.
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node2    | 2026-01-14 18:52:43,188 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembers
Version{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8
-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:45,378 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, nextTerm=2, lastLogTerm=1, lastLogIndex=4}
hazelcast-node1    | 2026-01-14 18:52:45,477 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'} for term: 2, number of votes: 2, majority: 2
hazelcast-node1    | 2026-01-14 18:52:45,501 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node1    | 2026-01-14 18:52:45,502 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Leader election started for term: 2, last log index: 4, last log term: 1
hazelcast-node1    | 2026-01-14 18:52:45,503 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node2    | 2026-01-14 18:52:43,198 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembers
Version{groupIdSeed=0, version=2}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8
-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:2, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    | 2026-01-14 18:56:21,138 [ INFO] [hz.jovial_lewin.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=7, /172.28.0.13:5701->/172.28.0.2:52902, qualifier=null, endpoint=[172.28.0.2]:52902, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - CANDIDATE this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:45,548 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=2, lastLogTerm=1, lastLogIndex=4, disruptive=false}. currently voted-for: RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}
hazelcast-node1    | 2026-01-14 18:52:45,644 [ INFO] [hz.compassionate_agnesi.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Repartitioning cluster data. Migration tasks count: 182
hazelcast-node1    | 2026-01-14 18:52:47,592 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Demoting to FOLLOWER after VoteRequest{candidate=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=3, lastLogTerm=1, lastLogIndex=4, disruptive=false} since current term: 2 is smaller
hazelcast-node1    | 2026-01-14 18:52:47,593 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:3, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:47,609 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=3, lastLogTerm=1, lastLogIndex=4, disruptive=false}
hazelcast-node1    | 2026-01-14 18:52:47,659 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}
hazelcast-node1    | 2026-01-14 18:52:47,669 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:3, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - LEADER
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:47,836 [ INFO] [hz.compassionate_agnesi.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] All migration tasks have been completed. (repartitionTime=Wed Jan 14 18:52:45 GMT 2026, plannedMigrations=182, completedMigrations=182, remainingMigrations=0, totalCompletedMigrations=182)
hazelcast-node1    | 2026-01-14 18:56:01,125 [ INFO] [hz.compassionate_agnesi.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=6, 
/172.28.0.11:5701->/172.28.0.2:58840, qualifier=null, endpoint=[172.28.0.2]:58840, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: ee8e5ceb-efd1-46e3-8da4-307725c6be3d, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:56:01,192 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=6, /172.28.0.11:5701->/172.28.0.2:58840, qualifier=null, endpoint=[172.28.0.2]:58840, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:56:01,249 [ INFO] [hz.compassionate_agnesi.event-4] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=6, /172.28.0
.11:5701->/172.28.0.2:58840, qualifier=null, endpoint=[172.28.0.2]:58840, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416961123, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:56:21,101 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=7, /172.28.0.11:5701->/172.28.0.2:43450, qualifier=null, endpoint=[172.28.0.2]:43450, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: d4864eff-b7b5-4cf1-981d-90546a3dbad0, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:56:21,138 [ INFO] [hz.compassionate_agnesi.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=7, /172.28.0.11:5701->/172.28.0.2:43450, qualifier=null, endpoint=[172.28.0.2]:43450, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:56:21,139 [ INFO] [hz.compassionate_agnesi.event-4] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=7, /172.28.0
.11:5701->/172.28.0.2:43450, qualifier=null, endpoint=[172.28.0.2]:43450, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416981100, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:56:34,069 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=8, /172.28.0.11:5701->/172.28.0.2:46952, qualifier=null, endpoint=[172.28.0.2]:46952, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:56:34,097 [ INFO] [hz.compassionate_agnesi.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=8, /172.28.0.11:5701->/172.28.0.2:46952, qualifier=null, endpoint=[172.28.0.2]:46952, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:56:34,098 [ INFO] [hz.compassionate_agnesi.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=8, /172.28.0
.11:5701->/172.28.0.2:46952, qualifier=null, endpoint=[172.28.0.2]:46952, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416994068, latest clientAttributes=null, labels=[]}
hazelcast-node2    | 2026-01-14 18:52:43,201 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembers
Version{groupIdSeed=0, version=3}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8
-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node3    | 2026-01-14 18:56:21,144 [ INFO] [hz.jovial_lewin.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=7, /172.28.0.13:5701
->/172.28.0.2:52902, qualifier=null, endpoint=[172.28.0.2]:52902, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416981113, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:56:34,058 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=8, /172.28.
0.13:5701->/172.28.0.2:57292, qualifier=null, endpoint=[172.28.0.2]:57292, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, client name: hz.client_0, client version: 5.4.0
hazelcast-node2    | 2026-01-14 18:52:43,204 [ INFO] [hz.inspiring_swirles.cached.thread-1] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]      
hazelcast-node3    | 2026-01-14 18:56:34,098 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=8, /172.28.0.13:5701->/172.28.0.2:57292, qualifier=null, endpoint=[172.28.0.2]:57292, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:56:34,107 [ INFO] [hz.jovial_lewin.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=8, /172.28.0.13:5701
->/172.28.0.2:57292, qualifier=null, endpoint=[172.28.0.2]:57292, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416994057, latest clientAttributes=null, labels=[]}
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-pessimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 0
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-optimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 0
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-fail-optimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 74,422
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-fail-optimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 76,582
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-fail-optimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 77,329
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-fail-optimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 77,906
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker-compose logs | grep retry
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker kill hazelcast-node2
hazelcast-node2
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-fail-optimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 0
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-fail-pessimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 1,038
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker exec counter-client python -c "
import hazelcast
c = hazelcast.HazelcastClient(cluster_name='counter-cluster', cluster_members=['172.28.0.13:5701'])
m = c.get_map('counter-fail-pessimistic').blocking()
print(f'Counter: {m.get(\"counter\") or 0:,}')
c.shutdown()
"
Counter: 5,729
vkhvorostianyi@DESKTOP-31NCPOQ:/mnt/c/Users/10/PycharmProjects/Distributed_Databases/task3$ docker-compose logs
Attaching to counter-client, hazelcast-node1, hazelcast-node3, hazelcast-node2
hazelcast-node2    | ########################################
hazelcast-node2    | # JAVA=/usr/bin/java
hazelcast-node2    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node2    | ########################################
hazelcast-node2    | 2026-01-14 18:50:33,866 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node2    | 2026-01-14 18:50:33,891 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | 2026-01-14 18:50:39,938 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node2    | 2026-01-14 18:50:40,199 [ INFO] [main] [c.h.s.logo]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node2    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node2    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node2    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node2    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node2    | 2026-01-14 18:50:40,200 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node2    | 2026-01-14 18:50:40,254 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.12]:5701
hazelcast-node2    | 2026-01-14 18:50:40,255 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node2    | 2026-01-14 18:50:40,266 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node2    | 2026-01-14 18:50:40,304 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node2    | To enable the Jet engine on the members, do one of the following:
hazelcast-node2    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node2    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node2    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node2    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node2    | 2026-01-14 18:50:48,595 [ INFO] [main] [c.h.s.security]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node2    | 2026-01-14 18:50:49,079 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node2    | 2026-01-14 18:50:49,096 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node2    | 2026-01-14 18:50:50,409 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.
hazelcast-node2    | 2026-01-14 18:50:50,471 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTING
hazelcast-node2    | 2026-01-14 18:50:50,859 [ INFO] [hz.goofy_joliot.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.11:60145
hazelcast-node2    | 2026-01-14 18:50:50,864 [ INFO] [hz.goofy_joliot.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.13:57489
hazelcast-node2    | 2026-01-14 18:50:50,909 [ INFO] [hz.goofy_joliot.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:43771 and /172.28.0.13:5701
hazelcast-node2    | 2026-01-14 18:50:50,919 [ INFO] [hz.goofy_joliot.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:60437 and /172.28.0.11:5701
hazelcast-node2    | 2026-01-14 18:50:55,795 [ INFO] [hz.goofy_joliot.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | Members {size:3, ver:3} [
hazelcast-node2    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node2    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67
hazelcast-node2    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644 this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:50:55,848 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTED
hazelcast-node2    | 2026-01-14 18:50:56,374 [ INFO] [hz.goofy_joliot.cached.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupIdSee
d=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 18:50:56,506 [ INFO] [hz.goofy_joliot.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'}, RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}]
hazelcast-node2    | 2026-01-14 18:50:56,516 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node2    | 2026-01-14 18:50:58,797 [ WARN] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are FOLLOWER and there is no current leader. Will start new election round...
hazelcast-node2    | 2026-01-14 18:50:58,807 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 18:50:58,807 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:0, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - FOLLOWER this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:50:59,012 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 18:50:59,013 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node2    | 2026-01-14 18:50:59,017 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Leader election started for term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 18:50:59,017 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - CANDIDATE this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:50:59,056 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored PreVoteResponse{voter=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, term=1, granted=true}. We are not FOLLOWER anymore.
hazelcast-node2    | 2026-01-14 18:50:59,078 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node2    | 2026-01-14 18:50:59,116 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}. currently voted-for: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node2    | 2026-01-14 18:50:59,130 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 18:50:59,131 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are the LEADER!
hazelcast-node2    | 2026-01-14 18:50:59,144 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - LEADER this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:50:59,183 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored VoteResponse{voter=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, term=1, granted=false}. We are not CANDIDATE anymore.
hazelcast-node2    | 2026-01-14 18:50:59,929 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c
-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 18:51:00,081 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=2}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c
-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 18:51:00,098 [ INFO] [hz.goofy_joliot.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=3}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c
-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 18:51:00,120 [ INFO] [hz.goofy_joliot.cached.thread-1] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]
hazelcast-node2    | 2026-01-14 18:51:14,769 [ INFO] [hz.goofy_joliot.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5, /172.28.
0.12:5701->/172.28.0.3:37202, qualifier=null, endpoint=[172.28.0.3]:37202, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: df20191c-422e-4159-87bd-a3a81c7e93ee, client name: hz.client_0, client version: 5.4.0
hazelcast-node2    | 2026-01-14 18:51:22,487 [ INFO] [hz.goofy_joliot.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=1, /172.28.0.12:5701->/172.28.0.11:60145, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node2    | 2026-01-14 18:51:22,499 [ INFO] [hz.goofy_joliot.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=3, /172.28.0.12:60437->/172.28.0.11:5701, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node2    | 2026-01-14 18:51:22,518 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:22,539 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:22,644 [ INFO] [hz.goofy_joliot.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:22,646 [ INFO] [hz.goofy_joliot.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:22,749 [ INFO] [hz.goofy_joliot.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:22,755 [ INFO] [hz.goofy_joliot.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:22,856 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:22,858 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:22,859 [ WARN] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.11]:5701 Cause => java.io.IOException {Connection refused to address /172.28.0.11:5701}, Error-Count: 5
hazelcast-node2    | 2026-01-14 18:51:22,860 [ WARN] [hz.goofy_joliot.cached.thread-3] [c.h.i.c.i.MembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 is suspected to be dead for reason: No connection
hazelcast-node2    | 2026-01-14 18:51:22,960 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true 
hazelcast-node2    | 2026-01-14 18:51:32,970 [ INFO] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connect timed out to address /172.28.0.11:5701]
hazelcast-node2    | 2026-01-14 18:51:32,971 [ WARN] [hz.goofy_joliot.cached.thread-3] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.11]:5701 Cause => java.io.IOException {Connect timed out to address /172.28.0.11:5701}, Error-Count: 6
hazelcast-node2    | 2026-01-14 18:51:35,515 [ INFO] [hz.goofy_joliot.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=5, /172.28.0.12:5701->/172.28.0.3:37202, qualifier=null, endpoint=[172.28.0.3]:37202, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node2    | 2026-01-14 18:51:35,532 [ INFO] [hz.goofy_joliot.event-1] [c.h.c.i.ClientEndpointManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=5, /172.28.0.12:5701
->/172.28.0.3:37202, qualifier=null, endpoint=[172.28.0.3]:37202, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416674724, latest clientAttributes=null, labels=[]}
hazelcast-node2    | 2026-01-14 18:51:43,068 [ WARN] [hz.goofy_joliot.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Mastership of [172.28.0.13]:5701 is accepted. Resp
onse: MembersView{version=3, members=[MemberInfo{address=[172.28.0.13]:5701, uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, cpMemberUUID=null, liteMember=false, memberListJoinVersion=2}, MemberInfo{address=[172.28.0.12]:5701, uuid=221562ed-985c-4023-8a45-56144f59f644, cpMemberUUID=null, liteMember=false, memberListJoinVersion=3}]}
hazelcast-node2    | 2026-01-14 18:51:43,078 [ INFO] [hz.goofy_joliot.generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node2    | 2026-01-14 18:51:43,083 [ INFO] [hz.goofy_joliot.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | Members {size:2, ver:4} [
hazelcast-node2    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67
hazelcast-node2    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644 this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:51:43,088 [ INFO] [hz.goofy_joliot.cached.thread-4] [c.h.t.TransactionManagerService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.11]:5701, UUID: e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node2    | 2026-01-14 18:51:43,095 [ WARN] [hz.goofy_joliot.cached.thread-4] [c.h.c.i.RaftService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node2    | 2026-01-14 18:51:43,385 [ WARN] [hz.goofy_joliot.generic-operation.thread-0] [c.h.i.p.InternalPartitionService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Following unknown addresses are found in partition table sent from master[[172.28.0.13]:5701]. (Probably they have recently joined or left the cluster.) {
hazelcast-node2    |    [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node2    | }
hazelcast-node2    | 2026-01-14 18:51:53,922 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Running shutdown hook... Current node state: ACTIVE
hazelcast-node2    | 2026-01-14 18:51:53,923 [ INFO] [hz.ShutdownThread] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is SHUTTING_DOWN
hazelcast-node2    | 2026-01-14 18:51:53,925 [ WARN] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Terminating forcefully...
hazelcast-node2    | 2026-01-14 18:51:53,926 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Shutting down connection manager...
hazelcast-node2    | 2026-01-14 18:51:53,928 [ INFO] [hz.ShutdownThread] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.12:43771->/172.28.0.13:5701, qualifier=null, endpoint=[172.28.0.13]:5701, remoteUuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: TcpServer is stopping
hazelcast-node2    | 2026-01-14 18:51:53,937 [ INFO] [hz.ShutdownThread] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.12:5701->/172.28.0.13:57489, qualifier=null, endpoint=[172.28.0.13]:5701, remoteUuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: TcpServer is stopping
hazelcast-node2    | 2026-01-14 18:51:53,941 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Shutting down node engine...
hazelcast-node2    | 2026-01-14 18:51:54,000 [ INFO] [hz.ShutdownThread] [c.h.i.i.NodeExtension]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Destroying node NodeExtension.
hazelcast-node2    | 2026-01-14 18:51:54,003 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Hazelcast Shutdown is completed in 76 ms.
hazelcast-node2    | ########################################
hazelcast-node2    | # JAVA=/usr/bin/java
hazelcast-node2    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node2    | ########################################
hazelcast-node2    | 2026-01-14 18:52:20,463 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node2    | 2026-01-14 18:52:20,494 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | 2026-01-14 18:52:27,437 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node2    | 2026-01-14 18:52:27,783 [ INFO] [main] [c.h.s.logo]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node2    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node2    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node2    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node2    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node2    | 2026-01-14 18:52:27,794 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node2    | 2026-01-14 18:52:27,840 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.12]:5701
hazelcast-node2    | 2026-01-14 18:52:27,860 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node2    | 2026-01-14 18:52:27,872 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node2    | 2026-01-14 18:52:27,891 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node2    | To enable the Jet engine on the members, do one of the following:
hazelcast-node2    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node2    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node2    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node2    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node2    | 2026-01-14 18:52:34,067 [ INFO] [main] [c.h.s.security]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node2    | 2026-01-14 18:52:34,427 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node2    | 2026-01-14 18:52:34,454 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node2    | 2026-01-14 18:52:35,962 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node2    | 2026-01-14 18:52:36,061 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTING
hazelcast-node2    | 2026-01-14 18:52:36,418 [ INFO] [hz.inspiring_swirles.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.11:59043
hazelcast-node2    | 2026-01-14 18:52:36,455 [ INFO] [hz.inspiring_swirles.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.13:56483
hazelcast-node2    | 2026-01-14 18:52:36,456 [ INFO] [hz.inspiring_swirles.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:49803 and /172.28.0.13:5701
hazelcast-node2    | 2026-01-14 18:52:36,460 [ INFO] [hz.inspiring_swirles.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:57023 and /172.28.0.11:5701
hazelcast-node2    | 2026-01-14 18:52:39,506 [ INFO] [hz.inspiring_swirles.generic-operation.thread-1] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | Members {size:2, ver:2} [
hazelcast-node2    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f
hazelcast-node2    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:52:39,508 [ INFO] [hz.inspiring_swirles.generic-operation.thread-0] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node2    | 2026-01-14 18:52:39,529 [ INFO] [hz.inspiring_swirles.generic-operation.thread-0] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node2    | 2026-01-14 18:52:39,563 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTED
hazelcast-node2    | 2026-01-14 18:52:39,724 [ INFO] [hz.inspiring_swirles.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | Members {size:3, ver:3} [
hazelcast-node2    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f
hazelcast-node2    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee this
hazelcast-node2    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:52:39,829 [ INFO] [hz.inspiring_swirles.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Received auth from Connection[
id=3, /172.28.0.12:5701->/172.28.0.3:51614, qualifier=null, endpoint=[172.28.0.3]:51614, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: bac00adb-5981-4f88-82a1-65cd53999c6f, client name: hz.client_0, client version: 5.4.0
hazelcast-node2    | 2026-01-14 18:52:39,966 [ INFO] [hz.inspiring_swirles.cached.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{group
IdSeed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node2    | 2026-01-14 18:52:40,139 [ INFO] [hz.inspiring_swirles.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}]
hazelcast-node2    | 2026-01-14 18:52:40,216 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node2    | 2026-01-14 18:52:42,315 [ WARN] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are FOLLOWER and there is no current leader. Will start new election round...
hazelcast-node2    | 2026-01-14 18:52:42,363 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 18:52:42,364 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:0, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - FOLLOWER this
hazelcast-node2    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:52:42,446 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 18:52:42,446 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node2    | 2026-01-14 18:52:42,449 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Leader election started for term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 18:52:42,449 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - CANDIDATE this
hazelcast-node2    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:52:42,516 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored PreVoteResponse{voter=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=1, granted=true}. We are not FOLLOWER anymore.
hazelcast-node2    | 2026-01-14 18:52:42,519 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 18:52:42,532 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are the LEADER!
hazelcast-node2    | 2026-01-14 18:52:42,545 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - LEADER this
hazelcast-node2    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node2    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 18:52:42,549 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored VoteResponse{voter=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=1, granted=true}. We are not CANDIDATE anymore.
hazelcast-node2    | 2026-01-14 18:52:43,188 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembers
Version{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8
-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node2    | 2026-01-14 18:52:43,198 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembers
Version{groupIdSeed=0, version=2}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8
-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node2    | 2026-01-14 18:52:43,201 [ INFO] [hz.inspiring_swirles.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembers
Version{groupIdSeed=0, version=3}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8
-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node2    | 2026-01-14 18:52:43,204 [ INFO] [hz.inspiring_swirles.cached.thread-1] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]      
hazelcast-node2    | ########################################
hazelcast-node2    | # JAVA=/usr/bin/java
hazelcast-node2    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node2    | ########################################
hazelcast-node2    | 2026-01-14 19:02:50,689 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node2    | 2026-01-14 19:02:50,723 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node2    | 2026-01-14 19:02:56,083 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node2    | 2026-01-14 19:02:57,212 [ INFO] [main] [c.h.s.logo]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node2    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node2    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node2    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node2    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node2    | 2026-01-14 19:02:57,212 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node2    | 2026-01-14 19:02:57,287 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.12]:5701
hazelcast-node2    | 2026-01-14 19:02:57,288 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node2    | 2026-01-14 19:02:57,288 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node2    | 2026-01-14 19:02:57,419 [ INFO] [main] [c.h.system]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node2    | To enable the Jet engine on the members, do one of the following:
hazelcast-node2    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node2    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node2    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node2    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node2    | 2026-01-14 19:03:05,277 [ INFO] [main] [c.h.s.security]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node2    | 2026-01-14 19:03:05,911 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node2    | 2026-01-14 19:03:05,916 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node1    | ########################################
hazelcast-node1    | # JAVA=/usr/bin/java
hazelcast-node1    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node1    | ########################################
hazelcast-node1    | 2026-01-14 18:50:34,256 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node1    | 2026-01-14 18:50:34,280 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | 2026-01-14 18:50:40,292 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node1    | 2026-01-14 18:50:40,546 [ INFO] [main] [c.h.s.logo]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node1    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node1    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node1    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node1    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node1    | 2026-01-14 18:50:40,547 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node1    | 2026-01-14 18:50:40,584 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.11]:5701
hazelcast-node1    | 2026-01-14 18:50:40,585 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node1    | 2026-01-14 18:50:40,586 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node1    | 2026-01-14 18:50:40,603 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node1    | To enable the Jet engine on the members, do one of the following:
hazelcast-node1    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node1    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node1    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    | 2026-01-14 18:50:48,214 [ INFO] [main] [c.h.s.security]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node1    | 2026-01-14 18:50:48,519 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node1    | 2026-01-14 18:50:48,533 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node1    | 2026-01-14 18:50:50,140 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node1    | 2026-01-14 18:50:50,179 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTING
hazelcast-node1    | 2026-01-14 18:50:50,713 [ INFO] [hz.epic_einstein.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:46037 and /172.28.0.13:5701
hazelcast-node1    | 2026-01-14 18:50:50,737 [ INFO] [hz.epic_einstein.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.13:35989
hazelcast-node1    | 2026-01-14 18:50:50,914 [ INFO] [hz.epic_einstein.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:60145 and /172.28.0.12:5701
hazelcast-node1    | 2026-01-14 18:50:50,916 [ INFO] [hz.epic_einstein.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.12:60437
hazelcast-node1    | 2026-01-14 18:50:55,440 [ INFO] [main] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:1, ver:1} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:55,464 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTED
hazelcast-node1    | 2026-01-14 18:50:55,551 [ INFO] [hz.epic_einstein.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:2, ver:2} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 this
hazelcast-node1    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:55,764 [ INFO] [hz.epic_einstein.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:3, ver:3} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 this
hazelcast-node1    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67
hazelcast-node1    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:56,098 [ INFO] [hz.epic_einstein.cached.thread-4] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupIdSe
ed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node1    | 2026-01-14 18:50:56,239 [ INFO] [hz.epic_einstein.cached.thread-4] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'}, RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}]
hazelcast-node1    | 2026-01-14 18:50:56,245 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node1    | 2026-01-14 18:50:56,329 [ INFO] [hz.epic_einstein.priority-generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initializing cluster partition table arrangement...
hazelcast-node1    | 2026-01-14 18:50:58,941 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node1    | 2026-01-14 18:50:58,953 [ WARN] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] We are FOLLOWER and there is no current leader. Will start new election round...
hazelcast-node1    | 2026-01-14 18:50:58,971 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 1, last log index: 0, last log term: 0
hazelcast-node1    | 2026-01-14 18:50:58,972 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:0, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:59,009 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'} for term: 1, number of votes: 2, majority: 2
hazelcast-node1    | 2026-01-14 18:50:59,010 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node1    | 2026-01-14 18:50:59,043 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Leader election started for term: 1, last log index: 0, last log term: 0
hazelcast-node1    | 2026-01-14 18:50:59,043 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} - CANDIDATE this
hazelcast-node1    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:59,163 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}. currently voted-for: RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}
hazelcast-node1    | 2026-01-14 18:50:59,228 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Ignored PreVoteResponse{voter=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, term=1, granted=true}. We are not FOLLOWER anymore.
hazelcast-node1    | 2026-01-14 18:50:59,244 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Demoting to FOLLOWER from current role: CANDIDATE, term: 1 to new term: 1 and leader: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node1    | 2026-01-14 18:50:59,246 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:50:59,249 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node1    | 2026-01-14 18:50:59,250 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - LEADER
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:51:00,014 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985
c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node2    | 2026-01-14 19:03:07,240 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node2    | 2026-01-14 19:03:07,288 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTING
hazelcast-node2    | 2026-01-14 19:03:07,538 [ INFO] [hz.compassionate_elbakyan.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.13:48297
hazelcast-node2    | 2026-01-14 19:03:07,676 [ INFO] [hz.compassionate_elbakyan.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:43479 and /172.28.0.13:5701
hazelcast-node2    | 2026-01-14 19:03:07,707 [ INFO] [hz.compassionate_elbakyan.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:5701 and /172.28.0.11:34857
hazelcast-node2    | 2026-01-14 19:03:07,819 [ INFO] [hz.compassionate_elbakyan.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.12:34429 and /172.28.0.11:5701
hazelcast-node2    | 2026-01-14 19:03:13,590 [ INFO] [hz.compassionate_elbakyan.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | Members {size:3, ver:3} [
hazelcast-node2    |    Member [172.28.0.11]:5701 - 40b6edb8-2f50-414d-aad7-721a1cef042d
hazelcast-node2    |    Member [172.28.0.13]:5701 - 835ef35e-0444-4929-b0a2-58679f9cdc66
hazelcast-node2    |    Member [172.28.0.12]:5701 - 923791b6-3d0d-41ce-86d6-26df8c076f0d this
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 19:03:13,591 [ INFO] [hz.compassionate_elbakyan.generic-operation.thread-1] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node2    | 2026-01-14 19:03:13,617 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is STARTED
hazelcast-node2    | 2026-01-14 19:03:13,919 [ INFO] [hz.compassionate_elbakyan.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5
, /172.28.0.12:5701->/172.28.0.3:46190, qualifier=null, endpoint=[172.28.0.3]:46190, remoteUuid=a868c835-82ad-4bec-addf-a9efc1153439, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: a868c835-82ad-4bec-addf-a9efc1153439, client name: hz.client_0, client version: 5.4.0
hazelcast-node2    | 2026-01-14 19:03:14,307 [ INFO] [hz.compassionate_elbakyan.cached.thread-2] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{
groupIdSeed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node2    | 2026-01-14 19:03:14,510 [ INFO] [hz.compassionate_elbakyan.cached.thread-2] [c.h.c.i.RaftService]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'}, RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, RaftEndpoint{uuid='40b6edb8-2f50-414d-aad7-721a1cef042d'}]
hazelcast-node2    | 2026-01-14 19:03:14,530 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node2    | 2026-01-14 19:03:16,840 [ WARN] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are FOLLOWER and there is no current leader. Will start new election round...
hazelcast-node2    | 2026-01-14 19:03:16,899 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 19:03:16,900 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] 
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:0, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701} - FOLLOWER this
hazelcast-node2    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 19:03:17,005 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='40b6edb8-2f50-414d-aad7-721a1cef042d'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 19:03:17,006 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node2    | 2026-01-14 19:03:17,008 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Leader election started for term: 1, last log index: 0, last log term: 0
hazelcast-node2    | 2026-01-14 19:03:17,009 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701} - CANDIDATE this
hazelcast-node2    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 19:03:17,082 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored PreVoteResponse{voter=RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'}, term=1, granted=true}. We are not FOLLOWER anymore.
hazelcast-node2    | 2026-01-14 19:03:17,150 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'} for term: 1, number of votes: 2, majority: 2
hazelcast-node2    | 2026-01-14 19:03:17,150 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] We are the LEADER!    
hazelcast-node1    | 2026-01-14 18:51:00,087 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=2}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985
c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node1    | 2026-01-14 18:51:00,199 [ INFO] [hz.epic_einstein.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=3}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985
c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node1    | 2026-01-14 18:51:00,204 [ INFO] [hz.epic_einstein.cached.thread-4] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]
hazelcast-node1    | 2026-01-14 18:51:14,683 [ INFO] [hz.epic_einstein.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5
, /172.28.0.11:5701->/172.28.0.3:36718, qualifier=null, endpoint=[172.28.0.3]:36718, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: df20191c-422e-4159-87bd-a3a81c7e93ee, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | ########################################
hazelcast-node1    | # JAVA=/usr/bin/java
hazelcast-node1    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node1    | ########################################
hazelcast-node1    | 2026-01-14 18:52:19,182 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node1    | 2026-01-14 18:52:19,198 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | 2026-01-14 18:52:25,723 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node1    | 2026-01-14 18:52:26,088 [ INFO] [main] [c.h.s.logo]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node1    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node1    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node1    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node1    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node1    | 2026-01-14 18:52:26,088 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node1    | 2026-01-14 18:52:26,165 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.11]:5701
hazelcast-node1    | 2026-01-14 18:52:26,166 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node1    | 2026-01-14 18:52:26,166 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node1    | 2026-01-14 18:52:26,175 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node1    | To enable the Jet engine on the members, do one of the following:
hazelcast-node1    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node1    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node1    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    | 2026-01-14 18:52:32,054 [ INFO] [main] [c.h.s.security]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node1    | 2026-01-14 18:52:32,536 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node1    | 2026-01-14 18:52:32,553 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node1    | 2026-01-14 18:52:34,042 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node1    | 2026-01-14 18:52:34,090 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTING
hazelcast-node1    | 2026-01-14 18:52:34,769 [ INFO] [hz.compassionate_agnesi.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.13:33817
hazelcast-node1    | 2026-01-14 18:52:34,771 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:57505 and /172.28.0.13:5701
hazelcast-node1    | 2026-01-14 18:52:36,414 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.12:57023
hazelcast-node1    | 2026-01-14 18:52:36,430 [ INFO] [hz.compassionate_agnesi.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:59043 and /172.28.0.12:5701
hazelcast-node1    | 2026-01-14 18:52:39,299 [ INFO] [main] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:1, ver:1} [
hazelcast-node2    | 2026-01-14 19:03:17,315 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0]
hazelcast-node2    |
hazelcast-node2    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node2    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}
hazelcast-node2    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701} - LEADER this
hazelcast-node2    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node2    | ]
hazelcast-node2    |
hazelcast-node2    | 2026-01-14 19:03:17,368 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Ignored VoteResponse{voter=RaftEndpoint{uuid='40b6edb8-2f50-414d-aad7-721a1cef042d'}, term=1, granted=true}. We are not CANDIDATE anymore.
hazelcast-node2    | 2026-01-14 19:03:18,052 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMe
mbersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b
6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node2    | 2026-01-14 19:03:18,173 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMe
mbersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b
6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node2    | 2026-01-14 19:03:18,175 [ INFO] [hz.compassionate_elbakyan.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMe
mbersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b
6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node2    | 2026-01-14 19:03:18,199 [ INFO] [hz.compassionate_elbakyan.cached.thread-2] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}] 
hazelcast-node1    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:39,329 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTED
hazelcast-node1    | 2026-01-14 18:52:39,452 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:2, ver:2} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f this
hazelcast-node1    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:39,678 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:3, ver:3} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f this
hazelcast-node1    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node1    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:39,991 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{gr
oupIdSeed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node1    | 2026-01-14 18:52:40,243 [ INFO] [hz.compassionate_agnesi.generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5, 
/172.28.0.11:5701->/172.28.0.3:43868, qualifier=null, endpoint=[172.28.0.3]:43868, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: bac00adb-5981-4f88-82a1-65cd53999c6f, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:52:40,256 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initializing cluster partition table arrangement...
hazelcast-node1    | 2026-01-14 18:52:40,286 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}]
hazelcast-node1    | 2026-01-14 18:52:40,291 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node1    | 2026-01-14 18:52:42,417 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node1    | 2026-01-14 18:52:42,492 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Moving to new term: 1 from current term: 0 after VoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node1    | 2026-01-14 18:52:42,494 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:42,494 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node1    | 2026-01-14 18:52:42,576 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}
hazelcast-node1    | 2026-01-14 18:52:42,577 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - LEADER
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:43,213 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]   
hazelcast-node1    | 2026-01-14 18:52:43,215 [ INFO] [hz.compassionate_agnesi.generic-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMember
sVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b
8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node1    | 2026-01-14 18:52:44,416 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.11:5701->/172.28.0.12:57023, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | ########################################
hazelcast-node3    | # JAVA=/usr/bin/java
hazelcast-node3    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node3    | ########################################
hazelcast-node3    | 2026-01-14 18:50:34,045 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node3    | 2026-01-14 18:50:34,075 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | 2026-01-14 18:50:39,778 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node3    | 2026-01-14 18:50:40,212 [ INFO] [main] [c.h.s.logo]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node3    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node3    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node3    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node3    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node3    | 2026-01-14 18:50:40,212 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node3    | 2026-01-14 18:50:40,265 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.13]:5701
hazelcast-node3    | 2026-01-14 18:50:40,265 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node3    | 2026-01-14 18:50:40,266 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node3    | 2026-01-14 18:50:40,287 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node3    | To enable the Jet engine on the members, do one of the following:
hazelcast-node3    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node3    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node3    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    | 2026-01-14 18:50:48,226 [ INFO] [main] [c.h.s.security]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node3    | 2026-01-14 18:50:48,758 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node3    | 2026-01-14 18:50:48,785 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node3    | 2026-01-14 18:50:50,210 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node3    | 2026-01-14 18:50:50,242 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTING
hazelcast-node3    | 2026-01-14 18:50:50,515 [ INFO] [hz.wonderful_hertz.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.11:46037
hazelcast-node3    | 2026-01-14 18:50:50,756 [ INFO] [hz.wonderful_hertz.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:35989 and /172.28.0.11:5701
hazelcast-node3    | 2026-01-14 18:50:50,866 [ INFO] [hz.wonderful_hertz.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.12:43771
hazelcast-node3    | 2026-01-14 18:50:50,940 [ INFO] [hz.wonderful_hertz.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:57489 and /172.28.0.12:5701
hazelcast-node3    | 2026-01-14 18:50:55,584 [ INFO] [hz.wonderful_hertz.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:2, ver:2} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67 this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:50:55,619 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTED
hazelcast-node3    | 2026-01-14 18:50:55,782 [ INFO] [hz.wonderful_hertz.generic-operation.thread-1] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:3, ver:3} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67 this
hazelcast-node3    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:50:56,168 [ INFO] [hz.wonderful_hertz.cached.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupId
Seed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node1    | 2026-01-14 18:52:44,403 [ WARN] [hz.compassionate_agnesi.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.11:59043->/172.28.0.12:5701, 
qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Exception in Connection[id=2, /172.28.0.11:59043->/172.28.0.12:5701, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=true, connectionType=MEMBER, planeIndex=0], thread=hz.compassionate_agnesi.IO.thread-in-1
hazelcast-node1    | java.net.SocketException: Connection reset
hazelcast-node1    |    at java.base/sun.nio.ch.SocketChannelImpl.throwConnectionReset(SocketChannelImpl.java:401) ~[?:?]
hazelcast-node1    |    at java.base/sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:434) ~[?:?]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioInboundPipeline.process(NioInboundPipeline.java:115) ~[hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.processSelectionKey(NioThread.java:383) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.processSelectionKeys(NioThread.java:368) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.selectLoop(NioThread.java:294) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.executeRun(NioThread.java:249) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.util.executor.HazelcastManagedThread.run(HazelcastManagedThread.java:111) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    | 2026-01-14 18:52:44,715 [ INFO] [hz.compassionate_agnesi.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node1    | 2026-01-14 18:52:44,761 [ INFO] [hz.compassionate_agnesi.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node1    | 2026-01-14 18:52:44,873 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node1    | 2026-01-14 18:52:44,916 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node1    | 2026-01-14 18:52:44,917 [ WARN] [hz.compassionate_agnesi.cached.thread-6] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.12]:5701 Cause => java.io.IOException {Connection refused to address /172.28.0.12:5701}, Error-Count: 5
hazelcast-node1    | 2026-01-14 18:52:44,930 [ INFO] [hz.compassionate_agnesi.cached.thread-1] [c.h.i.c.i.MembershipManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Removing Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node1    | 2026-01-14 18:52:44,933 [ INFO] [hz.compassionate_agnesi.cached.thread-1] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node1    | 2026-01-14 18:52:44,958 [ INFO] [hz.compassionate_agnesi.cached.thread-1] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:2, ver:4} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f this
hazelcast-node1    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:44,962 [ INFO] [hz.compassionate_agnesi.cached.thread-6] [c.h.t.TransactionManagerService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.12]:5701, UUID: 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node1    | 2026-01-14 18:52:44,981 [ WARN] [hz.compassionate_agnesi.cached.thread-6] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node1    | 2026-01-14 18:52:45,336 [ WARN] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Current leader RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'} is not reachable. Will start new election round...
hazelcast-node1    | 2026-01-14 18:52:45,337 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:45,364 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 2, last log index: 4, last log term: 1
hazelcast-node1    | 2026-01-14 18:52:45,365 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:45,378 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, nextTerm=2, lastLogTerm=1, lastLogIndex=4}
hazelcast-node1    | 2026-01-14 18:52:45,477 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'} for term: 2, number of votes: 2, majority: 2
hazelcast-node1    | 2026-01-14 18:52:45,501 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node1    | 2026-01-14 18:52:45,502 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Leader election started for term: 2, last log index: 4, last log term: 1
hazelcast-node1    | 2026-01-14 18:52:45,503 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:2, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    | 2026-01-14 18:50:56,300 [ INFO] [hz.wonderful_hertz.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='b604165b-e6f8-4b10-a1d4-4e77d80a6f67'}, RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}]
hazelcast-node3    | 2026-01-14 18:50:56,695 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node3    | 2026-01-14 18:50:58,854 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node3    | 2026-01-14 18:50:58,973 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node3    | 2026-01-14 18:50:59,042 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Moving to new term: 1 from current term: 0 after VoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 18:50:59,043 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:50:59,043 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 18:50:59,049 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='e27bd822-bb10-4779-9ea3-be7dd8ba5239'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}. currently voted-for: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node3    | 2026-01-14 18:50:59,175 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='221562ed-985c-4023-8a45-56144f59f644'}
hazelcast-node3    | 2026-01-14 18:50:59,177 [ INFO] [hz.wonderful_hertz.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    |    CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701} - LEADER
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:51:00,118 [ INFO] [hz.wonderful_hertz.cached.thread-1] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]        
hazelcast-node3    | 2026-01-14 18:51:00,262 [ INFO] [hz.wonderful_hertz.generic-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=0}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985
c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, address=[172.28.0.13]:5701}, CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701}, CPMember{uuid=221562ed-985c-4023-8a45-56144f59f644, address=[172.28.0.12]:5701}]}
hazelcast-node3    | 2026-01-14 18:51:14,636 [ INFO] [hz.wonderful_hertz.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id
=5, /172.28.0.13:5701->/172.28.0.3:52900, qualifier=null, endpoint=[172.28.0.3]:52900, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: df20191c-422e-4159-87bd-a3a81c7e93ee, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:51:22,493 [ INFO] [hz.wonderful_hertz.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.13:35989->/172.28.0.11:5701, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:22,495 [ INFO] [hz.wonderful_hertz.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=1, /172.28.0.13:5701->/172.28.0.11:46037, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:22,554 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:22,560 [ INFO] [hz.wonderful_hertz.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:22,566 [ INFO] [hz.wonderful_hertz.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:22,570 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:22,680 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:22,717 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connection refused to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:22,921 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:32,932 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connect timed out to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:33,036 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.11:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:35,515 [ INFO] [hz.wonderful_hertz.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=5, /172.28.0.13:5701->/172.28.0.3:52900, qualifier=null, endpoint=[172.28.0.3]:52900, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:35,542 [ INFO] [hz.wonderful_hertz.event-3] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=5, /172.28.0.13:5
701->/172.28.0.3:52900, qualifier=null, endpoint=[172.28.0.3]:52900, remoteUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=df20191c-422e-4159-87bd-a3a81c7e93ee, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416674615, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:51:43,046 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.11:5701. Reason: IOException[Connect timed out to address /172.28.0.11:5701]
hazelcast-node3    | 2026-01-14 18:51:43,047 [ WARN] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.11]:5701 Cause => java.io.IOException {Connect timed out to address /172.28.0.11:5701}, Error-Count: 5
hazelcast-node3    | 2026-01-14 18:51:43,049 [ WARN] [hz.wonderful_hertz.cached.thread-5] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239 is suspected to be dead for reason: No connection
hazelcast-node3    | 2026-01-14 18:51:43,049 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Starting mastership claim process...
hazelcast-node3    | 2026-01-14 18:51:43,056 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Local MembersView{version=3, members=[MemberInfo{address=[172.
28.0.11]:5701, uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, cpMemberUUID=null, liteMember=false, memberListJoinVersion=1}, MemberInfo{address=[172.28.0.13]:5701, uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, cpMemberUUID=null, liteMe
mber=false, memberListJoinVersion=2}, MemberInfo{address=[172.28.0.12]:5701, uuid=221562ed-985c-4023-8a45-56144f59f644, cpMemberUUID=null, liteMember=false, memberListJoinVersion=3}]} with suspected members: [Member [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239] and initial addresses to ask: [Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644]
hazelcast-node3    | 2026-01-14 18:51:43,071 [ INFO] [hz.wonderful_hertz.cached.thread-4] [c.h.i.p.i.PartitionStateManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    | 2026-01-14 18:51:43,074 [ INFO] [hz.wonderful_hertz.cached.thread-4] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:2, ver:4} [
hazelcast-node3    |    Member [172.28.0.13]:5701 - b604165b-e6f8-4b10-a1d4-4e77d80a6f67 this
hazelcast-node3    |    Member [172.28.0.12]:5701 - 221562ed-985c-4023-8a45-56144f59f644
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:51:43,076 [ INFO] [hz.wonderful_hertz.cached.thread-4] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Mastership is claimed with: MembersView{version=4, members=[Me
mberInfo{address=[172.28.0.13]:5701, uuid=b604165b-e6f8-4b10-a1d4-4e77d80a6f67, cpMemberUUID=null, liteMember=false, memberListJoinVersion=2}, MemberInfo{address=[172.28.0.12]:5701, uuid=221562ed-985c-4023-8a45-56144f59f644, cpMemberUUID=null, liteMember=false, memberListJoinVersion=3}]}
hazelcast-node3    | 2026-01-14 18:51:43,084 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.t.TransactionManagerService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.11]:5701, UUID: e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    | 2026-01-14 18:51:43,094 [ WARN] [hz.wonderful_hertz.cached.thread-5] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPMember{uuid=e27bd822-bb10-4779-9ea3-be7dd8ba5239, address=[172.28.0.11]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node3    | 2026-01-14 18:51:43,328 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.InternalPartitionService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Fetching partition tables from cluster to determine the most recent one... Local stamp: 8082085890800019451
hazelcast-node3    | 2026-01-14 18:51:43,336 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.InternalPartitionService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Most recent partition table is determined.
hazelcast-node3    | 2026-01-14 18:51:43,336 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.InternalPartitionService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Applying the most recent of partition state...
hazelcast-node3    | 2026-01-14 18:51:43,351 [ WARN] [hz.wonderful_hertz.migration] [c.h.i.p.InternalPartitionService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Following unknown addresses are found in partition table sent from master[[172.28.0.13]:5701]. (Probably they have recently joined or left the cluster.) {
hazelcast-node3    |    [172.28.0.11]:5701 - e27bd822-bb10-4779-9ea3-be7dd8ba5239
hazelcast-node3    | }
hazelcast-node3    | 2026-01-14 18:51:43,568 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Repartitioning cluster data. Migration tasks count: 184
hazelcast-node3    | 2026-01-14 18:51:45,103 [ INFO] [hz.wonderful_hertz.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] All migration tasks have been completed. (repartitionTime=Wed Jan 14 18:51:43 GMT 2026, plannedMigrations=184, completedMigrations=184, remainingMigrations=0, totalCompletedMigrations=184)
hazelcast-node3    | 2026-01-14 18:51:53,929 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Running shutdown hook... Current node state: ACTIVE
hazelcast-node3    | 2026-01-14 18:51:53,933 [ INFO] [hz.ShutdownThread] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is SHUTTING_DOWN
hazelcast-node3    | 2026-01-14 18:51:53,933 [ INFO] [hz.wonderful_hertz.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.13:5701->/172.28.0.12:43771, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=221562ed-985c-4023-8a45-56144f59f644, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:53,936 [ WARN] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Terminating forcefully...
hazelcast-node3    | 2026-01-14 18:51:53,936 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Shutting down connection manager...
hazelcast-node3    | 2026-01-14 18:51:53,937 [ INFO] [hz.wonderful_hertz.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=3, /172.28.0.13:57489->/172.28.0.12:5701, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=221562ed-985c-4023-8a45-56144f59f644, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:51:53,942 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 18:51:53,944 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:51:53,944 [ INFO] [hz.wonderful_hertz.cached.thread-5] [c.h.i.c.i.TcpIpJoiner]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.12]:5701 is added to the blacklist.
hazelcast-node3    | 2026-01-14 18:51:53,961 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Shutting down node engine...
hazelcast-node3    | 2026-01-14 18:51:54,015 [ INFO] [hz.ShutdownThread] [c.h.i.i.NodeExtension]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying node NodeExtension.
hazelcast-node3    | 2026-01-14 18:51:54,017 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Hazelcast Shutdown is completed in 82 ms.
hazelcast-node3    | ########################################
hazelcast-node3    | # JAVA=/usr/bin/java
hazelcast-node3    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node3    | ########################################
hazelcast-node3    | 2026-01-14 18:52:19,556 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node3    | 2026-01-14 18:52:19,566 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | 2026-01-14 18:52:25,699 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node3    | 2026-01-14 18:52:26,089 [ INFO] [main] [c.h.s.logo]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node3    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node3    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node3    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node3    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node3    | 2026-01-14 18:52:26,090 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node3    | 2026-01-14 18:52:26,128 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.13]:5701
hazelcast-node3    | 2026-01-14 18:52:26,143 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node3    | 2026-01-14 18:52:26,143 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node3    | 2026-01-14 18:52:26,149 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node3    | To enable the Jet engine on the members, do one of the following:
hazelcast-node3    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node3    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node3    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    | 2026-01-14 18:52:32,733 [ INFO] [main] [c.h.s.security]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node3    | 2026-01-14 18:52:33,033 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node3    | 2026-01-14 18:52:33,049 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node3    | 2026-01-14 18:52:34,206 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node3    | 2026-01-14 18:52:34,235 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTING
hazelcast-node3    | 2026-01-14 18:52:34,737 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.11:57505
hazelcast-node3    | 2026-01-14 18:52:34,826 [ INFO] [hz.jovial_lewin.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:33817 and /172.28.0.11:5701
hazelcast-node3    | 2026-01-14 18:52:36,409 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.12:49803
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - CANDIDATE this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:45,548 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=2, lastLogTerm=1, lastLogIndex=4, disruptive=false}. currently voted-for: RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}
hazelcast-node1    | 2026-01-14 18:52:45,644 [ INFO] [hz.compassionate_agnesi.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Repartitioning cluster data. Migration tasks count: 182
hazelcast-node1    | 2026-01-14 18:52:47,592 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Demoting to FOLLOWER after VoteRequest{candidate=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=3, lastLogTerm=1, lastLogIndex=4, disruptive=false} since current term: 2 is smaller
hazelcast-node1    | 2026-01-14 18:52:47,593 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:3, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:47,609 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}, term=3, lastLogTerm=1, lastLogIndex=4, disruptive=false}
hazelcast-node1    | 2026-01-14 18:52:47,659 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}
hazelcast-node1    | 2026-01-14 18:52:47,669 [ INFO] [hz.compassionate_agnesi.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:3, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - LEADER
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 18:52:47,836 [ INFO] [hz.compassionate_agnesi.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] All migration tasks have been completed. (repartitionTime=Wed Jan 14 18:52:45 GMT 2026, plannedMigrations=182, completedMigrations=182, remainingMigrations=0, totalCompletedMigrations=182)
hazelcast-node1    | 2026-01-14 18:56:01,125 [ INFO] [hz.compassionate_agnesi.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=6, 
/172.28.0.11:5701->/172.28.0.2:58840, qualifier=null, endpoint=[172.28.0.2]:58840, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: ee8e5ceb-efd1-46e3-8da4-307725c6be3d, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:56:01,192 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=6, /172.28.0.11:5701->/172.28.0.2:58840, qualifier=null, endpoint=[172.28.0.2]:58840, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:56:01,249 [ INFO] [hz.compassionate_agnesi.event-4] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=6, /172.28.0
.11:5701->/172.28.0.2:58840, qualifier=null, endpoint=[172.28.0.2]:58840, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416961123, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:56:21,101 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=7, /172.28.0.11:5701->/172.28.0.2:43450, qualifier=null, endpoint=[172.28.0.2]:43450, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: d4864eff-b7b5-4cf1-981d-90546a3dbad0, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:56:21,138 [ INFO] [hz.compassionate_agnesi.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=7, /172.28.0.11:5701->/172.28.0.2:43450, qualifier=null, endpoint=[172.28.0.2]:43450, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:56:21,139 [ INFO] [hz.compassionate_agnesi.event-4] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=7, /172.28.0
.11:5701->/172.28.0.2:43450, qualifier=null, endpoint=[172.28.0.2]:43450, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416981100, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:56:34,069 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=8, /172.28.0.11:5701->/172.28.0.2:46952, qualifier=null, endpoint=[172.28.0.2]:46952, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:56:34,097 [ INFO] [hz.compassionate_agnesi.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=8, /172.28.0.11:5701->/172.28.0.2:46952, qualifier=null, endpoint=[172.28.0.2]:46952, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:52:36,464 [ INFO] [hz.jovial_lewin.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:56483 and /172.28.0.12:5701
hazelcast-node3    | 2026-01-14 18:52:39,815 [ INFO] [hz.jovial_lewin.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:3, ver:3} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f
hazelcast-node3    |    Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node3    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86 this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:39,817 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node3    | 2026-01-14 18:52:39,818 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node3    | 2026-01-14 18:52:39,819 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node3    | 2026-01-14 18:52:39,954 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTED
hazelcast-node3    | 2026-01-14 18:52:40,322 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupIdSee
d=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node3    | 2026-01-14 18:52:40,689 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}]
hazelcast-node3    | 2026-01-14 18:52:40,729 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node3    | 2026-01-14 18:52:40,777 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5, /172.28.
0.13:5701->/172.28.0.3:38150, qualifier=null, endpoint=[172.28.0.3]:38150, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: bac00adb-5981-4f88-82a1-65cd53999c6f, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:52:42,437 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node3    | 2026-01-14 18:52:42,501 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Moving to new term: 1 from current term: 0 after VoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 18:52:42,502 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:42,503 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 18:52:42,558 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'}
hazelcast-node3    | 2026-01-14 18:52:42,558 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} - LEADER
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:43,225 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]
hazelcast-node3    | 2026-01-14 18:52:43,257 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=0}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6
-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node1    | 2026-01-14 18:56:34,098 [ INFO] [hz.compassionate_agnesi.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=8, /172.28.0
.11:5701->/172.28.0.2:46952, qualifier=null, endpoint=[172.28.0.2]:46952, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416994068, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:57:34,897 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=9, /172.28.0.11:5701->/172.28.0.2:36340, qualifier=null, endpoint=[172.28.0.2]:36340, remoteUuid=32b471d2-4047-40d7-9164-9ad7a8fa5141, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 32b471d2-4047-40d7-9164-9ad7a8fa5141, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:57:34,921 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=9, /172.28.0.11:5701->/172.28.0.2:36340, qualifier=null, endpoint=[172.28.0.2]:36340, remoteUuid=32b471d2-4047-40d7-9164-9ad7a8fa5141, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:57:34,923 [ INFO] [hz.compassionate_agnesi.event-4] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=9, /172.28.0
.11:5701->/172.28.0.2:36340, qualifier=null, endpoint=[172.28.0.2]:36340, remoteUuid=32b471d2-4047-40d7-9164-9ad7a8fa5141, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=32b471d2-4047-40d7-9164-9ad7a8fa5141, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417054896, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:57:48,609 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=10, /172.28.0.11:5701->/172.28.0.2:43936, qualifier=null, endpoint=[172.28.0.2]:43936, remoteUuid=7bcf6006-d2a0-49a5-976b-ca8f0f35e466, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 7bcf6006-d2a0-49a5-976b-ca8f0f35e466, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:57:48,633 [ INFO] [hz.compassionate_agnesi.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=10, /172.28.0.11:5701->/172.28.0.2:43936, qualifier=null, endpoint=[172.28.0.2]:43936, remoteUuid=7bcf6006-d2a0-49a5-976b-ca8f0f35e466, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:57:48,634 [ INFO] [hz.compassionate_agnesi.event-3] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=10, /172.28.
0.11:5701->/172.28.0.2:43936, qualifier=null, endpoint=[172.28.0.2]:43936, remoteUuid=7bcf6006-d2a0-49a5-976b-ca8f0f35e466, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=7bcf6006-d2a0-49a5-976b-ca8f0f35e466, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417068608, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:58:40,031 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=11, /172.28.0.11:5701->/172.28.0.2:43134, qualifier=null, endpoint=[172.28.0.2]:43134, remoteUuid=33a3b671-b112-4b04-bf1f-a84860d6f393, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 33a3b671-b112-4b04-bf1f-a84860d6f393, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:58:40,052 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=11, /172.28.0.11:5701->/172.28.0.2:43134, qualifier=null, endpoint=[172.28.0.2]:43134, remoteUuid=33a3b671-b112-4b04-bf1f-a84860d6f393, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:58:40,053 [ INFO] [hz.compassionate_agnesi.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=11, /172.28.
0.11:5701->/172.28.0.2:43134, qualifier=null, endpoint=[172.28.0.2]:43134, remoteUuid=33a3b671-b112-4b04-bf1f-a84860d6f393, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=33a3b671-b112-4b04-bf1f-a84860d6f393, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417120030, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:58:50,075 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=12, /172.28.0.11:5701->/172.28.0.2:56828, qualifier=null, endpoint=[172.28.0.2]:56828, remoteUuid=45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:58:50,126 [ INFO] [hz.compassionate_agnesi.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=12, /172.28.0.11:5701->/172.28.0.2:56828, qualifier=null, endpoint=[172.28.0.2]:56828, remoteUuid=45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:58:50,130 [ INFO] [hz.compassionate_agnesi.event-1] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=12, /172.28.
0.11:5701->/172.28.0.2:56828, qualifier=null, endpoint=[172.28.0.2]:56828, remoteUuid=45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417130074, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:58:53,982 [ INFO] [hz.compassionate_agnesi.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=13, /172.28.0.11:5701->/172.28.0.2:41644, qualifier=null, endpoint=[172.28.0.2]:41644, remoteUuid=989aad82-3ed9-4649-b099-d18fc8ddf04d, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 989aad82-3ed9-4649-b099-d18fc8ddf04d, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:58:54,010 [ INFO] [hz.compassionate_agnesi.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=13, /172.28.0.11:5701->/172.28.0.2:41644, qualifier=null, endpoint=[172.28.0.2]:41644, remoteUuid=989aad82-3ed9-4649-b099-d18fc8ddf04d, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:52:43,271 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=2}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6
-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node3    | 2026-01-14 18:52:43,272 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersi
on{groupIdSeed=0, version=3}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6
-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}, CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}, CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}]}
hazelcast-node3    | 2026-01-14 18:52:44,431 [ INFO] [hz.jovial_lewin.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.13:56483->/172.28.0.12:5701, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:52:44,452 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.13:5701->/172.28.0.12:49803, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:52:44,537 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true 
hazelcast-node3    | 2026-01-14 18:52:44,539 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:52:44,647 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true 
hazelcast-node3    | 2026-01-14 18:52:44,648 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:52:44,760 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true 
hazelcast-node3    | 2026-01-14 18:52:44,761 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:52:44,891 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true 
hazelcast-node3    | 2026-01-14 18:52:44,903 [ INFO] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 18:52:44,904 [ WARN] [hz.jovial_lewin.cached.thread-3] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.12]:5701 Cause => java.io.IOException {Connection refused to address /172.28.0.12:5701}, Error-Count: 5
hazelcast-node3    | 2026-01-14 18:52:44,906 [ WARN] [hz.jovial_lewin.cached.thread-1] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Member [172.28.0.12]:5701 - 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee is suspected to be dead for reason: No connection
hazelcast-node3    | 2026-01-14 18:52:44,947 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node3    | 2026-01-14 18:52:44,983 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:2, ver:4} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - 5d4caf68-b764-4d9b-8b78-f7430f87b80f
hazelcast-node3    |    Member [172.28.0.13]:5701 - 75cf96b8-42b6-4ded-aee2-4225a06c3f86 this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:45,006 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.t.TransactionManagerService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.12]:5701, UUID: 5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
hazelcast-node3    | 2026-01-14 18:52:45,024 [ WARN] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node3    | 2026-01-14 18:52:45,253 [ WARN] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leader RaftEndpoint{uuid='5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee'} is not reachable. Will start new election round...
hazelcast-node3    | 2026-01-14 18:52:45,260 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:45,344 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 2, last log index: 4, last log term: 1
hazelcast-node3    | 2026-01-14 18:52:45,346 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node1    | 2026-01-14 18:58:54,012 [ INFO] [hz.compassionate_agnesi.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=13, /172.28.
0.11:5701->/172.28.0.2:41644, qualifier=null, endpoint=[172.28.0.2]:41644, remoteUuid=989aad82-3ed9-4649-b099-d18fc8ddf04d, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=989aad82-3ed9-4649-b099-d18fc8ddf04d, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417133982, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 18:58:57,149 [ INFO] [hz.compassionate_agnesi.generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=14,
 /172.28.0.11:5701->/172.28.0.2:41654, qualifier=null, endpoint=[172.28.0.2]:41654, remoteUuid=5abb13ac-2a0c-44a9-a38b-977043d63ed3, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 5abb13ac-2a0c-44a9-a38b-977043d63ed3, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 18:58:57,188 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=14, /172.28.0.11:5701->/172.28.0.2:41654, qualifier=null, endpoint=[172.28.0.2]:41654, remoteUuid=5abb13ac-2a0c-44a9-a38b-977043d63ed3, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 18:58:57,190 [ INFO] [hz.compassionate_agnesi.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=14, /172.28.
0.11:5701->/172.28.0.2:41654, qualifier=null, endpoint=[172.28.0.2]:41654, remoteUuid=5abb13ac-2a0c-44a9-a38b-977043d63ed3, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=5abb13ac-2a0c-44a9-a38b-977043d63ed3, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417137148, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 19:00:46,145 [ INFO] [hz.compassionate_agnesi.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=5, /172.28.0.11:5701->/172.28.0.3:43868, qualifier=null, endpoint=[172.28.0.3]:43868, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 19:00:46,146 [ INFO] [hz.compassionate_agnesi.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=5, /172.28.0
.11:5701->/172.28.0.3:43868, qualifier=null, endpoint=[172.28.0.3]:43868, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416760048, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 19:02:25,292 [ INFO] [hz.compassionate_agnesi.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=3, /172.28.0.11:5701->/172.28.0.13:33817, qualifier=null, endpoint=[172.28.0.13]:5701, remoteUuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 19:02:25,314 [ INFO] [hz.compassionate_agnesi.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=1, /172.28.0.11:57505->/172.28.0.13:5701, qualifier=null, endpoint=[172.28.0.13]:5701, remoteUuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 19:02:25,323 [ INFO] [hz.compassionate_agnesi.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.13:5701, timeout: 10000, bind-any: true
hazelcast-node1    | 2026-01-14 19:02:25,333 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Running shutdown hook... Current node state: ACTIVE
hazelcast-node1    | 2026-01-14 19:02:25,344 [ INFO] [hz.compassionate_agnesi.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.13:5701. Reason: IOException[Connection refused to address /172.28.0.13:5701]
hazelcast-node1    | 2026-01-14 19:02:25,368 [ INFO] [hz.ShutdownThread] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is SHUTTING_DOWN
hazelcast-node1    | 2026-01-14 19:02:25,394 [ WARN] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Terminating forcefully...
hazelcast-node1    | 2026-01-14 19:02:25,398 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Shutting down connection manager...
hazelcast-node1    | 2026-01-14 19:02:25,429 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Shutting down node engine...
hazelcast-node1    | 2026-01-14 19:02:25,582 [ INFO] [hz.ShutdownThread] [c.h.i.i.NodeExtension]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying node NodeExtension.
hazelcast-node1    | 2026-01-14 19:02:25,605 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Hazelcast Shutdown is completed in 190 ms.
hazelcast-node1    | ########################################
hazelcast-node1    | # JAVA=/usr/bin/java
hazelcast-node1    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node1    | ########################################
hazelcast-node1    | 2026-01-14 19:02:50,625 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node1    | 2026-01-14 19:02:50,672 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node1    | 2026-01-14 19:02:56,857 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node1    | 2026-01-14 19:02:57,694 [ INFO] [main] [c.h.s.logo]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node1    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node1    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node1    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node1    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node1    | 2026-01-14 19:02:57,716 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node1    | 2026-01-14 19:02:57,909 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.11]:5701
hazelcast-node1    | 2026-01-14 19:02:57,927 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node1    | 2026-01-14 19:02:57,955 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node1    | 2026-01-14 19:02:57,964 [ INFO] [main] [c.h.system]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node1    | To enable the Jet engine on the members, do one of the following:
hazelcast-node1    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node1    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node1    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node1    | 2026-01-14 19:03:05,281 [ INFO] [main] [c.h.s.security]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node1    | 2026-01-14 19:03:05,947 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node1    | 2026-01-14 19:03:05,972 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node1    | 2026-01-14 19:03:07,281 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node1    | 2026-01-14 19:03:07,313 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTING
hazelcast-node1    | 2026-01-14 19:03:07,703 [ INFO] [hz.silly_lamport.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.13:58445
hazelcast-node1    | 2026-01-14 19:03:07,728 [ INFO] [hz.silly_lamport.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:34857 and /172.28.0.12:5701
hazelcast-node1    | 2026-01-14 19:03:07,764 [ INFO] [hz.silly_lamport.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:41225 and /172.28.0.13:5701
hazelcast-node1    | 2026-01-14 19:03:07,817 [ INFO] [hz.silly_lamport.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.11:5701 and /172.28.0.12:34429
hazelcast-node1    | 2026-01-14 19:03:12,558 [ INFO] [main] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:1, ver:1} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 40b6edb8-2f50-414d-aad7-721a1cef042d this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:12,587 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] [172.28.0.11]:5701 is STARTED
hazelcast-node1    | 2026-01-14 19:03:12,913 [ INFO] [hz.silly_lamport.generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:2, ver:2} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 40b6edb8-2f50-414d-aad7-721a1cef042d this
hazelcast-node1    |    Member [172.28.0.13]:5701 - 835ef35e-0444-4929-b0a2-58679f9cdc66
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:13,222 [ INFO] [hz.silly_lamport.cached.thread-3] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is waiting for 3 members to join the cluster. Current member count: 2
hazelcast-node1    | 2026-01-14 19:03:13,553 [ INFO] [hz.silly_lamport.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:3, ver:3} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 40b6edb8-2f50-414d-aad7-721a1cef042d this
hazelcast-node1    |    Member [172.28.0.13]:5701 - 835ef35e-0444-4929-b0a2-58679f9cdc66
hazelcast-node1    |    Member [172.28.0.12]:5701 - 923791b6-3d0d-41ce-86d6-26df8c076f0d
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:13,813 [ INFO] [hz.silly_lamport.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=5
, /172.28.0.11:5701->/172.28.0.3:41292, qualifier=null, endpoint=[172.28.0.3]:41292, remoteUuid=a868c835-82ad-4bec-addf-a9efc1153439, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: a868c835-82ad-4bec-addf-a9efc1153439, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 19:03:14,247 [ INFO] [hz.silly_lamport.priority-generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Initializing cluster partition table arrangement...
hazelcast-node1    | 2026-01-14 19:03:14,323 [ INFO] [hz.silly_lamport.cached.thread-3] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{groupIdSe
ed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node1    | 2026-01-14 19:03:14,608 [ INFO] [hz.silly_lamport.cached.thread-3] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'}, RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, RaftEndpoint{uuid='40b6edb8-2f50-414d-aad7-721a1cef042d'}]
hazelcast-node1    | 2026-01-14 19:03:14,643 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node1    | 2026-01-14 19:03:16,986 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node1    | 2026-01-14 19:03:17,145 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Moving to new term: 1 from current term: 0 after VoteRequest{candidate=RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node1    | 2026-01-14 19:03:17,154 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:17,155 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node1    | 2026-01-14 19:03:17,377 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}
hazelcast-node1    | 2026-01-14 19:03:17,378 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701} - LEADER
hazelcast-node1    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:18,269 [ INFO] [hz.silly_lamport.cached.thread-3] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]
hazelcast-node1    | 2026-01-14 19:03:18,455 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=0}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f5
0-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=2}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node1    | 2026-01-14 19:03:18,470 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=2}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f5
0-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=3}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node1    | 2026-01-14 19:03:18,471 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.RaftInvocationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVers
ion{groupIdSeed=0, version=3}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f5
0-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node1    | 2026-01-14 19:03:23,484 [ INFO] [hz.silly_lamport.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=3, /172.28.0.11:5701->/172.28.0.12:34429, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 19:03:23,502 [ INFO] [hz.silly_lamport.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=4, /172.28.0.11:34857->/172.28.0.12:5701, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 19:03:23,523 [ INFO] [hz.silly_lamport.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node1    | 2026-01-14 19:03:23,540 [ INFO] [hz.silly_lamport.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node1    | 2026-01-14 19:03:23,544 [ INFO] [hz.silly_lamport.cached.thread-2] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node1    | 2026-01-14 19:03:23,545 [ INFO] [hz.silly_lamport.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node1    | 2026-01-14 19:03:23,654 [ INFO] [hz.silly_lamport.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node1    | 2026-01-14 19:03:23,656 [ INFO] [hz.silly_lamport.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node1    | 2026-01-14 19:03:23,761 [ INFO] [hz.silly_lamport.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node1    | 2026-01-14 19:03:30,102 [ INFO] [hz.silly_lamport.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=6
, /172.28.0.11:5701->/172.28.0.2:55242, qualifier=null, endpoint=[172.28.0.2]:55242, remoteUuid=a6737b78-f109-41b4-a960-6a14f5e10bb1, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: a6737b78-f109-41b4-a960-6a14f5e10bb1, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 19:03:33,264 [ INFO] [hz.silly_lamport.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=6, /172.28.0.11:5701->/172.28.0.2:55242, qualifier=null, endpoint=[172.28.0.2]:55242, remoteUuid=a6737b78-f109-41b4-a960-6a14f5e10bb1, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 19:03:33,357 [ INFO] [hz.silly_lamport.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=6, /172.28.0.11:570
1->/172.28.0.2:55242, qualifier=null, endpoint=[172.28.0.2]:55242, remoteUuid=a6737b78-f109-41b4-a960-6a14f5e10bb1, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=a6737b78-f109-41b4-a960-6a14f5e10bb1, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417410101, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 19:03:33,769 [ INFO] [hz.silly_lamport.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connect timed out to address /172.28.0.12:5701]
hazelcast-node1    | 2026-01-14 19:03:45,144 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'}, nextTerm=2, lastLogTerm=1, lastLogIndex=4}
hazelcast-node1    | 2026-01-14 19:03:45,151 [ WARN] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Current leader RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}'s heartbeats are timed-out. Will start new election round...
hazelcast-node1    | 2026-01-14 19:03:45,152 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:45,162 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 2, last log index: 4, last log term: 1
hazelcast-node1    | 2026-01-14 19:03:45,163 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:45,166 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Moving to new term: 2 from current term: 1 after VoteRequest{candidate=RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'}, term=2, lastLogTerm=1, lastLogIndex=4, disruptive=false}
hazelcast-node1    | 2026-01-14 19:03:45,166 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:2, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:45,166 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'}, term=2, lastLogTerm=1, lastLogIndex=4, disruptive=false}
hazelcast-node1    | 2026-01-14 19:03:45,172 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'}
hazelcast-node1    | 2026-01-14 19:03:45,173 [ INFO] [hz.silly_lamport.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: METADATA(0), size:3, term:2, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} - LEADER
hazelcast-node1    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node1    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:47,360 [ INFO] [hz.silly_lamport.generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=7, /172.28
.0.11:5701->/172.28.0.2:59928, qualifier=null, endpoint=[172.28.0.2]:59928, remoteUuid=3afcfaf4-08a2-4f92-978b-bc48cfac697d, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 3afcfaf4-08a2-4f92-978b-bc48cfac697d, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 19:03:50,541 [ INFO] [hz.silly_lamport.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=7, /172.28.0.11:5701->/172.28.0.2:59928, qualifier=null, endpoint=[172.28.0.2]:59928, remoteUuid=3afcfaf4-08a2-4f92-978b-bc48cfac697d, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 19:03:50,542 [ INFO] [hz.silly_lamport.event-1] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=7, /172.28.0.11:570
1->/172.28.0.2:59928, qualifier=null, endpoint=[172.28.0.2]:59928, remoteUuid=3afcfaf4-08a2-4f92-978b-bc48cfac697d, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=3afcfaf4-08a2-4f92-978b-bc48cfac697d, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417427359, latest clientAttributes=null, labels=[]}
hazelcast-node1    | 2026-01-14 19:03:54,121 [ INFO] [hz.silly_lamport.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node1    | 2026-01-14 19:03:57,797 [ INFO] [hz.silly_lamport.cached.thread-6] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Host is unreachable to address /172.28.0.12:5701]
hazelcast-node1    | 2026-01-14 19:03:57,798 [ WARN] [hz.silly_lamport.cached.thread-6] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.12]:5701 Cause => java.io.IOException {Host is unreachable to address /172.28.0.12:5701}, Error-Count: 5
hazelcast-node3    | 2026-01-14 18:52:45,378 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, nextTerm=2, lastLogTerm=1, lastLogIndex=4}
hazelcast-node3    | 2026-01-14 18:52:45,502 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'} for term: 2, number of votes: 2, majority: 2
hazelcast-node3    | 2026-01-14 18:52:45,518 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node3    | 2026-01-14 18:52:45,521 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Leader election started for term: 2, last log index: 4, last log term: 1
hazelcast-node3    | 2026-01-14 18:52:45,522 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:2, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - CANDIDATE this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:45,574 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Duplicate VoteRequest{candidate=RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'}, term=2, lastLogTerm=1, lastLogIndex=4, disruptive=false}. currently voted-for: RaftEndpoint{uuid='75cf96b8-42b6-4ded-aee2-4225a06c3f86'}
hazelcast-node3    | 2026-01-14 18:52:47,553 [ WARN] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTimeoutTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Leader election for term: 2 has timed out!
hazelcast-node3    | 2026-01-14 18:52:47,554 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Leader election started for term: 3, last log index: 4, last log term: 1
hazelcast-node3    | 2026-01-14 18:52:47,555 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:3, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - CANDIDATE this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:52:47,639 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='5d4caf68-b764-4d9b-8b78-f7430f87b80f'} for term: 3, number of votes: 2, majority: 2
hazelcast-node3    | 2026-01-14 18:52:47,646 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] We are the LEADER!
hazelcast-node3    | 2026-01-14 18:52:47,651 [ INFO] [hz.jovial_lewin.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:3, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701}
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} - LEADER this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 18:53:44,494 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:53:44,497 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:53:44,509 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:53:44,510 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:53:44,512 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 18:53:44,513 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:53:44,518 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:53:44,518 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node1    | 2026-01-14 19:03:57,799 [ INFO] [hz.silly_lamport.cached.thread-6] [c.h.i.c.i.MembershipManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Removing Member [172.28.0.12]:5701 - 923791b6-3d0d-41ce-86d6-26df8c076f0d
hazelcast-node1    | 2026-01-14 19:03:57,802 [ INFO] [hz.silly_lamport.cached.thread-6] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID 923791b6-3d0d-41ce-86d6-26df8c076f0d
hazelcast-node1    | 2026-01-14 19:03:57,805 [ INFO] [hz.silly_lamport.cached.thread-6] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:2, ver:4} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 40b6edb8-2f50-414d-aad7-721a1cef042d this
hazelcast-node1    |    Member [172.28.0.13]:5701 - 835ef35e-0444-4929-b0a2-58679f9cdc66
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 19:03:57,827 [ INFO] [hz.silly_lamport.cached.thread-2] [c.h.t.TransactionManagerService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.12]:5701, UUID: 923791b6-3d0d-41ce-86d6-26df8c076f0d
hazelcast-node1    | 2026-01-14 19:03:57,847 [ WARN] [hz.silly_lamport.cached.thread-2] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node1    | 2026-01-14 19:03:58,062 [ INFO] [hz.silly_lamport.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Repartitioning cluster data. Migration tasks count: 180
hazelcast-node1    | 2026-01-14 19:03:59,426 [ INFO] [hz.silly_lamport.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] All migration tasks have been completed. (repartitionTime=Wed Jan 14 19:03:58 GMT 2026, plannedMigrations=180, completedMigrations=180, remainingMigrations=0, totalCompletedMigrations=180)
hazelcast-node1    | 2026-01-14 19:06:31,426 [ INFO] [hz.silly_lamport.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=8
, /172.28.0.11:5701->/172.28.0.2:43188, qualifier=null, endpoint=[172.28.0.2]:43188, remoteUuid=bf3a6e42-3392-4564-92e3-42ca7f0779b3, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: bf3a6e42-3392-4564-92e3-42ca7f0779b3, client name: hz.client_0, client version: 5.4.0
hazelcast-node1    | 2026-01-14 19:06:31,451 [ INFO] [hz.silly_lamport.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=8, /172.28.0.11:5701->/172.28.0.2:43188, qualifier=null, endpoint=[172.28.0.2]:43188, remoteUuid=bf3a6e42-3392-4564-92e3-42ca7f0779b3, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 19:06:31,452 [ INFO] [hz.silly_lamport.event-1] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=8, /172.28.0.11:570
1->/172.28.0.2:43188, qualifier=null, endpoint=[172.28.0.2]:43188, remoteUuid=bf3a6e42-3392-4564-92e3-42ca7f0779b3, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=bf3a6e42-3392-4564-92e3-42ca7f0779b3, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417591425, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:53:44,519 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 18:54:45,735 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:54:45,736 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:54:45,738 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:54:45,739 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:54:45,739 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 18:54:45,739 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:54:45,741 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:54:45,742 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:54:45,742 [ INFO] [hz.jovial_lewin.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 18:55:46,989 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:55:46,990 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:55:46,997 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:55:47,000 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:55:47,000 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 18:55:47,001 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:55:47,003 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:55:47,004 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:55:47,004 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 18:56:01,148 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=6,
 /172.28.0.13:5701->/172.28.0.2:40174, qualifier=null, endpoint=[172.28.0.2]:40174, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: ee8e5ceb-efd1-46e3-8da4-307725c6be3d, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:56:01,192 [ INFO] [hz.jovial_lewin.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=6, /172.28.0.13:5701->/172.28.0.2:40174, qualifier=null, endpoint=[172.28.0.2]:40174, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:56:01,264 [ INFO] [hz.jovial_lewin.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=6, /172.28.0.13:5701
->/172.28.0.2:40174, qualifier=null, endpoint=[172.28.0.2]:40174, remoteUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=ee8e5ceb-efd1-46e3-8da4-307725c6be3d, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416961147, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:56:21,116 [ INFO] [hz.jovial_lewin.generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=7, /172.28.
0.13:5701->/172.28.0.2:52902, qualifier=null, endpoint=[172.28.0.2]:52902, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: d4864eff-b7b5-4cf1-981d-90546a3dbad0, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:56:21,138 [ INFO] [hz.jovial_lewin.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=7, /172.28.0.13:5701->/172.28.0.2:52902, qualifier=null, endpoint=[172.28.0.2]:52902, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:56:21,144 [ INFO] [hz.jovial_lewin.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=7, /172.28.0.13:5701
->/172.28.0.2:52902, qualifier=null, endpoint=[172.28.0.2]:52902, remoteUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=d4864eff-b7b5-4cf1-981d-90546a3dbad0, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416981113, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:56:34,058 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=8, /172.28.
0.13:5701->/172.28.0.2:57292, qualifier=null, endpoint=[172.28.0.2]:57292, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:56:34,098 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=8, /172.28.0.13:5701->/172.28.0.2:57292, qualifier=null, endpoint=[172.28.0.2]:57292, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:56:34,107 [ INFO] [hz.jovial_lewin.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=8, /172.28.0.13:5701
->/172.28.0.2:57292, qualifier=null, endpoint=[172.28.0.2]:57292, remoteUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=5f55430e-b10b-4c3b-8050-f2b6f9ea4d7e, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416994057, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:56:48,250 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:56:48,251 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:56:48,254 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:56:48,254 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:56:48,255 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 18:56:48,255 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:56:48,266 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:56:48,266 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:56:48,267 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 18:57:34,888 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=9,
 /172.28.0.13:5701->/172.28.0.2:43992, qualifier=null, endpoint=[172.28.0.2]:43992, remoteUuid=32b471d2-4047-40d7-9164-9ad7a8fa5141, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 32b471d2-4047-40d7-9164-9ad7a8fa5141, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:57:34,922 [ INFO] [hz.jovial_lewin.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=9, /172.28.0.13:5701->/172.28.0.2:43992, qualifier=null, endpoint=[172.28.0.2]:43992, remoteUuid=32b471d2-4047-40d7-9164-9ad7a8fa5141, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:57:34,927 [ INFO] [hz.jovial_lewin.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=9, /172.28.0.13:5701
->/172.28.0.2:43992, qualifier=null, endpoint=[172.28.0.2]:43992, remoteUuid=32b471d2-4047-40d7-9164-9ad7a8fa5141, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=32b471d2-4047-40d7-9164-9ad7a8fa5141, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417054887, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:57:48,596 [ INFO] [hz.jovial_lewin.generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=10, /172.28
.0.13:5701->/172.28.0.2:46678, qualifier=null, endpoint=[172.28.0.2]:46678, remoteUuid=7bcf6006-d2a0-49a5-976b-ca8f0f35e466, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 7bcf6006-d2a0-49a5-976b-ca8f0f35e466, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:57:48,632 [ INFO] [hz.jovial_lewin.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=10, /172.28.0.13:5701->/172.28.0.2:46678, qualifier=null, endpoint=[172.28.0.2]:46678, remoteUuid=7bcf6006-d2a0-49a5-976b-ca8f0f35e466, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:57:48,635 [ INFO] [hz.jovial_lewin.event-1] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=10, /172.28.0.13:570
1->/172.28.0.2:46678, qualifier=null, endpoint=[172.28.0.2]:46678, remoteUuid=7bcf6006-d2a0-49a5-976b-ca8f0f35e466, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=7bcf6006-d2a0-49a5-976b-ca8f0f35e466, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417068595, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:57:48,874 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:57:48,875 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:57:48,883 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:57:48,884 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:57:48,884 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 18:57:48,884 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:57:48,885 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:57:48,886 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:57:48,886 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 18:58:40,014 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=11
, /172.28.0.13:5701->/172.28.0.2:44616, qualifier=null, endpoint=[172.28.0.2]:44616, remoteUuid=33a3b671-b112-4b04-bf1f-a84860d6f393, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 33a3b671-b112-4b04-bf1f-a84860d6f393, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:58:40,050 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=11, /172.28.0.13:5701->/172.28.0.2:44616, qualifier=null, endpoint=[172.28.0.2]:44616, remoteUuid=33a3b671-b112-4b04-bf1f-a84860d6f393, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:58:40,051 [ INFO] [hz.jovial_lewin.event-3] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=11, /172.28.0.13:570
1->/172.28.0.2:44616, qualifier=null, endpoint=[172.28.0.2]:44616, remoteUuid=33a3b671-b112-4b04-bf1f-a84860d6f393, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=33a3b671-b112-4b04-bf1f-a84860d6f393, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417120013, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:58:50,058 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=12
, /172.28.0.13:5701->/172.28.0.2:44482, qualifier=null, endpoint=[172.28.0.2]:44482, remoteUuid=45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:58:50,124 [ INFO] [hz.jovial_lewin.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=12, /172.28.0.13:5701->/172.28.0.2:44482, qualifier=null, endpoint=[172.28.0.2]:44482, remoteUuid=45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:58:50,133 [ INFO] [hz.jovial_lewin.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=12, /172.28.0.13:570
1->/172.28.0.2:44482, qualifier=null, endpoint=[172.28.0.2]:44482, remoteUuid=45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=45ec8a79-dcbb-46ed-bb5a-efc35ac7aab2, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417130058, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:58:50,145 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:58:50,145 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:58:50,148 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:58:50,148 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:58:50,149 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 18:58:50,160 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:58:50,163 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:58:50,164 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:58:50,166 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 18:58:53,975 [ INFO] [hz.jovial_lewin.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=13
, /172.28.0.13:5701->/172.28.0.2:51842, qualifier=null, endpoint=[172.28.0.2]:51842, remoteUuid=989aad82-3ed9-4649-b099-d18fc8ddf04d, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 989aad82-3ed9-4649-b099-d18fc8ddf04d, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:58:54,011 [ INFO] [hz.jovial_lewin.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=13, /172.28.0.13:5701->/172.28.0.2:51842, qualifier=null, endpoint=[172.28.0.2]:51842, remoteUuid=989aad82-3ed9-4649-b099-d18fc8ddf04d, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:58:54,015 [ INFO] [hz.jovial_lewin.event-2] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=13, /172.28.0.13:570
1->/172.28.0.2:51842, qualifier=null, endpoint=[172.28.0.2]:51842, remoteUuid=989aad82-3ed9-4649-b099-d18fc8ddf04d, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=989aad82-3ed9-4649-b099-d18fc8ddf04d, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417133973, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:58:57,137 [ INFO] [hz.jovial_lewin.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=14, /172.28
.0.13:5701->/172.28.0.2:51844, qualifier=null, endpoint=[172.28.0.2]:51844, remoteUuid=5abb13ac-2a0c-44a9-a38b-977043d63ed3, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 5abb13ac-2a0c-44a9-a38b-977043d63ed3, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 18:58:57,193 [ INFO] [hz.jovial_lewin.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=14, /172.28.0.13:5701->/172.28.0.2:51844, qualifier=null, endpoint=[172.28.0.2]:51844, remoteUuid=5abb13ac-2a0c-44a9-a38b-977043d63ed3, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 18:58:57,194 [ INFO] [hz.jovial_lewin.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=14, /172.28.0.13:570
1->/172.28.0.2:51844, qualifier=null, endpoint=[172.28.0.2]:51844, remoteUuid=5abb13ac-2a0c-44a9-a38b-977043d63ed3, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=5abb13ac-2a0c-44a9-a38b-977043d63ed3, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417137136, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 18:59:07,485 [ INFO] [hz.jovial_lewin.HealthMonitor] [c.h.i.d.HealthMonitor]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The HealthMonitor has detected a high load on the system. For more detailed information,
hazelcast-node3    | enable Diagnostics by adding the property -Dhazelcast.diagnostics.enabled=true
hazelcast-node3    | 2026-01-14 18:59:07,503 [ INFO] [hz.jovial_lewin.HealthMonitor] [c.h.i.d.HealthMonitor]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] processors=4, physical.memory.total=3.8G, physical.memory.free=1.2G, swap
.space.total=1024.0M, swap.space.free=1017.5M, heap.memory.used=65.4M, heap.memory.free=54.1M, heap.memory.total=120.0M, heap.memory.max=3.0G, heap.memory.used/total=54.51%, heap.memory.used/max=2.11%, minor.gc.count=14, minor.g
c.time=659ms, major.gc.count=0, major.gc.time=0ms, unknown.gc.count=10, unknown.gc.time=152ms, load.process=57.14%, load.system=79.17%, load.systemAverage=2.23, thread.count=48, thread.peakCount=55, cluster.timeDiff=-1, event.q.
size=0, executor.q.async.size=0, executor.q.client.size=0, executor.q.client.query.size=0, executor.q.client.blocking.size=0, executor.q.query.size=0, executor.q.scheduled.size=0, executor.q.io.size=0, executor.q.system.size=0, 
executor.q.operations.size=0, executor.q.priorityOperation.size=0, operations.completed.count=82796, executor.q.mapLoad.size=0, executor.q.mapLoadAllKeys.size=0, executor.q.cluster.size=0, executor.q.response.size=0, operations.running.count=0, operations.pending.invocations.percentage=0.00%, operations.pending.invocations.count=0, proxy.count=3, clientEndpoint.count=1, connection.active.count=3, client.connection.count=1, connection.count=2
hazelcast-node3    | 2026-01-14 18:59:51,405 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:59:51,405 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:59:51,408 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:59:51,409 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:59:51,412 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 18:59:51,412 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 18:59:51,417 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 18:59:51,417 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 18:59:51,417 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 19:00:46,145 [ INFO] [hz.jovial_lewin.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=5, /172.28.0.13:5701->/172.28.0.3:38150, qualifier=null, endpoint=[172.28.0.3]:38150, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 19:00:46,146 [ INFO] [hz.jovial_lewin.event-3] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=5, /172.28.0.13:5701
->/172.28.0.3:38150, qualifier=null, endpoint=[172.28.0.3]:38150, remoteUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=bac00adb-5981-4f88-82a1-65cd53999c6f, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768416760617, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 19:00:52,679 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:00:52,680 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:00:52,681 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:00:52,681 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:00:52,681 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 19:00:52,682 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 19:00:52,683 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:00:52,683 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:00:52,684 [ INFO] [hz.jovial_lewin.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 19:01:53,991 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:01:53,992 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:01:53,994 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:01:53,994 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:01:53,995 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 19:01:53,995 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 19:01:53,996 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=5243be2e-7de4-4b5e-b5fe-9b3d9a2f61ee
, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:01:53,996 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=75cf96b8-42b6-4ded-aee2-4225a06c3f86, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:01:53,997 [ INFO] [hz.jovial_lewin.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 19:02:25,209 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Running shutdown hook... Current node state: ACTIVE
hazelcast-node3    | 2026-01-14 19:02:25,212 [ INFO] [hz.ShutdownThread] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is SHUTTING_DOWN
hazelcast-node3    | 2026-01-14 19:02:25,215 [ WARN] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Terminating forcefully...
hazelcast-node3    | 2026-01-14 19:02:25,216 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Shutting down connection manager...
hazelcast-node3    | 2026-01-14 19:02:25,222 [ INFO] [hz.ShutdownThread] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=1, /172.28.0.13:33817->/172.28.0.11:5701, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: TcpServer is stopping
hazelcast-node3    | 2026-01-14 19:02:25,223 [ INFO] [hz.ShutdownThread] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=3, /172.28.0.13:5701->/172.28.0.11:57505, qualifier=null, endpoint=[172.28.0.11]:5701, remoteUuid=5d4caf68-b764-4d9b-8b78-f7430f87b80f, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: TcpServer is stopping
hazelcast-node3    | 2026-01-14 19:02:25,229 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Shutting down node engine...
hazelcast-node3    | 2026-01-14 19:02:25,327 [ INFO] [hz.ShutdownThread] [c.h.i.i.NodeExtension]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying node NodeExtension.
hazelcast-node3    | 2026-01-14 19:02:25,334 [ INFO] [hz.ShutdownThread] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Hazelcast Shutdown is completed in 113 ms.
hazelcast-node3    | ########################################
hazelcast-node3    | # JAVA=/usr/bin/java
hazelcast-node3    | # JAVA_OPTS=--add-modules java.se --add-exports java.base/jdk.internal.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.management/sun
.management=ALL-UNNAMED --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED -Dlog4j.shutdownHookEnabled=false -Dhazelcast.logging.shutdown=true -Dhazelcast.logging.type=log4j2 -Dlog4j.configurationFile=file:/opt/h
azelcast/config/log4j2.properties -Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml -Djet.custom.lib.dir=/opt/hazelcast/custom-lib -Djava.net.preferIPv4Stack=true -XX:MaxRAMPercentage=80.0 -Dhazelcast.config=/opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | # CLASSPATH=/opt/hazelcast/*:/opt/hazelcast/lib:/opt/hazelcast/lib/*:/opt/hazelcast/bin/user-lib:/opt/hazelcast/bin/user-lib/*
hazelcast-node3    | ########################################
hazelcast-node3    | 2026-01-14 19:02:50,777 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Loading configuration '/opt/hazelcast/config/hazelcast.yaml' from System property 'hazelcast.config'
hazelcast-node3    | 2026-01-14 19:02:50,824 [ INFO] [main] [c.h.i.c.AbstractConfigLocator]: Using configuration file at /opt/hazelcast/config/hazelcast.yaml
hazelcast-node3    | 2026-01-14 19:02:57,345 [ INFO] [main] [c.h.i.AddressPicker]: [LOCAL] [counter-cluster] [5.4.0] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.28.0.13, 172.28.0.11, 172.28.0.12]
hazelcast-node3    | 2026-01-14 19:02:57,802 [ INFO] [main] [c.h.s.logo]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |    o    o     o     o---o   o--o o      o---o     o     o----o o--o--o
hazelcast-node3    |    |    |    / \       /         |     /         / \    |         |
hazelcast-node3    |    o----o       o     o   o----o |    o             o   o----o    |
hazelcast-node3    |    |    |  *     \   /           |     \       *     \       |    |
hazelcast-node3    |    o    o *       o o---o   o--o o----o o---o *       o o----o    o
hazelcast-node3    | 2026-01-14 19:02:57,803 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.
hazelcast-node3    | 2026-01-14 19:02:57,890 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Hazelcast Platform 5.4.0 (20240415) starting at [172.28.0.13]:5701
hazelcast-node3    | 2026-01-14 19:02:57,890 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Cluster name: counter-cluster
hazelcast-node3    | 2026-01-14 19:02:57,891 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Integrity Checker is disabled. Fail-fast on corrupted executables will not be performed. For more information, see the documentation for Integrity Checker.
hazelcast-node3    | 2026-01-14 19:02:57,926 [ INFO] [main] [c.h.system]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The Jet engine is disabled.
hazelcast-node3    | To enable the Jet engine on the members, do one of the following:
hazelcast-node3    |   - Change member config using Java API: config.getJetConfig().setEnabled(true)
hazelcast-node3    |   - Change XML/YAML configuration property: Set hazelcast.jet.enabled to true
hazelcast-node3    |   - Add system property: -Dhz.jet.enabled=true (for Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    |   - Add environment variable: HZ_JET_ENABLED=true (recommended when running container image. For Hazelcast embedded, works only when loading config via Config.load)
hazelcast-node3    | 2026-01-14 19:03:04,437 [ INFO] [main] [c.h.s.security]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Enable DEBUG/FINE log level for log category com.hazelcast.system.security  or use -Dhazelcast.security.recommendations system property to see 🔒 security recommendations and the status of current config.
hazelcast-node3    | 2026-01-14 19:03:04,785 [ INFO] [main] [c.h.i.i.Node]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Using TCP/IP discovery
hazelcast-node3    | 2026-01-14 19:03:04,800 [ INFO] [main] [c.h.c.CPSubsystem]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is enabled with 3 members.
hazelcast-node3    | 2026-01-14 19:03:06,416 [ INFO] [main] [c.h.i.d.Diagnostics]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Diagnostics disabled. To enable add -Dhazelcast.diagnostics.enabled=true to the JVM arguments.      
hazelcast-node3    | 2026-01-14 19:03:06,447 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTING
hazelcast-node3    | 2026-01-14 19:03:07,613 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:48297 and /172.28.0.12:5701
hazelcast-node3    | 2026-01-14 19:03:07,621 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.12:43479
hazelcast-node3    | 2026-01-14 19:03:07,748 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:5701 and /172.28.0.11:41225
hazelcast-node3    | 2026-01-14 19:03:07,801 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Initialized new cluster connection between /172.28.0.13:58445 and /172.28.0.11:5701
hazelcast-node3    | 2026-01-14 19:03:12,962 [ INFO] [hz.unruffled_mirzakhani.generic-operation.thread-1] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:2, ver:2} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - 40b6edb8-2f50-414d-aad7-721a1cef042d
hazelcast-node3    |    Member [172.28.0.13]:5701 - 835ef35e-0444-4929-b0a2-58679f9cdc66 this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:12,973 [ INFO] [hz.unruffled_mirzakhani.generic-operation.thread-0] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node3    | 2026-01-14 19:03:12,973 [ INFO] [hz.unruffled_mirzakhani.generic-operation.thread-0] [c.h.i.c.i.ClusterJoinManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] The address ([172.28.0.11]:5701) will be added as a temporary member address to the TCP-IP joiner configuration.
hazelcast-node3    | 2026-01-14 19:03:13,029 [ INFO] [main] [c.h.c.LifecycleService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] [172.28.0.13]:5701 is STARTED
hazelcast-node3    | 2026-01-14 19:03:13,284 [ INFO] [hz.unruffled_mirzakhani.cached.thread-2] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is waiting for 3 members to join the cluster. Current member count: 2
hazelcast-node3    | 2026-01-14 19:03:13,575 [ INFO] [hz.unruffled_mirzakhani.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:3, ver:3} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - 40b6edb8-2f50-414d-aad7-721a1cef042d
hazelcast-node3    |    Member [172.28.0.13]:5701 - 835ef35e-0444-4929-b0a2-58679f9cdc66 this
hazelcast-node3    |    Member [172.28.0.12]:5701 - 923791b6-3d0d-41ce-86d6-26df8c076f0d
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:13,738 [ INFO] [hz.unruffled_mirzakhani.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=5, /172.28.0.13:5701->/172.28.0.3:49776, qualifier=null, endpoint=[172.28.0.3]:49776, remoteUuid=a868c835-82ad-4bec-addf-a9efc1153439, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: a868c835-82ad-4bec-addf-a9efc1153439, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 19:03:14,405 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMembersVersion{gr
oupIdSeed=0, version=-1}, members=[]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node3    | 2026-01-14 19:03:14,594 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] RaftNode[CPGroupId{name='METADATA', seed=0, groupId=0}] is created with [RaftEndpoint{uuid='835ef35e-0444-4929-b0a2-58679f9cdc66'}, RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, RaftEndpoint{uuid='40b6edb8-2f50-414d-aad7-721a1cef042d'}]
hazelcast-node3    | 2026-01-14 19:03:15,019 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Status is set to: ACTIVE
hazelcast-node3    | 2026-01-14 19:03:16,993 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, nextTerm=1, lastLogTerm=0, lastLogIndex=0}
hazelcast-node3    | 2026-01-14 19:03:17,099 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Moving to new term: 1 from current term: 0 after VoteRequest{candidate=RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 19:03:17,099 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:17,127 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted vote for VoteRequest{candidate=RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}, term=1, lastLogTerm=0, lastLogIndex=0, disruptive=false}
hazelcast-node3    | 2026-01-14 19:03:17,453 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.AppendRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Setting leader: RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}
hazelcast-node3    | 2026-01-14 19:03:17,469 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701} - LEADER
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:18,201 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.MetadataRaftGroupManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CP Subsystem is initialized with: [CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]   
hazelcast-node3    | 2026-01-14 19:03:18,211 [ INFO] [hz.unruffled_mirzakhani.generic-operation.thread-1] [c.h.c.i.RaftInvocationManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Replaced CPMembersContainer{version=CPMember
sVersion{groupIdSeed=0, version=0}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb
8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]} with CPMembersContainer{version=CPMembersVersion{groupIdSeed=0, version=4}, members=[CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}, CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}, CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}]}
hazelcast-node3    | 2026-01-14 19:03:23,484 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=3, /172.28.0.13:5701->/172.28.0.12:43479, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 19:03:23,490 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=1, /172.28.0.13:48297->/172.28.0.12:5701, qualifier=null, endpoint=[172.28.0.12]:5701, remoteUuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 19:03:23,526 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 19:03:23,539 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 19:03:23,641 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 19:03:23,642 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connection refused to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 19:03:23,744 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 19:03:30,086 [ INFO] [hz.unruffled_mirzakhani.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=6, /172.28.0.13:5701->/172.28.0.2:48950, qualifier=null, endpoint=[172.28.0.2]:48950, remoteUuid=a6737b78-f109-41b4-a960-6a14f5e10bb1, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: a6737b78-f109-41b4-a960-6a14f5e10bb1, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 19:03:33,266 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=6, /172.28.0.13:5701->/172.28.0.2:48950, qualifier=null, endpoint=[172.28.0.2]:48950, remoteUuid=a6737b78-f109-41b4-a960-6a14f5e10bb1, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 19:03:33,312 [ INFO] [hz.unruffled_mirzakhani.event-4] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=6, /172.28.0
.13:5701->/172.28.0.2:48950, qualifier=null, endpoint=[172.28.0.2]:48950, remoteUuid=a6737b78-f109-41b4-a960-6a14f5e10bb1, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=a6737b78-f109-41b4-a960-6a14f5e10bb1, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417410085, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 19:03:33,753 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connect timed out to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 19:03:33,854 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.12:5701, timeout: 10000, bind-any: true
hazelcast-node3    | 2026-01-14 19:03:43,866 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.i.s.t.TcpServerConnector]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.12:5701. Reason: IOException[Connect timed out to address /172.28.0.12:5701]
hazelcast-node3    | 2026-01-14 19:03:43,873 [ WARN] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.12]:5701 Cause => java.io.IOException {Connect timed out to address /172.28.0.12:5701}, Error-Count: 5
hazelcast-node3    | 2026-01-14 19:03:43,875 [ WARN] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.i.c.i.MembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Member [172.28.0.12]:5701 - 923791b6-3d0d-41ce-86d6-26df8c076f0d is suspected to be dead for reason: No connection
hazelcast-node3    | 2026-01-14 19:03:45,124 [ WARN] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leader RaftEndpoint{uuid='923791b6-3d0d-41ce-86d6-26df8c076f0d'}'s heartbeats are timed-out. Will start new election round...
hazelcast-node3    | 2026-01-14 19:03:45,125 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:45,135 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 2, last log index: 4, last log term: 1
hazelcast-node3    | 2026-01-14 19:03:45,138 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:1, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} - FOLLOWER this
hazelcast-node3    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:45,153 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='40b6edb8-2f50-414d-aad7-721a1cef042d'} for term: 2, number of votes: 2, majority: 2
hazelcast-node3    | 2026-01-14 19:03:45,153 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node3    | 2026-01-14 19:03:45,155 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Leader election started for term: 2, last log index: 4, last log term: 1
hazelcast-node3    | 2026-01-14 19:03:45,156 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:2, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} - CANDIDATE this
hazelcast-node3    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:45,164 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteRequestHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Granted pre-vote for PreVoteRequest{candidate=RaftEndpoint{uuid='40b6edb8-2f50-414d-aad7-721a1cef042d'}, nextTerm=2, lastLogTerm=1, lastLogIndex=4}
hazelcast-node3    | 2026-01-14 19:03:45,168 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='40b6edb8-2f50-414d-aad7-721a1cef042d'} for term: 2, number of votes: 2, majority: 2
hazelcast-node3    | 2026-01-14 19:03:45,169 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] We are the LEADER!      
hazelcast-node3    | 2026-01-14 19:03:45,171 [ INFO] [hz.unruffled_mirzakhani.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(METADATA)]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | CP Group Members {groupId: METADATA(0), size:3, term:2, logIndex:0} [
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} - LEADER this
hazelcast-node3    |    CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701}
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701}
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:47,350 [ INFO] [hz.unruffled_mirzakhani.generic-operation.thread-1] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connection[id=7, 
/172.28.0.13:5701->/172.28.0.2:43064, qualifier=null, endpoint=[172.28.0.2]:43064, remoteUuid=3afcfaf4-08a2-4f92-978b-bc48cfac697d, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: 3afcfaf4-08a2-4f92-978b-bc48cfac697d, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 19:03:50,541 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=7, /172.28.0.13:5701->/172.28.0.2:43064, qualifier=null, endpoint=[172.28.0.2]:43064, remoteUuid=3afcfaf4-08a2-4f92-978b-bc48cfac697d, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 19:03:50,544 [ INFO] [hz.unruffled_mirzakhani.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=7, /172.28.0
.13:5701->/172.28.0.2:43064, qualifier=null, endpoint=[172.28.0.2]:43064, remoteUuid=3afcfaf4-08a2-4f92-978b-bc48cfac697d, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=3afcfaf4-08a2-4f92-978b-bc48cfac697d, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417427349, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 19:03:57,804 [ INFO] [hz.unruffled_mirzakhani.priority-generic-operation.thread-0] [c.h.i.p.i.PartitionStateManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID 923791b6-3d0d-41ce-86d6-26df8c076f0d
hazelcast-node3    | 2026-01-14 19:03:57,815 [ INFO] [hz.unruffled_mirzakhani.priority-generic-operation.thread-0] [c.h.i.c.ClusterService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0]
hazelcast-node3    |
hazelcast-node3    | Members {size:2, ver:4} [
hazelcast-node3    |    Member [172.28.0.11]:5701 - 40b6edb8-2f50-414d-aad7-721a1cef042d
hazelcast-node3    |    Member [172.28.0.13]:5701 - 835ef35e-0444-4929-b0a2-58679f9cdc66 this
hazelcast-node3    | ]
hazelcast-node3    |
hazelcast-node3    | 2026-01-14 19:03:57,819 [ INFO] [hz.unruffled_mirzakhani.cached.thread-7] [c.h.t.TransactionManagerService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.12]:5701, UUID: 923791b6-3d0d-41ce-86d6-26df8c076f0d
hazelcast-node3    | 2026-01-14 19:03:57,835 [ WARN] [hz.unruffled_mirzakhani.cached.thread-7] [c.h.c.i.RaftService]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPMember{uuid=923791b6-3d0d-41ce-86d6-26df8c076f0d, address=[172.28.0.12]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node3    | 2026-01-14 19:04:19,592 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:04:19,594 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:04:19,608 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:04:19,608 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:04:19,610 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 19:04:19,611 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 19:04:19,612 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:04:19,613 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:04:19,614 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 19:05:20,736 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:05:20,738 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:05:20,755 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:05:20,756 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:05:20,758 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 19:05:20,759 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 19:05:20,760 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:05:20,761 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:05:20,762 [ INFO] [hz.unruffled_mirzakhani.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 19:06:20,732 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:06:20,733 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:06:20,736 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:06:20,737 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:06:20,738 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 19:06:20,738 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 19:06:20,740 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:06:20,741 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:06:20,742 [ INFO] [hz.unruffled_mirzakhani.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node3    | 2026-01-14 19:06:31,415 [ INFO] [hz.unruffled_mirzakhani.priority-generic-operation.thread-0] [c.h.c.i.p.t.AuthenticationMessageTask]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Received auth from Connecti
on[id=8, /172.28.0.13:5701->/172.28.0.2:40114, qualifier=null, endpoint=[172.28.0.2]:40114, remoteUuid=bf3a6e42-3392-4564-92e3-42ca7f0779b3, alive=true, connectionType=PYH, planeIndex=-1], successfully authenticated, clientUuid: bf3a6e42-3392-4564-92e3-42ca7f0779b3, client name: hz.client_0, client version: 5.4.0
hazelcast-node3    | 2026-01-14 19:06:31,447 [ INFO] [hz.unruffled_mirzakhani.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Connection[id=8, /172.28.0.13:5701->/172.28.0.2:40114, qualifier=null, endpoint=[172.28.0.2]:40114, remoteUuid=bf3a6e42-3392-4564-92e3-42ca7f0779b3, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node3    | 2026-01-14 19:06:31,451 [ INFO] [hz.unruffled_mirzakhani.event-5] [c.h.c.i.ClientEndpointManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=8, /172.28.0
.13:5701->/172.28.0.2:40114, qualifier=null, endpoint=[172.28.0.2]:40114, remoteUuid=bf3a6e42-3392-4564-92e3-42ca7f0779b3, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=bf3a6e42-3392-4564-92e3-42ca7f0779b3, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768417591414, latest clientAttributes=null, labels=[]}
hazelcast-node3    | 2026-01-14 19:07:20,730 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:07:20,730 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:07:20,733 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:07:20,733 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:07:20,733 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Searching a candidate transfer leadership from CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} with 1 leaderships.
hazelcast-node3    | 2026-01-14 19:07:20,734 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] No candidate could be found to get leadership from CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701}. Skipping to next...
hazelcast-node3    | 2026-01-14 19:07:20,735 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=923791b6-3d0d-41ce-86d6-26df
8c076f0d, address=[172.28.0.12]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.12]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node3    | 2026-01-14 19:07:20,735 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node3    |    CPMember{uuid=40b6edb8-2f50-414d-aad7-721a1cef042d, address=[172.28.0.11]:5701} priority 0 has 0,
hazelcast-node3    |    CPMember{uuid=835ef35e-0444-4929-b0a2-58679f9cdc66, address=[172.28.0.13]:5701} priority 0 has 1, leaderships.
hazelcast-node3    | 2026-01-14 19:07:20,736 [ INFO] [hz.unruffled_mirzakhani.cached.thread-4] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.13]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...


hazelcast-node1    | 2026-01-14 20:08:15,672 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: default(5082), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, address=[172.28.0.13]:5701} - LEADER
hazelcast-node1    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 20:08:27,265 [ INFO] [hz.upbeat_jang.HealthMonitor] [c.h.i.d.HealthMonitor]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] The HealthMonitor has detected a high load on the system. For more detailed information,
hazelcast-node1    | enable Diagnostics by adding the property -Dhazelcast.diagnostics.enabled=true
hazelcast-node1    | 2026-01-14 20:08:27,279 [ INFO] [hz.upbeat_jang.HealthMonitor] [c.h.i.d.HealthMonitor]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] processors=4, physical.memory.total=3.8G, physical.memory.free=1.0G, swap.
space.total=1024.0M, swap.space.free=1017.5M, heap.memory.used=74.3M, heap.memory.free=53.3M, heap.memory.total=128.0M, heap.memory.max=3.0G, heap.memory.used/total=58.01%, heap.memory.used/max=2.40%, minor.gc.count=8, minor.gc.
time=647ms, major.gc.count=0, major.gc.time=0ms, unknown.gc.count=8, unknown.gc.time=68ms, load.process=53.85%, load.system=93.75%, load.systemAverage=5.83, thread.count=56, thread.peakCount=57, cluster.timeDiff=0, event.q.size=
0, executor.q.async.size=0, executor.q.client.size=0, executor.q.client.query.size=0, executor.q.client.blocking.size=0, executor.q.query.size=0, executor.q.scheduled.size=0, executor.q.io.size=0, executor.q.system.size=0, execu
tor.q.operations.size=0, executor.q.priorityOperation.size=0, operations.completed.count=1476, executor.q.mapLoad.size=0, executor.q.mapLoadAllKeys.size=0, executor.q.cluster.size=0, executor.q.response.size=0, operations.running.count=0, operations.pending.invocations.percentage=0.00%, operations.pending.invocations.count=3, proxy.count=0, clientEndpoint.count=1, connection.active.count=5, client.connection.count=1, connection.count=3
hazelcast-node1    | 2026-01-14 20:08:47,985 [ INFO] [hz.upbeat_jang.HealthMonitor] [c.h.i.d.HealthMonitor]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] processors=4, physical.memory.total=3.8G, physical.memory.free=1.0G, swap.
space.total=1024.0M, swap.space.free=1017.5M, heap.memory.used=93.4M, heap.memory.free=34.3M, heap.memory.total=128.0M, heap.memory.max=3.0G, heap.memory.used/total=72.96%, heap.memory.used/max=3.02%, minor.gc.count=8, minor.gc.
time=647ms, major.gc.count=0, major.gc.time=0ms, unknown.gc.count=8, unknown.gc.time=68ms, load.process=60.00%, load.system=76.79%, load.systemAverage=6.80, thread.count=56, thread.peakCount=57, cluster.timeDiff=0, event.q.size=
0, executor.q.async.size=0, executor.q.client.size=0, executor.q.client.query.size=0, executor.q.client.blocking.size=0, executor.q.query.size=0, executor.q.scheduled.size=0, executor.q.io.size=0, executor.q.system.size=0, execu
tor.q.operations.size=0, executor.q.priorityOperation.size=0, operations.completed.count=5748, executor.q.mapLoad.size=0, executor.q.mapLoadAllKeys.size=0, executor.q.cluster.size=0, executor.q.response.size=0, operations.running.count=0, operations.pending.invocations.percentage=0.00%, operations.pending.invocations.count=4, proxy.count=0, clientEndpoint.count=1, connection.active.count=5, client.connection.count=1, connection.count=3
hazelcast-node1    | 2026-01-14 20:09:01,800 [ INFO] [hz.upbeat_jang.IO.thread-in-2] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=2, /172.28.0.11:5701->/172.28.0.13:46223, qualifier=null, endpoint=[172.28.0.13]:5701, remoteUuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 20:09:01,803 [ WARN] [hz.upbeat_jang.IO.thread-in-0] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=1, /172.28.0.11:51423->/172.28.0.13:5701, qualifier
=null, endpoint=[172.28.0.13]:5701, remoteUuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, alive=false, connectionType=MEMBER, planeIndex=0] closed. Reason: Exception in Connection[id=1, /172.28.0.11:51423->/172.28.0.13:5701, qualifier=null, endpoint=[172.28.0.13]:5701, remoteUuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, alive=true, connectionType=MEMBER, planeIndex=0], thread=hz.upbeat_jang.IO.thread-in-0
hazelcast-node1    | java.net.SocketException: Connection reset
hazelcast-node1    |    at java.base/sun.nio.ch.SocketChannelImpl.throwConnectionReset(SocketChannelImpl.java:401) ~[?:?]
hazelcast-node1    |    at java.base/sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:434) ~[?:?]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioInboundPipeline.process(NioInboundPipeline.java:115) ~[hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.processSelectionKey(NioThread.java:383) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.processSelectionKeys(NioThread.java:368) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.selectLoop(NioThread.java:294) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.networking.nio.NioThread.executeRun(NioThread.java:249) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    |    at com.hazelcast.internal.util.executor.HazelcastManagedThread.run(HazelcastManagedThread.java:111) [hazelcast-5.4.0.jar:5.4.0]
hazelcast-node1    | 2026-01-14 20:09:01,946 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.13:5701, timeout: 10000, bind-any: true  
hazelcast-node1    | 2026-01-14 20:09:01,978 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.13:5701. Reason: IOException[Connection refused to address /172.28.0.13:5701]
hazelcast-node1    | 2026-01-14 20:09:02,080 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.13:5701, timeout: 10000, bind-any: true  
hazelcast-node1    | 2026-01-14 20:09:02,082 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.13:5701. Reason: IOException[Connection refused to address /172.28.0.13:5701]
hazelcast-node1    | 2026-01-14 20:09:12,894 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connecting to /172.28.0.13:5701, timeout: 10000, bind-any: true  
hazelcast-node1    | 2026-01-14 20:09:22,898 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.s.t.TcpServerConnector]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Could not connect to: /172.28.0.13:5701. Reason: IOException[Connect timed out to address /172.28.0.13:5701]
hazelcast-node1    | 2026-01-14 20:09:22,899 [ WARN] [hz.upbeat_jang.cached.thread-7] [c.h.i.s.t.TcpServerConnectionErrorHandler]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Removing connection to endpoint [172.28.0.13]:5701 Cause => java.io.IOException {Connect timed out to address /172.28.0.13:5701}, Error-Count: 5
hazelcast-node1    | 2026-01-14 20:09:22,900 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.c.i.MembershipManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Removing Member [172.28.0.13]:5701 - db779203-23bd-404d-88dc-38a7a3cc9fdd
hazelcast-node1    | 2026-01-14 20:09:22,902 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.p.i.PartitionStateManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Storing snapshot of partition assignments while removing UUID db779203-23bd-404d-88dc-38a7a3cc9fdd
hazelcast-node1    | 2026-01-14 20:09:22,904 [ INFO] [hz.upbeat_jang.cached.thread-7] [c.h.i.c.ClusterService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | Members {size:2, ver:4} [
hazelcast-node1    |    Member [172.28.0.11]:5701 - 63a02f4a-ee00-4bfe-b1f3-52fe490ef094 this
hazelcast-node1    |    Member [172.28.0.12]:5701 - 4fc9c64f-5d25-423d-b419-7836387a4a5d
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 20:09:22,916 [ INFO] [hz.upbeat_jang.cached.thread-6] [c.h.t.TransactionManagerService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Committing/rolling-back live transactions of [172.28.0.13]:5701, UUID: db779203-23bd-404d-88dc-38a7a3cc9fdd
hazelcast-node1    | 2026-01-14 20:09:22,924 [ WARN] [hz.upbeat_jang.cached.thread-6] [c.h.c.i.RaftService]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, address=[172.28.0.13]:5701} is not present in the cluster. It will be auto-removed from the CP Subsystem after 14400 seconds.
hazelcast-node1    | 2026-01-14 20:09:23,404 [ INFO] [hz.upbeat_jang.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Repartitioning cluster data. Migration tasks count: 179
hazelcast-node1    | 2026-01-14 20:09:24,497 [ WARN] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.RaftNodeImpl$LeaderFailureDetectionTask(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Current leader RaftEndpoint{uuid='db779203-23bd-404d-88dc-38a7a3cc9fdd'} is not reachable. Will start new election round...
hazelcast-node1    | 2026-01-14 20:09:24,498 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: default(5082), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 20:09:24,520 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.t.PreVoteTask(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote started for next term: 2, last log index: 26044, last log term: 1
hazelcast-node1    | 2026-01-14 20:09:24,521 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: default(5082), size:3, term:1, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} - FOLLOWER this
hazelcast-node1    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 20:09:24,639 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Pre-vote granted from RaftEndpoint{uuid='4fc9c64f-5d25-423d-b419-7836387a4a5d'} for term: 2, number of votes: 2, majority: 2
hazelcast-node1    | 2026-01-14 20:09:24,639 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.h.PreVoteResponseHandlerTask(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] We have the majority during pre-vote phase. Let's start real election!
hazelcast-node1    | 2026-01-14 20:09:24,683 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.t.LeaderElectionTask(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Leader election started for term: 2, last log index: 26044, last log term: 1
hazelcast-node1    | 2026-01-14 20:09:24,696 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: default(5082), size:3, term:2, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} - CANDIDATE this
hazelcast-node1    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 20:09:24,748 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Vote granted from RaftEndpoint{uuid='4fc9c64f-5d25-423d-b419-7836387a4a5d'} for term: 2, number of votes: 2, majority: 2
hazelcast-node1    | 2026-01-14 20:09:24,753 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.h.VoteResponseHandlerTask(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] We are the LEADER!
hazelcast-node1    | 2026-01-14 20:09:24,755 [ INFO] [hz.upbeat_jang.partition-operation.thread-0] [c.h.c.i.r.i.RaftNode(default)]: [172.28.0.11]:5701 [counter-cluster] [5.4.0]
hazelcast-node1    |
hazelcast-node1    | CP Group Members {groupId: default(5082), size:3, term:2, logIndex:0} [
hazelcast-node1    |    CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9fdd, address=[172.28.0.13]:5701}
hazelcast-node1    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} - LEADER this
hazelcast-node1    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701}
hazelcast-node1    | ]
hazelcast-node1    |
hazelcast-node1    | 2026-01-14 20:09:25,154 [ INFO] [hz.upbeat_jang.migration] [c.h.i.p.i.MigrationManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] All migration tasks have been completed. (repartitionTime=Wed Jan 14 20:09:23 GMT 2026, plannedMigrations=179, completedMigrations=179, remainingMigrations=0, totalCompletedMigrations=179)
hazelcast-node1    | 2026-01-14 20:09:28,665 [ INFO] [hz.upbeat_jang.HealthMonitor] [c.h.i.d.HealthMonitor]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] processors=4, physical.memory.total=3.8G, physical.memory.free=1.2G, swap.
space.total=1024.0M, swap.space.free=1017.5M, heap.memory.used=83.4M, heap.memory.free=44.2M, heap.memory.total=128.0M, heap.memory.max=3.0G, heap.memory.used/total=65.18%, heap.memory.used/max=2.69%, minor.gc.count=9, minor.gc.
time=759ms, major.gc.count=0, major.gc.time=0ms, unknown.gc.count=8, unknown.gc.time=68ms, load.process=31.25%, load.system=71.19%, load.systemAverage=5.18, thread.count=54, thread.peakCount=57, cluster.timeDiff=0, event.q.size=
0, executor.q.async.size=0, executor.q.client.size=0, executor.q.client.query.size=0, executor.q.client.blocking.size=0, executor.q.query.size=0, executor.q.scheduled.size=0, executor.q.io.size=0, executor.q.system.size=0, execu
tor.q.operations.size=0, executor.q.priorityOperation.size=0, operations.completed.count=13661, executor.q.mapLoad.size=0, executor.q.mapLoadAllKeys.size=0, executor.q.cluster.size=0, executor.q.response.size=0, operations.running.count=0, operations.pending.invocations.percentage=0.00%, operations.pending.invocations.count=4, proxy.count=0, clientEndpoint.count=1, connection.active.count=3, client.connection.count=1, connection.count=2
hazelcast-node1    | 2026-01-14 20:10:22,568 [ INFO] [hz.upbeat_jang.IO.thread-in-1] [c.h.i.s.t.TcpServerConnection]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Connection[id=5, /172.28.0.11:5701->/172.28.0.3:55182, qualifier=null, endpoint=[172.28.0.3]:55182, remoteUuid=903e6e3e-99bc-4d06-bb7a-bb3f8d569d58, alive=false, connectionType=PYH, planeIndex=-1] closed. Reason: Connection closed by the other side
hazelcast-node1    | 2026-01-14 20:10:22,635 [ INFO] [hz.upbeat_jang.event-1] [c.h.c.i.ClientEndpointManager]: [172.28.0.11]:5701 [counter-cluster] [5.4.0] Destroying ClientEndpoint{connection=Connection[id=5, /172.28.0.11:5701-
>/172.28.0.3:55182, qualifier=null, endpoint=[172.28.0.3]:55182, remoteUuid=903e6e3e-99bc-4d06-bb7a-bb3f8d569d58, alive=false, connectionType=PYH, planeIndex=-1], clientUuid=903e6e3e-99bc-4d06-bb7a-bb3f8d569d58, clientName=hz.client_0, authenticated=true, clientVersion=5.4.0, creationTime=1768421292673, latest clientAttributes=null, labels=[]}

hazelcast-node2    | 2026-01-14 20:11:14,791 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:11:14,792 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:11:14,794 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:11:14,794 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node2    | 2026-01-14 20:12:16,165 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:12:16,166 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:12:16,167 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:12:16,168 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:12:16,169 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node2    | 2026-01-14 20:13:17,516 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:13:17,517 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:13:17,518 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:13:17,519 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:13:17,519 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node2    | 2026-01-14 20:14:18,834 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:14:18,835 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:14:18,837 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:14:18,838 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:14:18,838 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node2    | 2026-01-14 20:15:20,141 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:15:20,142 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:15:20,143 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:15:20,145 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:15:20,145 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node2    | 2026-01-14 20:16:21,499 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:16:21,500 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:16:21,502 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:16:21,504 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:16:21,504 [ INFO] [hz.cool_mcclintock.cached.thread-1] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node2    | 2026-01-14 20:17:22,918 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:17:22,919 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:17:22,920 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:17:22,922 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:17:22,959 [ INFO] [hz.cool_mcclintock.cached.thread-5] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
hazelcast-node2    | 2026-01-14 20:18:03,751 [ INFO] [hz.cool_mcclintock.HealthMonitor] [c.h.i.d.HealthMonitor]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] processors=4, physical.memory.total=3.8G, physical.memory.free=1.3G, s
wap.space.total=1024.0M, swap.space.free=1017.5M, heap.memory.used=66.1M, heap.memory.free=69.0M, heap.memory.total=136.0M, heap.memory.max=3.0G, heap.memory.used/total=48.63%, heap.memory.used/max=2.14%, minor.gc.count=16, mino
r.gc.time=1062ms, major.gc.count=0, major.gc.time=0ms, unknown.gc.count=10, unknown.gc.time=151ms, load.process=76.72%, load.system=4.02%, load.systemAverage=0.07, thread.count=59, thread.peakCount=59, cluster.timeDiff=0, event.
q.size=0, executor.q.async.size=0, executor.q.client.size=0, executor.q.client.query.size=0, executor.q.client.blocking.size=0, executor.q.query.size=0, executor.q.scheduled.size=0, executor.q.io.size=0, executor.q.system.size=0
, executor.q.operations.size=0, executor.q.priorityOperation.size=0, operations.completed.count=48158, executor.q.mapLoad.size=0, executor.q.mapLoadAllKeys.size=0, executor.q.cluster.size=0, executor.q.response.size=0, operations.running.count=0, operations.pending.invocations.percentage=0.00%, operations.pending.invocations.count=0, proxy.count=0, clientEndpoint.count=0, connection.active.count=2, client.connection.count=0, connection.count=1
hazelcast-node2    | 2026-01-14 20:18:23,629 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:18:23,630 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:18:23,631 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Skipped CPMember{uuid=db779203-23bd-404d-88dc-38a7a3cc9
fdd, address=[172.28.0.13]:5701} for leadership rebalancing due to java.util.concurrent.CompletionException: com.hazelcast.spi.exception.TargetNotMemberException: Not Member! target: [172.28.0.13]:5701, partitionId: -1, operation: com.hazelcast.cp.internal.operation.GetLeadedGroupsOp, service: hz:core:raft
hazelcast-node2    | 2026-01-14 20:18:23,632 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] Current leadership claims:
hazelcast-node2    |    CPMember{uuid=4fc9c64f-5d25-423d-b419-7836387a4a5d, address=[172.28.0.12]:5701} priority 0 has 1,
hazelcast-node2    |    CPMember{uuid=63a02f4a-ee00-4bfe-b1f3-52fe490ef094, address=[172.28.0.11]:5701} priority 0 has 1, leaderships.
hazelcast-node2    | 2026-01-14 20:18:23,633 [ INFO] [hz.cool_mcclintock.cached.thread-3] [c.h.c.i.RaftGroupMembershipManager]: [172.28.0.12]:5701 [counter-cluster] [5.4.0] CPGroup leadership balance is fine, cannot rebalance further...
```