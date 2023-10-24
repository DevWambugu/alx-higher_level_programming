#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const starWarsApi = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsApi, function (error, result, body) {
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (characterErr, characterRes, characterBody) {
      console.log(JSON.parse(characterBody).name);
    });
  }
});
