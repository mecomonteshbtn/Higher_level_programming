#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const element of list) {
    if (element === searchElement) {
      occurences++;
    }
  }
  return occurences;
};
