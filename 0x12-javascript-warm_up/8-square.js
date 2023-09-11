#!/usr/bin/node
const { argv } = require('process');
const x = parseInt(argv[2]);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'x';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
