export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Creates a buffer of `length` bytes in memory
  const buffer = new ArrayBuffer(length);

  // Creates a DataView to read/write typed values
  const dataView = new DataView(buffer);

  // Writes the signed 8-bit value at offset `position`
  dataView.setInt8(position, value);

  return dataView;
}
