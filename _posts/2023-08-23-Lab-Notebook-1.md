---
layout: post
title: Lab Notebook 1
description: Progress with hacks for week 0!
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 0}}
---

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

