#!/usr/bin/node
exports.esrever = function (list) {
  const newReversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newReversedList.push(list[i]);
  }
  return (newReversedList);
};
