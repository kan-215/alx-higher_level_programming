#!/usr/bin/node

// request module 
const request = require('request');

//  HTTP GET request for the URL
request(process.argv[2], function (error, response, body) {
  // Check for errors during the HTTP request.
  if (!error) {
    // parse the JSON data and extract the results array
    const results = JSON.parse(body).results;
    //  iterate through the movies in the results array using the reduce method
    console.log(results.reduce((count, movie) => {
      // check if there is a character with ID 18
      return movie.characters.find((character) => character.endsWith('/18/'))
       // If a character with ID 18 is found, increment count by 1.
        ? count + 1
        // else keep the count running
        : count;
    }, 0));
  }
});
