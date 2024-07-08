#!/usr/bin/node

//import 'process'
const process = require('process');

//retrieve second argument
const x = process.argv[2];

//check if x is a number
const size = parseInt(x);

if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
