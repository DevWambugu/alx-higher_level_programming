#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  return (a + b);
}
const firstnumber = Number(argv[2]);
const secondnumber = Number(argv[3]);
const sum = add(firstnumber, secondnumber);
console.log(sum);
