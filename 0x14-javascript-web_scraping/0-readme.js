#!/usr/bin/node

//import the module
const fs = require('fs');

//first argument is the file path
const file = process.argv[2];

//read the file
fs.readFile(file, 'utf8', (Error, data) => {
    if (Error) {
        console.error('Error reading file:', Error);
        return;
    }

    console.log(data);
});
