export default function getListStudentIds(objectArray) {
  if (!Array.isArray(objectArray)) {
    return [];
  }

  return objectArray.map((o) => o.id);
}
