#!/bin/bash
echo "=========================================="
echo "Web-Counter - Full Docker Test Suite"
echo "=========================================="
echo ""
echo "Step 1: Building Docker images..."
docker-compose build
echo ""
echo "Step 2: Starting servers (In-Memory, File, PostgreSQL)..."
docker-compose up -d web-counter-inmemory web-counter-file web-counter-postgres
echo ""
echo "Step 3: Waiting for servers to be healthy..."
sleep 15
echo ""
echo "Step 4: Running experiments..."
docker-compose --profile testing up test-runner
echo ""
echo "Step 5: Viewing results..."
docker-compose logs test-runner
echo ""
echo "=========================================="
echo "All tests completed!"
echo "=========================================="
echo ""
echo "Servers running:"
echo "  In-Memory:  http://localhost:8080"
echo "  File:       http://localhost:8081"
echo "  PostgreSQL: http://localhost:8082"
echo ""
echo "To stop servers, run:"
echo "  docker-compose down"
