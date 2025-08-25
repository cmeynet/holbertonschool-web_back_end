export default function getStudentsByLocation(listStudents, city) {
  return listStudents.filter((l) => l.location === city);
}
