#!/usr/bin/node
const argv = process.argv;
const argc = process.argv.length;
if (argc < 4) {
  console.log(0);
} else {
  const array = argv.slice(2).sort().reverse();
  const number = array[1];
  console.log(number);
}
