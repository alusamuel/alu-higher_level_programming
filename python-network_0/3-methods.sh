#!/bin/bash
# Show allowed HTTP methods for a URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-