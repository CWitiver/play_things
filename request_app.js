
var bodyParser = require('body-parser');
var express = require('express');
var request = require('request');

var app = express();  // Initialize Express app.

// Configure body parser.
app.use(bodyParser.json());      // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({  // to support URL-encoded bodies
  extended: true
}));

// Default GET url.
app.get('/', function (req, res) {
  res.send('' +
    '<html>' +
      '<head></head>' +
      '<body>' +
        '<form action="/" method="POST">' +
          '<span>Enter a Name:</span>' +
          '<input type="text" name="name_input" />' +
        '</form>' +
      '</body>' +
    '</html>')
});

// Default POST url.
app.post('/', function (req, res) {
  var name = req.body.name_input;
  request('http://localhost:3000/' + name, function (error, response, body) {
    if (!error && response.statusCode == 200) {
      res.send(body);
    }
  });
});

app.listen(4000);