#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    return list.reduce((count, elem) => count + (elem === searchElement ? 1 : 0), 0);
};