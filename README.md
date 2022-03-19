# MonoInit Documentation
Monorepo initialiser for hackarmour written in python.

## Getting Started
You need `git`, `wget` and `python3` to use monoinit.

This script is expected to be ran only on *NIX systems. If you're on windows, please use Windows Subsystem for Linux.

Use the following command to get monoinit in your project:
```bash
wget https://raw.githubusercontent.com/hackarmour/monoinit/main/main.py -O monoinit.py
```

Launch the monoinit shell using the following command:
```bash
python3 monoinit.py
```

Meant to be shipped with each monorepo (This script is standalone) for better tooling. Expects a file called `workflow.json` at the root of monorepo. This file has config for different commands the shell can run. Here's an example config:

```json
{
    "socket": {
        "folder": "py1",
        "run": "python3 main.py",
        "test": "python3 test.py"
    },
    "client": {
        "folder": "py2",
        "install": "pip install --upgrade -r requirements.txt",
        "run": "python3 main.py"
    }
}
```

Here `socket` and `client` are the names of repos inside the monorepo. The goal of this file to let monoinit know all the common commands these projects have. For instance, when `run` command is ran at the root of the monorepo, monoinit searches for `run` in all of the repos, executes them together and aggregates the outputs and shows them all together. There's no point of running the command when the shell is inside one of the repo folders.

## Commands
MonoInit is like the default `/bin/sh` except it has some more commands to help you with managing your /monorepo.

- `init`
    This command will initialise an empty repo. 

- `newcommand`
    Used to create a new command in a repo.

- `rmcommand`
    Used to remove a command from a repo.

- `update`
    This will update monoinit to the latest version.

- `todos`
    This command will go through all the files in the current working directory and list all the todos.

- `exit`
    This command is used to exit the monoinit shell.

Apart from these commands, you can use all the other commands on your machine.

## Features
- Commit message formatting: When commiting changes to upstream by switching into a repo, monoinit will format the commit as
```bash
monorepo ❯❯❯ cd repo1
repo1 ❯❯❯ git commit -m "changes" // this will be formatted as "repo1: changes"
```

- git log: Running `git log` will output a beautified git log graph.

___

## Screenshot of the shell
![image](https://user-images.githubusercontent.com/83999665/158515493-0278ffd6-45c2-47f4-9073-184cc68d99b5.png)


### Team

- Project Lead - [@ujjwal-kr](https://github.com/ujjwal-kr)
- Devs - [@mrHola21](https://github.com/mrHola21), [@TheEmperor342](https://github.com/TheEmperor342)
