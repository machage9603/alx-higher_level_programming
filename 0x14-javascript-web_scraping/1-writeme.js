#!/usr/bin/node

// import the module
const fs = require('fs');

// first argument is the file path
const file = process.argv[2];

// second arg is the string to write
const content = process.argv[3];

// write the file
fs.writeFile(file, content, 'utf-8', error => {
  if (error) {
    console.log(error);
  }
});
