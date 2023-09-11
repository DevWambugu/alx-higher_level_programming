#!/usr/bin/node
const { argv } = require('process');

function secondBiggest (argumentsPassed) {
  if (argumentsPassed.length === 0 || argumentsPassed.length === 1) {
    return (0);
  } else {
    const sortedArguments = argumentsPassed;
    sortedArguments.sort((a, b) => a - b);
    return (sortedArguments[1]);
  }
}

const args = argv.slice(2).map(Number);
const secondBiggestNo = secondBiggest(args);
console.log(secondBiggestNo);
