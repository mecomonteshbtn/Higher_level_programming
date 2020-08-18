#!/bin/bash
# Display all HTTP methods the server will accept
curl -Is 0.0.0.0:5000/route_4| grep Allow | cut -c 8-
