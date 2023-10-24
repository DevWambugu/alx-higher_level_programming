#!/usr/bin/node
// displays the status code of a GET request
const request = require('request');
request(process.argv[2], function (error, result) {
  if (error) {
    console.log('code:', error.statusCode);
  } else {
    console.log('code:', result.statusCode);
  }
});
