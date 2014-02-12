# Git

## Presentation

In software development, is a distributed version control and source code management
(SCM) system with an emphasis on speed.
I use git for all my project including this [website](https://github.com/maggick/my_website).
I use it in command line with [tig](https://github.com/jonas/tig)


## Merge two different repository

if you have two differents repositry (first and second) to merge in one even in local :

we create a new git repository ans make an initial commit :

    mkdir newRepository
    git init
    touch .gitignore
    git add .gitignore
    git commit .gitignore -m 'init'

we fetch and merge the first

    git remote add first pathTo/first
    git fetch first
    git merge first/master

we fetch and merge the second

    git remote add second pathTo/second
    git fetch second
    git merge second/master
