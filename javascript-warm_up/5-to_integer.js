#!/usr/bin/node
let number = Number(process.argv[2]);
if (isNaN(number)) {
    console.log('Not a number');
} else {
    console.log(`My number: ${number}`);
}
