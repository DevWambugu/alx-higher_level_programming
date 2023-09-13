#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const userID in dict) {
  const occurrence = dict[userID];
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(userID);
}
console.log(newDict);
