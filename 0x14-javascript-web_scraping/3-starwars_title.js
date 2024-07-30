#!/usr/bin/node

// Import the 'request' module.
const request = require('request');

// create a  URL for the selected  Star Wars film
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Use the 'request' module to perform an HTTP GET request to the created URL link

request(url, function (error, response, body) {
  // log title if successful else log error if not.
  console.log(error || JSON.parse(body).title);
});
