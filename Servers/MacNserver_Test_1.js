// This server is not up on AWS
// This is test server

const express = require("express");
const app = express();
const port = 5000;
const path = require("path");

// Path to the pages directory
const pagesPath = path.join(__dirname, 'pages');

// parse incoming requests with JSON payloads
app.use(express.json());

// parse url encoded bodies (for form submissions)
app.use(express.urlencoded({ extended: true }));

// Server static files from the 'pages' directory
app.use(express.static(pagesPath));

// Sanitize input function
function sanitizedInput(input) {
    const pattern = /<.*?>|script/gi; // Unwanted characters or sequences
    return input.replace(pattern, ''); // Replace unwanted sequences with an empty string
}

// Sanitize all incoming query and body parameters
app.use((req, res, next) => {
    if (req.query) {
        Object.keys(req.query).forEach(key => {
            req.query[key] = sanitizedInput(req.query[key]);
        });
    }

    if (req.body) {
        Object.keys(req.body).forEach(key => {
            req.body[key] = sanitizedInput(req.body[key]);
        });
    }

    next();
});

app.get("/", (req, res) => {
    res.sendFile(path.join(pagesPath, 'index.html'));
});

// Route to demonstrate sanitized input
app.post("/submit", (req, res) => {
    // Assuming req.body contains form data
    const sanitizedData = req.body;
    console.log("Sanitized Data: ", sanitizedData);
    res.send("Data received and sanitized");
});

// Create and Start the server for the API on the defined port
app.listen(port, () => {
    console.log(`MacN app is listening at http://localhost:${port}`);
});
