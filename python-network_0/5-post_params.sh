#!/bin/bash
# Send POST request with data to a URL.
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"