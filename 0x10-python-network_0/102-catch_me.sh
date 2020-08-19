#!/bin/bash
# Get request to the URL and display the body of the response
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
