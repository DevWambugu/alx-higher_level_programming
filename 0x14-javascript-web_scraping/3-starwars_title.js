#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const starWarsapi = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
request(starWarsapi, function (error, result, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
