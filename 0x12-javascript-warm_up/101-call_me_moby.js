#!/usr/bin/node
exports.callMeMoby = function (number, functionality) {
  for (let i = 0; i < number; i++) {
    functionality();
  }
};
