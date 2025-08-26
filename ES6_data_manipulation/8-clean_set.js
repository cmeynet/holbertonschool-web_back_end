export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }

  const parts = [];
  for (const value of set) {
    if (value.startsWith(startString)) {
      const suffix = value.slice(startString.length);
      parts.push(suffix);
    }
  }
  return parts.join('-');
}
