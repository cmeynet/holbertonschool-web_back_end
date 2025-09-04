// Displays the question
console.log('Welcome to Holberton School, what is your name?');

// Retrieves the user name
process.stdin.on('data', (data) => {
  // Converts the Buffer to a string and removes spaces
  process.stdout.write(`Your name is: ${data}`);
  process.exit(0); // 0 = success
});
// Closing message
process.on('exit', () => {
  console.log('This important software is now closing');
});
