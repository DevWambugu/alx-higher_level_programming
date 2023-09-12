#!/usr/bin/node
class Rectangle {
  constructor(h, w) {
    if (w <= 0 || h <= 0 || typeof w != 'number' ||
      typeof h != 'number') {
      return {};
    }
    this.height = h;
    this.width = w;
  }
}
module.exports = Rectangle;
