#!/usr/bin/node
const { argv } = require('process');
const intValue = parseInt(argv[2]);

function factorial (factInt) {
  if (isNaN(factInt)) {
    return (1);
  } else if (factInt === 0) {
    return (1);
  } else {
    return (factInt * factorial(factInt - 1));
  }
}

const factResult = factorial(intValue);
console.log(factResult);
