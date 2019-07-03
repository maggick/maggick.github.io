Title: git tricks
Status: hidden

# Git

## Presentation

Git is a distributed version control and source code management
(SCM) system with an emphasis on speed.
I use git for all my project including this
[website](https://github.com/maggick/maggick.github.io).
I use it in command line with [tig](https://github.com/jonas/tig).


## Merge two different repository

If you have two different repository (first and second) to merge in one even in local:

We create a new git repository ans make an initial commit:

    mkdir newRepository
    git init
    touch .gitignore
    git add .gitignore
    git commit .gitignore -m 'init'

We fetch and merge the first:

    git remote add first pathTo/first
    git fetch first
    git merge first/master

If you have a message like `fatal: refusing to merge unrelated histories` you
need to force git to merge the projects using `--allow-unrelated-histories`.

We fetch and merge the second:

    git remote add second pathTo/second
    git fetch second
    git merge second/master

## Remove unwanted data (passwords) from git history

It append to put unwanted data in a file, and then commit this data to git, in
this case you may want to remove all this data from your history.
To do so, just rewrite the history with the following command:

    git filter-branch --tree-filter 'git ls-files -z "*.py" |xargs -0 perl -p -i -e "s#(PASSWORD1|PASSWORD2)#youPassowrd#g"' -- --all

This command will just change the history of python files and replace
"PASSWORD1" and "PASSWORD2" whit "youPassword".

*WARNING* rewriting history is dangerous, make a backup before doing anything.

