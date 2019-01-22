// component for spawning processes in nodejs
const spawn = require('child_process').spawn;

// the parameters provided by the user
const parameters = process.argv.splice(2);

// add the screenshots.py script name at the front of the parameter list
parameters.splice(0, 0, 'screenshots.py');

// spawn a new process with the given parameters
let screenshots = spawn('python', parameters);

// wait for the responses
screenshots.stdout.on('data', function (data) {
    console.log(data.toString());
});


