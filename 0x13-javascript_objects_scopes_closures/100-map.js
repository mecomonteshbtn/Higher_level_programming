#!/usr/bin/node
const array = require('./100-data').list;
console.log(array.map(x => x * array.indexOf(x)));
