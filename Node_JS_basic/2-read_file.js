function countStudents(path) {
  const fs = require('fs');
  try {
    const data = fs.readFileSync(path, 'utf8'); // lit le fichier de manière synchrone
    const lines = data.split('\n'); // divise le contenu du CSV en un tableau de lignes
    const cleanLines = lines.filter(line => line.trim() !== ''); // supprime les lignes vides ou contenant seulement des espaces
    const rows = cleanLines.slice(1); // retourne un tableau sans la première ligne
    const students = rows.map(line => line.split(',')); // transformer en tableau de tableaux
    const totalStudents = students.length; // compter le nombre d'étudiants
    console.log(`Number of students: ${totalStudents}`);

    // Regrouper le nombre d'étudiants par filière
    const fields = {}; // objet vide pour stocker les étudiants par filière
    for (const student of students) {
      const firstname = student[0]; // récupère le prénom
      const field = student[3]; // récupère la filière
      if (!fields[field]) {
        fields[field] = []; // crée un tableau vide si première fois qu'on rencontre une filière
      }
      fields[field].push(firstname); // ajoute le prénom de l'étudiant à la filière
    }

    // Afficher le nombre d'étudiants par filière
    for (const fieldName of Object.keys(fields)) { // récupère toutes les filières dans l'objet
      const names = fields[fieldName].join(', '); // transforme le tableau de prénoms en chaine séparée par des virgules
      console.log(`Number of students in ${fieldName}: ${fields[fieldName].length}. List: ${names}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
