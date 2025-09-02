const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
    const databasePath = process.argv[2];

    countStudents(databasePath)
      .then((texte) => {
        res.send(`This is the list of our students\n${texte}`);
      })
      .catch(() => {
        res.send('Cannot load the database');
      });
});

app.listen(1245);

module.exports = app;
