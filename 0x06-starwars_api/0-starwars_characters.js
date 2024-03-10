#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    console.log(i);
    request(characters[i], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const people = JSON.parse(body).name;
      console.log(people);
    });
  }
});
