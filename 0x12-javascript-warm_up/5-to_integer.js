#!/usr/bin/node
const integer = parseInt(process.argv[2]);
if (integer) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
