// Displays the question
console.log('Welcome to Holberton School, what is your name?');

// Retrieves the user name
process.stdin.on('data', (data) => {
  // Converts the Buffer to a string and removes spaces
  console.log('Your name is:', data.toString().trim());

  // Closing message
  console.log('This important software is now closing');
  process.exit(0); // 0 = success
});
