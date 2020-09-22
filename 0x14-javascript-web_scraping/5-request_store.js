#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, 'utf8', function (error, data) {
      if (error) {
        console.error(error);
      }
    });
  }
});
