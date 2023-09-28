#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/stdout -w "%{http_code}" "$1" | awk 'NR==1{status=$0; next} status==200'
