"""
Hazelcast Counter Implementation for Task 1
Uses IAtomicLong with CP Subsystem for distributed, fault-tolerant counting
"""

import hazelcast
import os


class HazelcastCounter:
    def __init__(self):
        """Initialize Hazelcast client and atomic counter"""
        # Get Hazelcast cluster members from environment or use defaults
        cluster_members = os.getenv(
            'HAZELCAST_MEMBERS',
            '172.27.0.11:5701,172.27.0.12:5701,172.27.0.13:5701'
        ).split(',')

        cluster_name = os.getenv('HAZELCAST_CLUSTER', 'task1-cluster')

        # Create Hazelcast client
        self.client = hazelcast.HazelcastClient(
            cluster_name=cluster_name,
            cluster_members=cluster_members
        )

        # Get atomic counter (CP Subsystem)
        self.counter = self.client.cp_subsystem.get_atomic_long("task1-counter").blocking()

        print(f"✓ Connected to Hazelcast cluster: {cluster_name}")
        print(f"  Members: {cluster_members}")

    def increment(self):
        """Increment counter and return new value"""
        return self.counter.increment_and_get()

    def get(self):
        """Get current counter value"""
        return self.counter.get()

    def reset(self):
        """Reset counter to 0"""
        self.counter.set(0)
        return 0

    def close(self):
        """Shutdown Hazelcast client"""
        if self.client:
            self.client.shutdown()

