const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.getJSON(url, function (body) {
  let name = body.name;
  $('DIV#character').text(name);
});
