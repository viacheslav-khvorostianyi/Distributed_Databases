### Task1
To run the performance tests for the web-counter application using Docker, follow the steps below:
```./run_all_docker.sh```

To run performance testS for Hazelcast using Docker, follow the steps below:
```bash
docker compose -f docker-compose-hazelcast.yml up -d
sleep 30
docker compose -f docker-compose-hazelcast.yml run --rm client \
    python client.py --url http://server:8080 --run-all --requests-per-client 10000
````

#### The output:
```bash
web-counter-test-runner | ============================================================
web-counter-test-runner | Web-Counter Performance Testing (Docker)                                                                                                                                                                  
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Configuration:
web-counter-test-runner |   In-Memory URL: http://web-counter-inmemory:8080
web-counter-test-runner |   File URL: http://web-counter-file:8080
web-counter-test-runner |   PostgreSQL URL: http://web-counter-postgres:8080
web-counter-test-runner |   Requests per client: 10000
web-counter-test-runner |
web-counter-test-runner | Waiting for servers to be ready...
web-counter-test-runner |
web-counter-test-runner | Checking In-Memory server... ✓ Ready                                                                                                                                                                      
web-counter-test-runner | Checking File server... ✓ Ready                                                                                                                                                                           
web-counter-test-runner | Checking PostgreSQL server... ✓ Ready                                                                                                                                                                     
web-counter-test-runner |
web-counter-test-runner |
web-counter-test-runner | ============================================================                                                                                                                                              
web-counter-test-runner | Testing In-Memory Backend                                                                                                                                                                                 
web-counter-test-runner | ============================================================                                                                                                                                              
web-counter-test-runner |
web-counter-test-runner | ############################################################
web-counter-test-runner | # Running all experiments with 10000 requests per client
web-counter-test-runner | # Server: http://web-counter-inmemory:8080
web-counter-test-runner | ############################################################
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 1 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 10000
web-counter-test-runner |   Expected count: 10000
web-counter-test-runner |   Elapsed time: 32.5936 seconds
web-counter-test-runner |   Throughput: 306.81 requests/second
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 2 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 20000
web-counter-test-runner |   Expected count: 20000
web-counter-test-runner |   Elapsed time: 62.6226 seconds
web-counter-test-runner |   Throughput: 319.37 requests/second
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 5 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 50000
web-counter-test-runner |   Expected count: 50000
web-counter-test-runner |   Elapsed time: 129.0934 seconds
web-counter-test-runner |   Throughput: 387.32 requests/second
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | SUMMARY OF ALL EXPERIMENTS
web-counter-test-runner | ============================================================
web-counter-test-runner | Clients    Total Req    Time (s)     Throughput (req/s)
web-counter-test-runner | ------------------------------------------------------------
web-counter-test-runner | 1     10000        32.5936      306.81
web-counter-test-runner | 2     20000        62.6226      319.37
web-counter-test-runner | 5     50000        129.0934     387.32
web-counter-test-runner | ✓ In-Memory tests completed successfully                                                                                                                                                                  
web-counter-test-runner |
web-counter-test-runner | ============================================================                                                                                                                                              
web-counter-test-runner | Testing File Backend                                                                                                                                                                                      
web-counter-test-runner | ============================================================                                                                                                                                              
web-counter-test-runner |
web-counter-test-runner | ############################################################
web-counter-test-runner | # Running all experiments with 10000 requests per client
web-counter-test-runner | # Server: http://web-counter-file:8080
web-counter-test-runner | ############################################################
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 1 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 10000
web-counter-test-runner |   Expected count: 10000
web-counter-test-runner |   Elapsed time: 37.6194 seconds
web-counter-test-runner |   Throughput: 265.82 requests/second
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 2 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 20000
web-counter-test-runner |   Expected count: 20000
web-counter-test-runner |   Elapsed time: 67.9453 seconds
web-counter-test-runner |   Throughput: 294.35 requests/second
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 5 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 50000
web-counter-test-runner |   Expected count: 50000
web-counter-test-runner |   Elapsed time: 173.8542 seconds
web-counter-test-runner |   Throughput: 287.60 requests/second
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | SUMMARY OF ALL EXPERIMENTS
web-counter-test-runner | ============================================================
web-counter-test-runner | Clients    Total Req    Time (s)     Throughput (req/s)
web-counter-test-runner | ------------------------------------------------------------
web-counter-test-runner | 1     10000        37.6194      265.82
web-counter-test-runner | 2     20000        67.9453      294.35
web-counter-test-runner | 5     50000        173.8542     287.60
web-counter-test-runner | ✓ File tests completed successfully                                                                                                                                                                       
web-counter-test-runner |
web-counter-test-runner | ============================================================                                                                                                                                              
web-counter-test-runner | Testing PostgreSQL (Atomic Update) Backend                                                                                                                                                                
web-counter-test-runner | ============================================================                                                                                                                                              
web-counter-test-runner |
web-counter-test-runner | ############################################################
web-counter-test-runner | # Running all experiments with 10000 requests per client
web-counter-test-runner | # Server: http://web-counter-postgres:8080
web-counter-test-runner | ############################################################
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 1 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 10000
web-counter-test-runner |   Expected count: 10000
web-counter-test-runner |   Elapsed time: 197.0679 seconds
web-counter-test-runner |   Throughput: 50.74 requests/second
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 2 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 20000
web-counter-test-runner |   Expected count: 20000
web-counter-test-runner |   Elapsed time: 235.1090 seconds
web-counter-test-runner |   Throughput: 85.07 requests/second
web-counter-test-runner | Counter reset successfully
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | Running experiment: 5 client(s), 10000 requests each
web-counter-test-runner | ============================================================
web-counter-test-runner |
web-counter-test-runner | Results:
web-counter-test-runner |   Total count: 50000
web-counter-test-runner |   Expected count: 50000
web-counter-test-runner |   Elapsed time: 724.6053 seconds
web-counter-test-runner |   Throughput: 69.00 requests/second
web-counter-test-runner |
web-counter-test-runner | ============================================================
web-counter-test-runner | SUMMARY OF ALL EXPERIMENTS
web-counter-test-runner | ============================================================
web-counter-test-runner | Clients    Total Req    Time (s)     Throughput (req/s)
web-counter-test-runner | ------------------------------------------------------------
web-counter-test-runner | 1     10000        197.0679     50.74
web-counter-test-runner | 2     20000        235.1090     85.07
web-counter-test-runner | 5     50000        724.6053     69.00
web-counter-test-runner | ✓ PostgreSQL (Atomic Update) tests completed successfully                                                                                                                                                 
web-counter-test-runner |
web-counter-test-runner | ============================================================                                                                                                                                              
web-counter-test-runner | All experiments completed successfully!                                                                                                                                                                   
web-counter-test-runner | ============================================================                                                                                                                                              

HAZELCAST EXPERIMENTS
=============================================
############################################################
# Running all experiments with 1000 requests per client
# Server: http://server:8080
############################################################
Counter reset successfully

============================================================
Running experiment: 1 client(s), 1000 requests each
============================================================

Results:
  Total count: 1000
  Expected count: 1000
  Elapsed time: 6.9047 seconds
  Throughput: 144.83 requests/second
Counter reset successfully

============================================================
Running experiment: 2 client(s), 1000 requests each
============================================================

Results:
  Total count: 2000
  Expected count: 2000
  Elapsed time: 10.9221 seconds
  Throughput: 183.12 requests/second
Counter reset successfully

============================================================
Running experiment: 5 client(s), 1000 requests each
============================================================

Results:
  Total count: 5000
  Expected count: 5000
  Elapsed time: 17.9176 seconds
  Throughput: 279.06 requests/second

============================================================
SUMMARY OF ALL EXPERIMENTS
============================================================
Clients    Total Req    Time (s)     Throughput (req/s)
------------------------------------------------------------
1     1000         6.9047       144.83
2     2000         10.9221      183.12
5     5000         17.9176      279.06
```