#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

const [fileA, fileB, dest] = args;

const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(dest, contentA + contentB);
