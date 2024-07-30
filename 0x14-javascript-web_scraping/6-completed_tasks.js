#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);
      const completed = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          completed[todo.userId] = (completed[todo.userId] || 0) + 1;
        }
      });

      // Print the results
      console.log(JSON.stringify(completed, null, 2));
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error:', error);
  }
});
