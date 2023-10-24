#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const starWarsApi = process.argv[2];

let times = 0;

request(starWarsApi, function (error, result, body) {
  if (!error) {
    body = JSON.parse(body).results;
    for (let i = 0; i < body.length; ++i) {
      const characters = body[i].characters;

      for (let j = 0; j < characters.length; ++j) {
        const character = characters[j];
        const characterId = character.split('/')[5];
        if (characterId === '18') {
          times += 1;
        }
      }
    }
  }
  console.log(times);
});
