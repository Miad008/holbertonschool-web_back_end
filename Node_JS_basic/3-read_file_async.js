const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const header = lines[0].split(',');
      const idxFn = header.findIndex((ele) => ele === 'firstname');
      const idxFd = header.findIndex((ele) => ele === 'field');
      const fields = {};
      const students = {};

      for (let i = 1; i < lines.length; i++) {
        const list = lines[i].split(',');
        const field = list[idxFd];
        const firstname = list[idxFn];

        if (!fields[field]) fields[field] = 0;
        fields[field] += 1;

        if (!students[field]) students[field] = '';
        students[field] += students[field] ? `, ${firstname}` : firstname;
      }

      console.log(`Number of students: ${lines.length - 1}`);
      for (const field in fields) {
        if (Object.hasOwnProperty.call(fields, field)) {
          console.log(`Number of students in ${field}: ${fields[field]}. List: ${students[field]}`);
        }
      }

      resolve();
    });
  });
}

module.exports = countStudents;
