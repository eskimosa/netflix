#!/bin/bash

# wait-for-it.sh - waits for a service to be available

# Exit on error
set -e

host="$1"
port="$2"
shift 2
cmd="$@"

# Print the host and port for debugging purposes
echo "Host: $host"
echo "Port: $port"

# Loop until the service is available
until nc -z "$host" "$port"; do
  echo "Waiting for $host:$port to be available..."
  sleep 1
done

echo "$host:$port is available - executing command"
exec $cmd

