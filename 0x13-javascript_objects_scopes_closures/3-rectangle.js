#!/usr/bin/node
class Rectangle {
  constructor (h, w) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' ||
      typeof h !== 'number') {
      return {};
    }
    this.height = h;
    this.width = w;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
