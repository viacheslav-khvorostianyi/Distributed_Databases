# Task 2 - PostgreSQL Counter Implementation

```bash
postgres-test-runner | 
postgres-test-runner | ============================================================
postgres-test-runner | PostgreSQL Counter Implementation Tests
postgres-test-runner | ============================================================
postgres-test-runner |
postgres-test-runner | ============================================================
postgres-test-runner | TEST: 1. Lost Update (NOT thread-safe)
postgres-test-runner | ============================================================
postgres-test-runner | Threads: 10
postgres-test-runner | Iterations per thread: 10000
postgres-test-runner | Expected final count: 100000
postgres-test-runner |
postgres-test-runner | Counter reset to 0
postgres-test-runner | Results:
postgres-test-runner |   Final counter value: 9995
postgres-test-runner |   Expected value: 100000
postgres-test-runner |   Lost updates: 90005
postgres-test-runner |   Elapsed time: 532.24 seconds
postgres-test-runner |   Throughput: 187.88 updates/second
postgres-test-runner |   ✗ FAILURE: Lost 90005 updates!
postgres-test-runner |
postgres-test-runner | ============================================================
postgres-test-runner | TEST: 2. Serializable Isolation Level
postgres-test-runner | ============================================================
postgres-test-runner | Threads: 10
postgres-test-runner | Iterations per thread: 10000
postgres-test-runner | Expected final count: 100000
postgres-test-runner |
postgres-test-runner | Counter reset to 0
postgres-test-runner | Results:
postgres-test-runner |   Final counter value: 100000
postgres-test-runner |   Expected value: 100000
postgres-test-runner |   Lost updates: 0
postgres-test-runner |   Elapsed time: 1011.15 seconds
postgres-test-runner |   Throughput: 98.90 updates/second
postgres-test-runner |   ✓ SUCCESS: No lost updates!
postgres-test-runner |
postgres-test-runner | ============================================================
postgres-test-runner | TEST: 3. In-place Atomic Update
postgres-test-runner | ============================================================
postgres-test-runner | Threads: 10
postgres-test-runner | Iterations per thread: 10000
postgres-test-runner | Expected final count: 100000
postgres-test-runner |
postgres-test-runner | Counter reset to 0
postgres-test-runner | Results:
postgres-test-runner |   Final counter value: 100000
postgres-test-runner |   Expected value: 100000
postgres-test-runner |   Lost updates: 0
postgres-test-runner |   Elapsed time: 463.39 seconds
postgres-test-runner |   Throughput: 215.80 updates/second
postgres-test-runner |   ✓ SUCCESS: No lost updates!
postgres-test-runner |
postgres-test-runner | ============================================================
postgres-test-runner | TEST: 4. Row-level Locking (FOR UPDATE)
postgres-test-runner | ============================================================
postgres-test-runner | Threads: 10
postgres-test-runner | Iterations per thread: 10000
postgres-test-runner | Expected final count: 100000
postgres-test-runner |
postgres-test-runner | Counter reset to 0
postgres-test-runner | Results:
postgres-test-runner |   Final counter value: 100000
postgres-test-runner |   Expected value: 100000
postgres-test-runner |   Lost updates: 0
postgres-test-runner |   Elapsed time: 463.38 seconds
postgres-test-runner |   Throughput: 215.81 updates/second
postgres-test-runner |   ✓ SUCCESS: No lost updates!
postgres-test-runner |
postgres-test-runner | ============================================================
postgres-test-runner | TEST: 5. Optimistic Concurrency Control
postgres-test-runner | ============================================================
postgres-test-runner | Threads: 10
postgres-test-runner | Iterations per thread: 10000
postgres-test-runner | Expected final count: 100000
postgres-test-runner |
postgres-test-runner | Counter reset to 0
postgres-test-runner | Results:
postgres-test-runner |   Final counter value: 100000
postgres-test-runner |   Expected value: 100000
postgres-test-runner |   Lost updates: 0
postgres-test-runner |   Elapsed time: 4651.62 seconds
postgres-test-runner |   Throughput: 21.50 updates/second
postgres-test-runner |   ✓ SUCCESS: No lost updates!
postgres-test-runner |
postgres-test-runner | ============================================================
postgres-test-runner | SUMMARY OF ALL TESTS
postgres-test-runner | ============================================================
postgres-test-runner | Test                                     Result     Time (s)     Throughput (ops/s)
postgres-test-runner | ------------------------------------------------------------
postgres-test-runner | 1. Lost Update (NOT thread-safe)         ✗ FAIL     532.24       187.88
postgres-test-runner | 2. Serializable Isolation Level          ✓ PASS     1011.15      98.90
postgres-test-runner | 3. In-place Atomic Update                ✓ PASS     463.39       215.80
postgres-test-runner | 4. Row-level Locking (FOR UPDATE)        ✓ PASS     463.38       215.81
postgres-test-runner | 5. Optimistic Concurrency Control        ✓ PASS     4651.62      21.50
postgres-test-runner | ============================================================
postgres-test-runner exited with code 0

==========================================
Tests completed!
==========================================

```