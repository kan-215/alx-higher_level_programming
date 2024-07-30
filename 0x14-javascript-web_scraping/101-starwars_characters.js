#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

//  GET request to the Star Wars API URL 
request(apiUrl, function (error, response, body) {
  // Check for  errors during the HTTP request
  if (!error && response.statusCode === 200) {
    // Parse the JSON response
    const movieData = JSON.parse(body);
    //  array of promises to fetch data for individual characters
    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        // request to fetch data for individual characters.
        request(characterUrl, function (charError, charResponse, charBody) {
          // Check for errors during the HTTP request
          if (!charError && charResponse.statusCode === 200) {
            // Parse the JSON response body
            const characterData = JSON.parse(charBody);
            // Resolve the promise with the name of the character.
            resolve(characterData.name);
          } else {
            // reject the promise with the error message if  there was an error during the HTTP request
            reject(new Error(`Error fetching character data: ${charError}`));
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        console.log(characterNames.join('\n'));
      })
      .catch((error) => {
        console.error(error.message);
      });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
