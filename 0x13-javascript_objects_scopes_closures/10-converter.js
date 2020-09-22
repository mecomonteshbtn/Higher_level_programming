#!/usr/bin/node
exports.converter = function converter (base) {
  if (!converter.Number) {
    converter.Number = base;
    return converter;
  } else {
    return parseInt(converter.Number, base);
  }
};
