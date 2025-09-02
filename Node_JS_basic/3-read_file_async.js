function countStudents(path) {
  return new Promise((resolve, reject) => {
    const fs = require('fs');

    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      const cleanLines = lines.filter(line => line.trim() !== '');
      const rows = cleanLines.slice(1);
      const students = rows.map(line => line.split(','));

      let output = `Number of students: ${students.length}\n`;

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

module.exports = countStudents;
