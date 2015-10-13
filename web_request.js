var request = require('request');

var name = 'Sir Gnar';

request('http://localhost:3000/' + name, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body);
  }
});