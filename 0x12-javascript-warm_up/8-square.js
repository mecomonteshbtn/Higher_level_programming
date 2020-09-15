#!/usr/bin/node
const number = process.argv[2];
if (!parseInt(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
