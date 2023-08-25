---
layout: blogs
permalink: /blogs
title: Soham's Blogs
---
##### This is what I have been doing in CSP class


<html>
<head>
    <title>Search Terms</title>
    <script>
        var terms = []; // Global array to store terms

        function loadTerms() {
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "terms.txt", true);
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var rawData = xhr.responseText;
                    var lines = rawData.split("\n");
                    for (var i = 0; i < lines.length; i++) {
                        var termData = lines[i].split("=");
                        terms.push(termData);
                    }
                }
            };
            xhr.send();
        }

        function searchTerms() {
            var searchInput = document.getElementById("searchInput").value;
            var resultOutput = document.getElementById("resultOutput");
            var found = false;

            for (var i = 0; i < terms.length; i++) {
                if (searchInput === terms[i][0]) {
                    found = true;
                    resultOutput.innerText = "Definition:\n" + terms[i][1];
                    break; // No need to continue searching if term is found
                }
            }

            if (!found) {
                resultOutput.innerText = "Sorry, we can't find that term. Make sure you have spelled your query correctly.";
            }
        }
    </script>
</head>
<body onload="loadTerms()">
    <h1>Search Terms</h1>
    <input type="text" id="searchInput" placeholder="Enter your search">
    <button onclick="searchTerms()">Search</button>
    <div id="resultOutput"></div>
</body>
</html>

 
 
## Super Quick Overview

| Week | Accomplishments |
| ----------- | ----------- |
| 0 | Installed WSL, VSCode, and created github repo|
| 1 |Set up website, commited changes to github|


## August 22th 2023 
Committed the repository to github. And started working on my website.

### 1) Committing and Push

a) I clicked source control on the right side of VSCode and committed all the changes. I also synced all the changes

b) I started working on my website

## August 21th, 2023
Today I setup Jupyter notebook, Installed Gemfile dependencies, and started a server

### 1) Installing Packages

a) I went to the command prompt and ran theses commands:
    
    pip install nbconvert 
    pip install nbformat
    pip install pyyaml
    jupyter --version
    jupyter kernelspec list

b) Then I went to VSCode and opened the terminal in it

c) Then I ran the command: 
    **bundle install**
This installs dependencies in my Gemfile

d) Then I could finally start my local server by running:
    **make** 
Initially the command didn't work but after commenting line 7 on Makefile (a file in student repo)
(to find out what bundle install and make are, refer to terms page below)


## August 18th, 2023
Today I cloned the teacher repository (for practice) and a student repository for my website. I also configured a git connection with Git Hub and installed/updated a lot of packages.

### 1) Cloning the repository

a) First I opened WSL. Then I used the command **cd vscode** to make sure that the I am in the vscode directory

b) Then I used the command **git clone https://github.com/nighthawkcoders/teacher.git** to clone the teacher repository on VScode (this is just for my practice. I will be cloning the student repository)

c) Then, I went to github to create my personal repository. This is so that after I clone the student repository, I can push it to my own repository on github.

d) After that I used the command **git clone https://github.com/nighthawkcoders/student** to clone the repository.

e) I opened the repository throught VScode using **code student**
Make sure you are running VSCode from WSL

<img src="images/vscode_in_WSL.png" alt=" " width="450" height="80" border="10" />

(Bottom left view of VSCode)

### 2) Git connection to Github

a) I ran 2 commands on WSL: 

    git config --global user.email <sohampkul@gmail.com>

    git config --global user.name <SOoctosnake>
 

### 3) Install and Udpating all the packages

I ran these commands below. Keep in mind that the lines starting with '#' are comment and not actual commands
I had a lot of these packages installed and up to date but it never hurts to be safe.

    sudo apt update
    sudo apt upgrade -y

    # Install Ruby and necessary development tools
    sudo apt install -y ruby-full build-essential zlib1g-dev

    # Install Python 3 and pip
    sudo apt-get install -y python3 python3-pip python-is-python3

    # Install Jupyter Notebook
    sudo apt-get install -y jupyter-notebook

    # Install Gems
    export GEM_HOME="$HOME/gems"
    export PATH="$HOME/gems/bin:$PATH"
    gem install jekyll bundler


## August 17th, 2023
I installed WSL and VSCode. This will help me make a website on github

###  1) WSL is a type of virtual machine inbuit in Windows to run linux.

a. To properly install WSL, I opened the command prompt as adminstrater. This is where we will be doing a lot of the installations

b. To install WSL, I used the command: 
    **wsl --install** 

c. After WSL installation, I ran this command to install Ubuntu from WSL: 
    **wsl --install -d Ubuntu**

### 2) Now I installed vscode. It is good to have all the files of a repository on github but if I wanted to actually make a website and edit it, I would need to use vscode

a) I first downloaded VScode here: [Download](https://code.visualstudio.com/)

b) Then install I it. I clicked on add the Remote Developers extension pack (forgot to do it before) and I clicked Add to PATH

Now I have VSCode and WSL working!


## Terms
    make - command that helps run your local server
    make convert - checks and ensures Jupyter notebooks are up to date
    make clean - stops the local server and cleans the files
    make stop - stops the local server
    cd ~ allows you to move through directories
    cd vscode - allows you to go to VSCode directory
    python –version - shows you your current python version
    jupyter –version - shows all your jupyter files and their current versions
    git clone - clones a repository 
    rbenv versions - shows your current ruby versions
    ruby -v - shows your current ruby version
    bundle install - this command installs the dependencies in your Gemfile
    ![]( ) - adds an image on markdown



