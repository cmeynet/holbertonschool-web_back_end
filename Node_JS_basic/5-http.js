const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-type': 'text/plain' });
    countStudents(process.argv[2]) // récupère le chemin du CSV
      .then((texte) => {
        res.end(`This is the list of our students\n${texte}`);
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  }
});

app.listen(1245);

module.exports = app;
