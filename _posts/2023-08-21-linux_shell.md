---
layout: post
title: Linux Shell and Bash
description: A Tech Talk on Linux and the Bash shell.
toc: True
comments: True
categories: ['5.A', 'C4.1']
type: devops
---

## Bash Tutorial
> A brief overview of Bash, on your way to becoming a Linux expert.  When a computer boots up, a kernel (MacOS, Windows, Linux) is started.  This kernel provides a shell that allows user to interact with a most basic set of commands.  Typically, the casual user will not interact with the shell as a Desktop User Interface is started by the computer boot up process.  To activate a shell directly, users will run a "terminal" through the Desktop. VS Code provides ability to activate "terminal" while in the IDE.

## Prerequisites
> Setup bash shell dependency variables for this page.

- Hack: Change variables to match your project.


```python
%%script bash

# Dependency Variables, set to match your project directories

cat <<EOF > /tmp/variables.sh
export project_dir=$HOME/vscode  # change vscode to different name to test git clone
export project=\$project_dir/teacher  # change teacher to name of project from git clone
export project_repo="https://github.com/nighthawkcoders/teacher.git"  # change to project of choice
EOF
```


```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

# Access the variables
echo "Project dir: $project_dir"
echo "Project: $project"
echo "Repo: $project_repo"
```

    Project dir: /home/flyinglizard29/vscode
    Project: /home/flyinglizard29/vscode/teacher
    Repo: https://github.com/nighthawkcoders/teacher.git


## Setup Project
> Pull code from GitHub to your machine. This script will create a project directory and add "project" from GitHub to the vscode directory.  There is conditional logic to make sure that clone only happen if it does not (!) exist.


```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

echo "Using conditional statement to create a project directory and project"

cd ~    # start in home directory

# Conditional block to make a project directory
if [ ! -d $project_dir ]
then 
    echo "Directory $project_dir does not exists... makinng directory $project_dir"
    mkdir -p $project_dir
fi
echo "Directory $project_dir exists." 

# Conditional block to git clone a project from project_repo
if [ ! -d $project ]
then
    echo "Directory $project does not exists... cloning $project_repo"
    cd $project_dir
    git clone $project_repo
    cd ~
fi
echo "Directory $project exists." 
```

    Using conditional statement to create a project directory and project
    Directory /home/flyinglizard29/vscode exists.
    Directory /home/flyinglizard29/vscode/teacher exists.


### Look at files Github project
> All computers contain files and directories.  The clone brought more files from cloud to your machine.  Review the bash shell script observe the commands that show and interact with files and directories.

- "ls" lists computer files in Unix and Unix-like operating systems
- "cd" offers way to navigate and change working directory
- "pwd" print working directory
- "echo" used to display line of text/string that are passed as an argument


```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

echo "Navigate to project, then navigate to area wwhere files were cloned"
cd $project
pwd

echo ""
echo "list top level or root of files with project pulled from github"
ls

```

    Navigate to project, then navigate to area wwhere files were cloned
    /home/flyinglizard29/vscode/teacher
    
    list top level or root of files with project pulled from github
    Gemfile
    LICENSE
    Makefile
    README.md
    _config.yml
    _data
    _includes
    _layouts
    _notebooks
    _posts
    assets
    csa.md
    csp.md
    csse.md
    images
    index.md
    indexBlogs.md
    scripts


### Look at file list with hidden and long attributes
> Most linux commands have options to enhance behavior

