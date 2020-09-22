#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let data;
let movies = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    data = JSON.parse(body);
    data.results.forEach(function (result) {
      result.characters.forEach(function (character) {
        const split = character.split('/');
        if (split[split.length - 2] === '18') {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});
