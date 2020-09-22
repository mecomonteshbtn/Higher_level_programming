#!/usr/bin/node
const array = require('./100-data').list;
console.log(array);
const compute = array.map(x => x * array.indexOf(x));
console.log(compute);
