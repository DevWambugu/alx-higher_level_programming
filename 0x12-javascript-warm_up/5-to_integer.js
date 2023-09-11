#!/usr/bin/node
const { argv } = require('process');
const intValue = parseInt(argv[2]);

if (!isNaN(intValue)) {
  console.log(`My number: ${process.argv[2]}`);
} else {
  console.log('Not a number');
}
