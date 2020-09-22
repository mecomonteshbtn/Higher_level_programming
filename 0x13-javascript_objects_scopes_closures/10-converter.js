#!/usr/bin/node
exports.converter = function converter (base) {
  return x => x.toString(base);
};
