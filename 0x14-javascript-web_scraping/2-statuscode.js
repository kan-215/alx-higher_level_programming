#!/usr/bin/node

const request = require('request');
// impport the request module.

request.get(process.argv[2])
// HTTP GET request to the URL using the request module

  .on('response', function (response) {
    // Set up an event listener

    console.log(`code: ${response.statusCode}`);
  });
