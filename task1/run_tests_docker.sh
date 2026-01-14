#!/bin/bash
# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'
echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}Web-Counter Performance Testing (Docker)${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""
# Get configuration from environment variables
INMEMORY_URL=${INMEMORY_URL:-"http://web-counter-inmemory:8080"}
FILE_URL=${FILE_URL:-"http://web-counter-file:8080"}
POSTGRES_URL=${POSTGRES_URL:-"http://web-counter-postgres:8080"}
REQUESTS_PER_CLIENT=${REQUESTS_PER_CLIENT:-10000}
echo -e "${YELLOW}Configuration:${NC}"
echo "  In-Memory URL: $INMEMORY_URL"
echo "  File URL: $FILE_URL"
echo "  PostgreSQL URL: $POSTGRES_URL"
echo "  Requests per client: $REQUESTS_PER_CLIENT"
echo ""
# Check if servers are running
check_server() {
    local url=$1
    local name=$2
    echo -n "Checking $name server... "
    for i in {1..30}; do
        if python -c "import requests; requests.get('$url/count')" 2>/dev/null; then
            echo -e "${GREEN}✓ Ready${NC}"
            return 0
        fi
        sleep 1
    done
    echo -e "${RED}✗ Not responding${NC}"
    return 1
}
# Run experiments for a given backend
run_backend_tests() {
    local url=$1
    local backend_name=$2
    echo ""
    echo -e "${BLUE}============================================================${NC}"
    echo -e "${BLUE}Testing $backend_name Backend${NC}"
    echo -e "${BLUE}============================================================${NC}"
    python client.py --url "$url" --run-all --requests-per-client $REQUESTS_PER_CLIENT
    local exit_code=$?
    if [ $exit_code -eq 0 ]; then
        echo -e "${GREEN}✓ $backend_name tests completed successfully${NC}"
    else
        echo -e "${RED}✗ $backend_name tests failed with exit code $exit_code${NC}"
    fi
    return $exit_code
}
# Main execution
main() {
    echo -e "${YELLOW}Waiting for servers to be ready...${NC}"
    echo ""
    inmemory_running=false
    file_running=false
    postgres_running=false
    if check_server "$INMEMORY_URL" "In-Memory"; then
        inmemory_running=true
    fi
    if check_server "$FILE_URL" "File"; then
        file_running=true
    fi
    if check_server "$POSTGRES_URL" "PostgreSQL"; then
        postgres_running=true
    fi
    echo ""
    if [ "$inmemory_running" = false ] && [ "$file_running" = false ] && [ "$postgres_running" = false ]; then
        echo -e "${RED}ERROR: No servers are responding!${NC}"
        exit 1
    fi
    # Run tests
    all_passed=true
    if [ "$inmemory_running" = true ]; then
        run_backend_tests "$INMEMORY_URL" "In-Memory"
        if [ $? -ne 0 ]; then
            all_passed=false
        fi
    fi
    if [ "$file_running" = true ]; then
        run_backend_tests "$FILE_URL" "File"
        if [ $? -ne 0 ]; then
            all_passed=false
        fi
    fi
    if [ "$postgres_running" = true ]; then
        run_backend_tests "$POSTGRES_URL" "PostgreSQL (Atomic Update)"
        if [ $? -ne 0 ]; then
            all_passed=false
        fi
    fi
    echo ""
    echo -e "${BLUE}============================================================${NC}"
    if [ "$all_passed" = true ]; then
        echo -e "${GREEN}All experiments completed successfully!${NC}"
        echo -e "${BLUE}============================================================${NC}"
        exit 0
    else
        echo -e "${RED}Some experiments failed!${NC}"
        echo -e "${BLUE}============================================================${NC}"
        exit 1
    fi
}
# Run main function
main
