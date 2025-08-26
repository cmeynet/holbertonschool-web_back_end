export default function updateUniqueItems(map) {
  if (!map instanceof Map) {
    throw new Error('Cannot process');
  }

  for (let [key, value] of map) {
    if (value === 1) {
        value = 100;
    }
    map.set(key, value);
}

    return {...map};
}