#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL passed as the first argument
URL="$1"

# Sends a POST request to the passed URL and displays the body of the response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$URL"
