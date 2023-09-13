#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase(number) {
  if (number === 0) {
    return('');
  }
  const remainder = number % base;
  return convertToBase(Math.floor(number / base)) + String(remainder);
  };
};
