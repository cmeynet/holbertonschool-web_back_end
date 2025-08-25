export default function getStudentIdsSum(listStudents) {
  return listStudents.reduce((acc, n) => acc + n.id, 0);
}
