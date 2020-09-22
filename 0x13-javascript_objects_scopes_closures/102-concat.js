#!/usr/bin/node
const argv = process.argv;
const file = require('fs');
const fileA = argv[2];
const textA = file.readFileSync(fileA, 'utf8');
const fileB = argv[3];
const textB = file.readFileSync(fileB, 'utf8');
const fileC = argv[4];
file.writeFileSync(fileC, textA + textB);
