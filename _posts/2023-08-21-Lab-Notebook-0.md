---
layout: post
title: Lab Notebook 0
description: Progress with hacks for week 0!
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 0}}
---

# Why I love my tools

### Essential Tools for Computer Science and Analysis (CSA)
In the world of Computer Science and Analysis (CSA), a wide array of tools contribute to the success of various projects and endeavors. While there are many tools available, some are considered fundamental for anyone seeking to excel in this field. In this blog post, we'll delve into the major tools that are vital for success in CSA.

### WSL - Windows Subsystem for Linux

WSL (Windows Subsystem for Linux) is a powerful tool that bridges the gap between Windows and Linux environments. It allows developers to run a Linux distribution alongside their Windows system, enabling seamless interaction with Linux-based tools and commands. WSL is invaluable for those who need to work with tools and frameworks that are predominantly Linux-oriented.

### VSCode - Visual Studio Code

VSCode (Visual Studio Code) is a versatile code editor that has gained immense popularity among developers. With its rich extension ecosystem, VSCode supports a wide range of programming languages, making it a go-to choice for coding projects across various domains. Its features, such as IntelliSense and integrated version control, significantly boost productivity.

### GitHub - Version Control and Code Hosting

GitHub is a widely used platform for version control, collaboration, and code hosting. It provides a robust environment for developers to manage their code repositories, collaborate with team members, and contribute to open-source projects. GitHub also offers GitHub Pages, a powerful feature for hosting static websites and blogs directly from your repositories.

### Python - Versatile Programming Language

Python is a versatile and beginner-friendly programming language that finds extensive use in CSA. Known for its readability and ease of use, Python is ideal for various tasks, from data analysis and machine learning to web development. Its extensive libraries and frameworks make it a must-have tool for developers and data scientists alike.

### Java - Robust and Widely Used Programming Language

Java is a robust and widely used programming language that excels in building large-scale applications and platforms. Its platform independence, object-oriented nature, and extensive libraries make it a preferred choice for projects that require performance and scalability.

### Jekyll - Static Site Generator

Jekyll is a static site generator that simplifies the process of building websites and blogs. It enables developers to create dynamic-looking websites using simple templates and Markdown content. Jekyll's integration with GitHub Pages makes it a natural choice for hosting technical blogs and documentation.

### Ruby - Dynamic and Expressive Programming Language

Ruby is a dynamic and expressive programming language that's often associated with web development. While it's used in various contexts, Ruby is particularly known for its role in building web applications using the Ruby on Rails framework. It's also a fundamental tool for local hosting and server-side scripting.

### Jupyter - Interactive Computing and Blogging

Jupyter provides an interactive environment for coding, data analysis, and blogging. Jupyter Notebooks allow you to create documents that combine code, visualizations, and explanatory text, making it an excellent tool for technical blogging. You can showcase your coding experiments, analyze data, and share insights in a single, interactive document.

In conclusion, these tools form the backbone of success in Computer Science and Analysis. Whether you're coding, collaborating, building websites, or creating insightful blogs, these tools empower you to tackle challenges effectively and showcase your expertise in the field.

Remember, the technology landscape is continually evolving, and staying up-to-date with these tools and their advancements will undoubtedly contribute to your journey in CSA.

# Linux Hacks

Installing Ubuntu: 
sudo apt update
sudo apt upgrade -y

Finding Ubuntu Version:
lsb_release -a

Getting Github Info:
git config --global --get <user.name>
git config --global --get <user.email>

User.name is your name in github while user.email is your email that you used to sign in into github.

Testing/Installing Python:
- "sudo apt install -y python3" will install python, resulting in the terminal "Installing Python..."
- If python is installed, it will return "Python is already installed."
- You may check the version through: "python3 --version"

Testing Ruby:
- Install ruby through "sudo apt install -y ruby-full build-essential zlib1g-dev"
- If installed, it should state "Ruby is already installed."
- To check the version, type "ruby -v"

Testing Jupyter:
- Use the command "sudo apt-get install -y jupyter-notebook" to install Jupyter
- It should say "Jupyter is already installed" if Bundler is already installed
- Check the version through "jupyter --version"

Testing Bundler:
- Use the command "gem install jekyll bundler" to install Bundler
- It should say "Bundler is already installed" if Bundler is already installed

Some Linux commands used for later usage: 
ls: List files and directories in the current directory.
cd: Change the current directory.
pwd: Print the current working directory.
cp: Copy files or directories.
mv: Move or rename files or directories.
rm: Remove files or directories.
grep: Search for patterns in files.
chmod: Change file permissions.
top: Display system resource usage.
df: Display disk space usage.
ps: List currently running processes.
cat: Display the contents of a file.

