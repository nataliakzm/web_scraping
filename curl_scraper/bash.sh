#!/bin/bash

# Use Rotating Proxies with cURL

# Read the list of proxies from a text file and test each one of them 
while read -r proxy; do
    echo "Testing proxy: $proxy"

    # Make a request through the proxy using cURL and check if it was successful
    if curl --proxy "$proxy" -k https://httpbin.org/anything
 >/dev/null 2>&1; then
        curl --proxy "$proxy" -k https://httpbin.org/anything
        echo "Success! Proxy $proxy works."
    else
        echo "Failed to connect to $proxy"
    fi

    # Wait a bit before testing the next proxy to avoid being blocked 
        # by the server for too many requests in a short period of time (DDoS)
    sleep 1
done < proxies.txt