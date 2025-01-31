#!/usr/bin/node
const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';
for (let i = 0; i < arr.length; i++) {
  output += arr[i] + (i < arr.length - 1 ? '\n' : '');
}
console.log(output);
