#!/usr/bin/node

// import the module
const request = require('request');

// first argument is the URL to request(GET)
const url = process.argv[2];

// make a HTTP GET request
request(url, function (error, response, body) {
  // check for errors during the request
  if (error) {
    console.error(error);
  } else {
    // if there are no errors, print the status code
    console.log('code:', response.statusCode);
  }
});
