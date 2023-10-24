#!/usr/bin/node

// The script reads and prints the content of a file:
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
