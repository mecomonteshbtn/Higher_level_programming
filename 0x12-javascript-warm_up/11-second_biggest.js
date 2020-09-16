#!/usr/bin/node
const argv = process.argv;
const argc = process.argv.length;
if (argc < 4) {
  console.log(0);
} else {
  const array = argv.sort().reverse();
  console.log(array[1]);
}
