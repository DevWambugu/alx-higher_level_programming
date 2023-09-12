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

  rotate () {
    const tempHolder = this.height;
    this.height = this.width;
    this.width = tempHolder;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
