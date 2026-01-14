#!/bin/bash

echo "=========================================="
echo "PostgreSQL Counter Tests"
echo "=========================================="
echo ""

echo "Step 1: Starting PostgreSQL..."
docker-compose up -d postgres

echo ""
echo "Step 2: Waiting for PostgreSQL to be ready..."
sleep 5

echo ""
echo "Step 3: Running tests..."
docker-compose --profile testing up test-runner

echo ""
echo "Step 4: Viewing results..."
docker-compose logs test-runner

echo ""
echo "=========================================="
echo "Tests completed!"
echo "=========================================="
echo ""
echo "To stop PostgreSQL:"
echo "  docker-compose down"

