#!/usr/bin/node

const fs = require('fs');
// Import the 'fs' module.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // Use fs.writeFile() to write data to a file specified as the third cmd line argument
  // The data is  taken from the 4th command-line argument (process.argv[3]).

  if (error) {
    // the 'error' parameter will contain an error object if the error parameter occurs
    console.error(error);
  }
});