[ls reference](https://www.rapidtables.com/code/linux/ls.html)


```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

echo "Navigate to project, then navigate to area wwhere files were cloned"
cd $project
pwd

echo ""
echo "list all files in long format"
ls -al   # all files -a (hidden) in -l long listing
```

    Navigate to project, then navigate to area wwhere files were cloned
    /home/flyinglizard29/vscode/teacher
    
    list all files in long format
    total 100
    drwxr-xr-x 12 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 .
    drwxr-xr-x  4 flyinglizard29 flyinglizard29 4096 Aug 18 11:53 ..
    drwxr-xr-x  8 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 .git
    drwxr-xr-x  3 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 .github
    -rw-r--r--  1 flyinglizard29 flyinglizard29  157 Aug 18 11:41 .gitignore
    -rw-r--r--  1 flyinglizard29 flyinglizard29  122 Aug 18 11:41 Gemfile
    -rw-r--r--  1 flyinglizard29 flyinglizard29 1081 Aug 18 11:41 LICENSE
    -rw-r--r--  1 flyinglizard29 flyinglizard29 3114 Aug 18 11:41 Makefile
    -rw-r--r--  1 flyinglizard29 flyinglizard29 8036 Aug 18 11:41 README.md
    -rw-r--r--  1 flyinglizard29 flyinglizard29  607 Aug 18 11:41 _config.yml
    drwxr-xr-x  2 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 _data
    drwxr-xr-x  2 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 _includes
    drwxr-xr-x  2 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 _layouts
    drwxr-xr-x  3 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 _notebooks
    drwxr-xr-x  2 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 _posts
    drwxr-xr-x  4 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 assets
    -rw-r--r--  1 flyinglizard29 flyinglizard29   92 Aug 18 11:41 csa.md
    -rw-r--r--  1 flyinglizard29 flyinglizard29   98 Aug 18 11:41 csp.md
    -rw-r--r--  1 flyinglizard29 flyinglizard29  108 Aug 18 11:41 csse.md
    drwxr-xr-x  2 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 images
    -rw-r--r--  1 flyinglizard29 flyinglizard29 5149 Aug 18 11:41 index.md
    -rw-r--r--  1 flyinglizard29 flyinglizard29   53 Aug 18 11:41 indexBlogs.md
    drwxr-xr-x  2 flyinglizard29 flyinglizard29 4096 Aug 18 11:41 scripts



```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

echo "Look for posts"
export posts=$project/_posts  # _posts inside project
cd $posts  # this should exist per fastpages
pwd  # present working directory
ls -l  # list posts
```

    Look for posts
    /home/flyinglizard29/vscode/teacher/_posts
    total 88
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  7685 Aug 18 11:41 2023-08-16-Tools_Equipment.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  4650 Aug 18 11:41 2023-08-16-pair_programming.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  7137 Aug 18 11:41 2023-08-17-markdown-html_fragments.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  6659 Aug 18 11:41 2023-08-23-javascript-calculator.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29 10642 Aug 18 11:41 2023-08-30-agile_methodolgy.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  3849 Aug 18 11:41 2023-08-30-javascript-music-api.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  5312 Aug 18 11:41 2023-09-06-javascript-motion-mario-oop.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  4812 Aug 18 11:41 2023-09-13-java-free_response.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29 13220 Aug 18 11:41 2023-10-16-java-api-pojo-jpa.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  6819 Aug 18 11:41 2023-11-13-jwt-java-spring.md



```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

echo "Look for notebooks"
export notebooks=$project/_notebooks  # _notebooks is inside project
cd $notebooks   # this should exist per fastpages
pwd  # present working directory
ls -l  # list notebooks
```

    Look for notebooks
    /home/flyinglizard29/vscode/teacher/_notebooks
    total 752
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  13014 Aug 18 11:41 2023-08-01-cloud_database.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29   8992 Aug 18 11:41 2023-08-01-mario_player.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  43705 Aug 18 11:41 2023-08-02-cloud-workspace-automation.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  22060 Aug 18 11:41 2023-08-03-mario_block.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  11791 Aug 18 11:41 2023-08-03-mario_platform.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  19450 Aug 18 11:41 2023-08-03-mario_tube.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  24387 Aug 18 11:41 2023-08-04-mario_background.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29    695 Aug 18 11:41 2023-08-07-mario_lesson.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  10110 Aug 18 11:41 2023-08-15-java-hello.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  20892 Aug 18 11:41 2023-08-16-github_pages_setup.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  32191 Aug 18 11:41 2023-08-16-linux_shell.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  11466 Aug 18 11:41 2023-08-16-python_hello.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29   9425 Aug 18 11:41 2023-08-23-github_pages_anatomy.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  22668 Aug 18 11:41 2023-08-23-java-console_games.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29   9038 Aug 18 11:41 2023-08-23-python_tricks.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  10152 Aug 18 11:41 2023-08-30-javascript_top_10.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29   9689 Aug 18 11:41 2023-08-30-showcase-S1-pair.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29   7192 Aug 18 11:41 2023-09-05-python-flask-anatomy.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  22157 Aug 18 11:41 2023-09-06-AWS-deployment.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  14380 Aug 18 11:41 2023-09-06-java-primitives.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  11671 Aug 18 11:41 2023-09-06-javascript-input.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  13706 Aug 18 11:41 2023-09-12-java_menu_class.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29   9562 Aug 18 11:41 2023-09-13-java_fibonaccii_class.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  44217 Aug 18 11:41 2023-09-13-javascript_output.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  43423 Aug 18 11:41 2023-09-13-python-pandas_intro.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  11578 Aug 18 11:41 2023-09-20-java-image_2D.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  26739 Aug 18 11:41 2023-09-20-javascript_motion_dog.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  13599 Aug 18 11:41 2023-10-02-java-spring-anatomy.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  12429 Aug 18 11:41 2023-10-09-java-chatgpt.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  15632 Aug 18 11:41 2023-10-09-javascript_api.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29 113091 Aug 18 11:41 2023-10-09-python_machine_learing_fitness.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  16271 Aug 18 11:41 2023-11-13-jwt-python-flask.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  15951 Aug 18 11:41 2023-11-13-vulnerabilities.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  18328 Aug 18 11:41 2023-11-20-jwt-java-spring-challenge.md
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  10745 Aug 18 11:41 2024-01-04-cockpit-setup.ipynb
    drwxr-xr-x 2 flyinglizard29 flyinglizard29   4096 Aug 18 11:41 files



```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

echo "Look for images in notebooks, print working directory, list files"
cd $notebooks/images  # this should exist per fastpages
pwd
ls -l
```

    Look for images in notebooks, print working directory, list files
    /home/flyinglizard29/vscode/student/_notebooks
    total 56
    -rw-r--r-- 1 flyinglizard29 flyinglizard29 34652 Aug 22 09:52 2023-08-16-linux_shell.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  5390 Aug 22 09:04 2023-08-17-AP-pseudo-vs-python.ipynb
    -rw-r--r-- 1 flyinglizard29 flyinglizard29  8557 Aug 22 09:05 2023-08-21-VSCode-GitHub_Pages.ipynb


    bash: line 6: cd: /images: No such file or directory


### Look inside a Markdown File
> "cat" reads data from the file and gives its content as output


```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

echo "Navigate to project, then navigate to area wwhere files were cloned"

cd $project
echo "show the contents of README.md"
echo ""

cat README.md  # show contents of file, in this case markdown
echo ""
echo "end of README.md"

```

    Navigate to project, then navigate to area wwhere files were cloned
    show the contents of README.md
    
    ## Teacher Blog site
    This site is intended for the development of Teacher content.  This blogging site is built using GitHub Pages [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).
    - The purpose is to build lessons and distribute across different Computer Science sections (CSSE, CSP, CSA), a pathway that covers 3 years of High School Instruction.
    - The primary languages and frameworks that are taught are `JavaScript/HTML/CSS`, `Python/Flask`, `Java/Spring`.  Read below for more details.
    - In this course, Teacher content is not exclusively developed by Teachers.  In fact, many Students have been invited to develop and publish content into this repository.  Their names will appear as authors on the content which they aided in producing.
    - This site has incorporated ideas and has radically modified scripts from the now deprecated [fastpages](https://github.com/fastai/fastpages) repository.
    - This site includes assistance and guideance from ChatGPT, [chat.openai.com](https://chat.openai.com/) 
    
    ### Courses and Pathway
    The focus of the Del Norte Computer Science three-year pathway is `Full Stack Web Development`.  This focus provides a variety of technologies and exposures.  The intention of the pathway is breadth and exposure.
    - `JavaScript` documents are focused on frontend development and for entry class into the Del Norte Computer Science pathway.  JavaScript documents and materials are a prerequisites to Python and Java classes.
    - `Python` documents are focused on backend development and requirements for the AP Computer Science Principles exam.
    - `Java` documents are focused on backend development and requirements for the AP Computer Sciene A exam.
    - `Data Structures` materials embedded into JavaScript, Python, or Java documents are focused on college course articulation.
    
    ### Resources and Instruction
    The materials, such as this README, as well as `Tools`, `DevOps`, and `Collaboration` resources are integral part of this course and Computer Science in general.  Everything in our environment is part of our learning of Computer Science. 
    - `Visual Studio Code` is key the code-build-debug cycle editor used in this course, [VSCode download](https://code.visualstudio.com/).  This is an example of a resource, but inside of it it has features for collaboration.
    - `Tech Talks`, aka lectures, are intended to be interactive and utilize `Jupyter Notebooks` and Websites.  This is an example of blending instruction and tools together, which in turn provide additional resources for learning.  For instance, deep knowledge on  GitHub Pages and Notebooks are valuable in understanding principles behind Full Stack Development and Data Science. 
    
    ## GitHub Pages
    All `GitHub Pages` websites are managed on GitHub infrastructure. GitHub uses `Jekyll` to tranform your content into static websites and blogs. Each time we change files in GitHub it initiates a GitHub Action that rebuilds and publishes the site with Jekyll.  
    - GitHub Pages is powered by: [Jekyll](https://jekyllrb.com/).
    - Publised teacher website: [nighthawkcoders.github.io/teacher](https://nighthawkcoders.github.io/teacher/)
    
    ## Preparing a Preview Site 
    In all development, it is recommended to test your code before deployment.  The GitHub Pages development process is optimized by testing your development on your local machine, prior to files on GitHub
    
    Development Cycle. For GitHub pages, the tooling described below will create a development cycle  `make-code-save-preview`.  In the development cycle, it is a requirement to preview work locally, prior to doing a VSCode `commit` to git.
    
    Deployment Cycle.  In the deplopyment cycle, `sync-github-action-review`, it is a requirement to complete the development cycle prior to doing a VSCode `sync`.  The sync triggers github repository update.  The action starts the jekyll build to publish the website.  Any step can have errors and will require you to do a review.
    
    ### WSL and/or Ubuntu installation requirements
    - The result of these step is Ubuntu tools to run preview server.  These procedures were created using [jekyllrb.com](https://jekyllrb.com/docs/installation/ubuntu/)
    ```bash
    # Ubuntu requirements
    #
    echo "=== Install Ruby ==="
    # sudo apt install. installs packages for Ubuntu
    sudo apt install ruby-full build-essential zlib1g-dev -y
    # the following "echo" commands adds gems installation directory into the .bashrc file, avoiding root requirements
    echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
    #
    echo "=== Install Jekyl ==="
    gem install jekyll bundler
    #
    echo "=== Install Conda ==="
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh -O /tmp/miniconda.sh
    chmod +x /tmp/miniconda.sh
    /tmp/miniconda.sh -b -p $HOME/miniconda
    # Configure ruby into shell
    # source the .bashrc file or relanuch terminal
    # update conda
    ~/miniconda/bin/conda update -n base -y -c defaults conda
    ~/miniconda/bin/conda install -y -c conda-forge pyyam
    echo "=== Activate Conda  ==="
    source ~/.bashrc
    ```
    
    ### MacOs installation requirements 
    - Ihe result of these step are MacOS tools to run preview server.  These procedures were created using [jekyllrb.com](https://jekyllrb.com/docs/installation/macos/)
    ```bash
    # ruby
    # MacOS commands
    #
    # Install Ruby for MacOS
    brew install chruby ruby-install xz
    ruby-install ruby 3.1.3
    # Configure ruby into shell using .zshrc
    echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
    echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
    echo '# Install Ruby Gems to ~/gems' >> ~/.zshrc
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.zshrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.zshrc
    #
    # install conda for MacOS
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O /tmp/miniconda.sh
    bash /tmp/miniconda.sh -b -p $HOME/miniconda
    #
    # source the .zshrc file or relanuch terminal
    source ~/.zshrc
    #
    # update conda
    conda update -n base -y -c defaults conda
    #
    # Install local build tools
    gem install jekyll bundler
    #
    conda install -y -c conda-forge pyyam
    # install jekyll
    gem install jekyll bundler
    ```
    
    ### Preview
    - The result of these step is server running on: http://0.0.0.0:4100/teacher/.  Regeneration messages will run in terminal on any save.  Press the Enter or Return key in the terminal at any time to enter commands.
    
    - Complete installation
    ```bash
    bundle install
    ```
    - Run Server.  This requires running terminal commands `make`, `make stop`, `make clean`, or `make convert` to manage the running server.  Logging of details will appear in terminal.   A `Makefile` has been created in project to support commands and start processes.
    
        - Start preview server in terminal
        ```bash
        cd ~/vscode/teacher  # my project location, adapt as necessary
        make
        ```
    
        - Terminal output of shows server address. Cmd or Ctl click http location to open preview server in browser. Example Server address message... 
        ```
        Server address: http://0.0.0.0:4100/teacher/
        ```
    
        - Save on ipynb or md activiates "regeneration". Refresh browser to see updates. Example terminal message...
        ```
        Regenerating: 1 file(s) changed at 2023-07-31 06:54:32
            _notebooks/2024-01-04-cockpit-setup.ipynb
        ```
    
        - Terminal message are generated from background processes.  Click return or enter to obtain prompt and use terminal as needed for other tasks.  Alway return to root of project `cd ~/vscode/teacher` for all "make" actions. 
            
    
        - Stop preview server, but leave constructed files in project for your review.
        ```bash
        make stop
        ```
    
        - Stop server and "clean" constructed files, best choice when renaming files to eliminate potential duplicates in constructed files.
        ```bash
        make clean
        ```
    
        - Test notebook conversions, best choice to see if IPYNB conversion is acting up.
        ```bash
        make convert
        ```
        
    
    end of README.md


### Env, Git and GitHub
> Env(ironment) is used to capture things like path to Code or Home directory.  Git and GitHub is NOT Only used to exchange code between individuals, it is often used to exchange code through servers, in our case deployment for Website.   All tools we use have a behind the scenes hav relationship with the system they run on (MacOS, Windows, Linus) or a relationship with servers which they are connected to (ie GitHub).  There is an "env" command in bash.  There are environment files and setting files (.git/config) for Git.  They both use a key/value concept.

- "env" show setting for your shell
- "git clone" sets up a director of files
- "cd $project" allows user to move inside that directory of files
- ".git" is a hidden directory that is used by git to establish relationship between machine and the git server on GitHub.  


```python
%%script bash

# This command has no dependencies

echo "Show the shell environment variables, key on left of equal value on right"
echo ""

env
```

    Show the shell environment variables, key on left of equal value on right
    
    SHELL=/bin/bash
    PYTHONUNBUFFERED=1
    WSL2_GUI_APPS_ENABLED=1
    WSL_DISTRO_NAME=Ubuntu
    ELECTRON_RUN_AS_NODE=1
    VSCODE_AMD_ENTRYPOINT=vs/workbench/api/node/extensionHostProcess
    NAME=LAPTOP-E9QKSBIA
    PWD=/home/flyinglizard29/vscode/student/_notebooks
    LOGNAME=flyinglizard29
    PYDEVD_IPYTHON_COMPATIBLE_DEBUGGING=1
    HOME=/home/flyinglizard29
    LANG=C.UTF-8
    WSL_INTEROP=/run/WSL/11950_interop
    LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
    WAYLAND_DISPLAY=wayland-0
    CLICOLOR=1
    VSCODE_L10N_BUNDLE_LOCATION=
    LESSCLOSE=/usr/bin/lesspipe %s %s
    VSCODE_HANDLES_SIGPIPE=true
    TERM=xterm-color
    LESSOPEN=| /usr/bin/lesspipe %s
    USER=flyinglizard29
    GIT_PAGER=cat
    PYTHONIOENCODING=utf-8
    DISPLAY=:0
    SHLVL=1
    PAGER=cat
    VSCODE_CWD=/mnt/c/Users/derri/AppData/Local/Programs/Microsoft VS Code
    MPLBACKEND=module://matplotlib_inline.backend_inline
    XDG_RUNTIME_DIR=/run/user/1000/
    WSLENV=VSCODE_WSL_EXT_LOCATION/up
    VSCODE_WSL_EXT_LOCATION=/mnt/c/Users/derri/.vscode/extensions/ms-vscode-remote.remote-wsl-0.81.0
    XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
    PATH=/bin:/home/flyinglizard29/.local/bin:/home/flyinglizard29/.vscode-server/bin/6c3e3dba23e8fadc360aed75ce363ba185c49794/bin/remote-cli:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Program Files (x86)/Common Files/Oracle/Java/javapath:/mnt/c/windows/system32:/mnt/c/windows:/mnt/c/windows/System32/Wbem:/mnt/c/windows/System32/WindowsPowerShell/v1.0/:/mnt/c/windows/System32/OpenSSH/:/mnt/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/mnt/c/Program Files/NVIDIA Corporation/NVIDIA NvDLISR:/mnt/c/Program Files/Git/cmd:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/Docker/Docker/resources/bin:/mnt/d/derri/Anaconda2/Anaconda2:/mnt/d/derri/Anaconda2/Anaconda2/Scripts:/mnt/d/derri/Anaconda2/Anaconda2/Library/bin:/mnt/c/Users/derri/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/derri/AppData/Local/Programs/Microsoft VS Code/bin:/snap/bin:/home/flyinglizard29/.vscode-server/bin/6c3e3dba23e8fadc360aed75ce363ba185c49794/bin/remote-cli:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Program Files (x86)/Common Files/Oracle/Java/javapath:/mnt/c/windows/system32:/mnt/c/windows:/mnt/c/windows/System32/Wbem:/mnt/c/windows/System32/WindowsPowerShell/v1.0/:/mnt/c/windows/System32/OpenSSH/:/mnt/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/mnt/c/Program Files/NVIDIA Corporation/NVIDIA NvDLISR:/mnt/c/Program Files/Git/cmd:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/Docker/Docker/resources/bin:/mnt/d/derri/Anaconda2/Anaconda2:/mnt/d/derri/Anaconda2/Anaconda2/Scripts:/mnt/d/derri/Anaconda2/Anaconda2/Library/bin:/mnt/c/Users/derri/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/derri/AppData/Local/Programs/Microsoft VS Code/bin:/snap/bin
    DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
    VSCODE_NLS_CONFIG={"locale":"en","osLocale":"en","availableLanguages":{}}
    HOSTTYPE=x86_64
    PULSE_SERVER=unix:/mnt/wslg/PulseServer
    VSCODE_HANDLES_UNCAUGHT_ERRORS=true
    VSCODE_IPC_HOOK_CLI=/run/user/1000/vscode-ipc-aab45a60-c9ff-42d7-83bf-d95fdfe4e1f6.sock
    _=/bin/env



```python
%%script bash

# Extract saved variables
source /tmp/variables.sh

cd $project

echo ""
echo "show the secrets of .git"
cd .git
ls -l

echo ""
echo "look at config file"
cat config
```

    
    show the secrets of .git
    total 52
    -rw-r--r-- 1 flyinglizard29 flyinglizard29    21 Aug 18 11:41 HEAD
    drwxr-xr-x 2 flyinglizard29 flyinglizard29  4096 Aug 18 11:41 branches
    -rw-r--r-- 1 flyinglizard29 flyinglizard29   267 Aug 18 11:41 config
    -rw-r--r-- 1 flyinglizard29 flyinglizard29    73 Aug 18 11:41 description
    drwxr-xr-x 2 flyinglizard29 flyinglizard29  4096 Aug 18 11:41 hooks
    -rw-r--r-- 1 flyinglizard29 flyinglizard29 11606 Aug 18 11:41 index
    drwxr-xr-x 2 flyinglizard29 flyinglizard29  4096 Aug 18 11:41 info
    drwxr-xr-x 3 flyinglizard29 flyinglizard29  4096 Aug 18 11:41 logs
    drwxr-xr-x 4 flyinglizard29 flyinglizard29  4096 Aug 18 11:41 objects
    -rw-r--r-- 1 flyinglizard29 flyinglizard29   112 Aug 18 11:41 packed-refs
    drwxr-xr-x 5 flyinglizard29 flyinglizard29  4096 Aug 18 11:41 refs
    
    look at config file
    [core]
    	repositoryformatversion = 0
    	filemode = true
    	bare = false
    	logallrefupdates = true
    [remote "origin"]
    	url = https://github.com/nighthawkcoders/teacher.git
    	fetch = +refs/heads/*:refs/remotes/origin/*
    [branch "main"]
    	remote = origin
    	merge = refs/heads/main


### Student Request - Make a file in Bash
> This example was requested by a student (Jun Lim, CSA). The request was to make jupyer file using bash, I adapted the request to markdown.  This type of thought will have great extrapolation to coding and possibilities of using List, Arrays, or APIs to build user interfaces.  JavaScript is a language where building HTML is very common.

> To get more interesting output from terminal, this will require using something like mdless (https://github.com/ttscoff/mdless).  This enables see markdown in rendered format.
- On Desktop [Install PKG from MacPorts](https://www.macports.org/install.php)
- In Terminal on MacOS
    - [Install ncurses](https://ports.macports.org/port/ncurses/)
    - ```gem install mdless```
    
> Output of the example is much nicer in "jupyter"


```python
%%script bash

# This example has error in VSCode, it run best on Jupyter
cd /tmp

file="sample.md"
if [ -f "$file" ]; then
    rm $file
fi

tee -a $file >/dev/null <<EOF
# Show Generated Markdown
This introductory paragraph and this line and the title above are generated using tee with the standard input (<<) redirection operator.
- This bulleted element is still part of the tee body.
EOF

echo "- This bulleted element and lines below are generated using echo with standard output (>>) redirection operator." >> $file
echo "- The list definition, as is, is using space to seperate lines.  Thus the use of commas and hyphens in output." >> $file
actions=("ls,list-directory" "cd,change-directory" "pwd,present-working-directory" "if-then-fi,test-condition" "env,bash-environment-variables" "cat,view-file-contents" "tee,write-to-output" "echo,display-content-of-string" "echo_text_>\$file,write-content-to-file" "echo_text_>>\$file,append-content-to-file")
for action in ${actions[@]}; do  # for loop is very similar to other language, though [@], semi-colon, do are new
  action=${action//-/ }  # convert dash to space
  action=${action//,/: } # convert comma to colon
  action=${action//_text_/ \"sample text\" } # convert _text_ to sample text, note escape character \ to avoid "" having meaning
  echo "    - ${action//-/ }" >> $file  # echo is redirected to file with >>
done

echo ""
echo "File listing and status"
ls -l $file # list file
wc $file   # show words
mdless $file  # this requires installation, but renders markown from terminal

rm $file  # clean up termporary file
```

    
    File listing and status
    -rw-r--r-- 1 flyinglizard29 flyinglizard29 809 Aug 22 09:53 sample.md
     15 132 809 sample.md


    bash: line 30: mdless: command not found


## Hack Preparation.
> Review Tool Setup Procedures and think about some thing you could verify through a Shell notebook.
- Come up with your own student view of this procedure to show your tools are installed.
- Name and create notes on some Linux commands you will use frequently.
- Is there anything we use to verify tools we install? Review versions checks.
- Is there anything we could verify with Anaconda?  or WSL?  
- How would you update a repository?  Could you do that in script above?

```
Installing Ubuntu: 
sudo apt update
sudo apt upgrade -y

Finding Ubuntu Version:
lsb_release -a

Getting Github Info:
git config --global --get <user.name>
git config --global --get <user.email>

# User.name is your name in github while user.email is your email that you used to sign in into github.

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
```
