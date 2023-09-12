#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += char;
      }
      console.log(row);
    }
  }
};
