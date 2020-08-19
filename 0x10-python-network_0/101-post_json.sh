#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
