---
toc: true
comments: true
layout: post
title: Glossary
description: Search up terms for their definiton. These terms are from notes/hacks.
type: tangibles
courses: { compsci: {week: 1} }
---

<html>
<head>
    <title>Command Glossary</title>
    <style>
        /* Add some basic styling */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        input[type="text"] {
            width: 300px;
            padding: 5px;
        }

        #result {
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Command Glossary</h1>
    <p>Enter a command to get its definition:</p>
    <input type="text" id="searchInput" placeholder="Enter a command">
    <button onclick="search()">Search</button>
    <p id="result"></p>

    <script>
        // Define a JavaScript object to store command definitions
        const commandDefinitions = {
            "make": "Command that helps run your local server.",
            "make convert": "Checks and ensures Jupyter notebooks are up to date.",
            "make clean": "Stops the local server and cleans the files.",
            "make stop": "Stops the local server.",
            "cd ~": "Allows you to move through directories.",
            "cd vscode": "Allows you to go to the VSCode directory.",
            "python --version": "Shows your current Python version.",
            "jupyter --version": "Shows all your Jupyter files and their current versions.",
            "git clone": "Clones a repository.",
            "rbenv versions": "Shows your current Ruby versions.",
            "ruby -v": "Shows your current Ruby version.",
            "bundle install": "Installs the dependencies in your Gemfile.",
            "ls": "Lists files in the repository.",
            "pwd": "Print working directory command.",
            "mkdir": "Command used to create directories.",
            "echo": "Print any text that follows the command.",
            "clear": "Clears the terminal display.",
            "mv": "Move or rename files.",
            "useradd": "Adds a new user.",
            "sudo": "Command to create privileges."
        };

        // Function to search for a command and display its definition
        function search() {
            const searchInput = document.getElementById("searchInput").value;
            const resultElement = document.getElementById("result");

            if (commandDefinitions.hasOwnProperty(searchInput)) {
                resultElement.innerText = commandDefinitions[searchInput];
            } else {
                resultElement.innerText = "Command not found.";
            }
        }
    </script>
</body>
</html>

- make - command that helps run your local server
- make convert - checks and ensures Jupyter notebooks are up to date
- make clean - stops the local server and cleans the files
- make stop - stops the local server
- cd - allows you to move through directories
- cd vscode - allows you to go to VSCode directory
- python –version - shows you your current python version
- jupyter –version - shows all your jupyter files and their current versions
- git clone - clones a repository
- rbenv versions - shows your current ruby versions
- ruby -v - shows your current ruby version
- bundle install - this command installs the dependencies in your Gemfile
- adds an image
- ls - lists files in the respository
- pwd - Print working directory command
- mkdir - Command used to create directories
- echo - Print any text that follows the command
- clear - Clear the terminal display
- mv - Move or rename files
- useradd - adds a new user
- sudo - command to create privileges