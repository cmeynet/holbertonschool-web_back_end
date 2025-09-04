const http = require('http');
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

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-type': 'text/plain' });
    countStudents(process.argv[2])
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
