#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error != null) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
