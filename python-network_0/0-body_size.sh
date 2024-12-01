#!/bin/bash
# Get HTTP response size in bytes.
curl -s "$1" | wc -c