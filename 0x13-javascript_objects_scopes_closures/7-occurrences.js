#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numberOfOccurences = 0;

  for (const element of list) {
    if (element === searchElement) {
      numberOfOccurences++;
    }
  }
  return (numberOfOccurences);
};
