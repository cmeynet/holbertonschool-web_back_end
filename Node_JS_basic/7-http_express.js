const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      const cleanLines = lines.filter((line) => line.trim() !== '');
      const rows = cleanLines.slice(1);
      const students = rows.map((line) => line.split(','));

      const totalStudents = students.length;
      let output = `Number of students: ${totalStudents}\n`;

      const fields = {};
      for (const student of students) {
        const firstname = student[0];
        const field = student[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }

      for (const fieldName of Object.keys(fields)) {
        const names = fields[fieldName].join(', ');
        output += `Number of students in ${fieldName}: ${fields[fieldName].length}. List: ${names}\n`;
      }
      resolve(output.trim());
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const dataStudents = await countStudents(process.argv[2]);
    res.setHeader('Content-type', 'text/plain');
    res.status(200).send(`This is the list of our students\n${dataStudents}`);
  } catch (err) {
    res.send(err.message);
  }
});

if (require.main === module) {
  app.listen(1245);
}

module.exports = app;
