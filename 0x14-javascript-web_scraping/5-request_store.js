#!/usr/bin/node

// Import the built-in fs module
const fs = require('fs');

// Import the request module
const request = require('request');

// Use the 'request' module to perform an HTTP GET request for the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3])
