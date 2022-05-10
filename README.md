# MonoInit Documentation
Monorepo initialiser for hackarmour written in python.

## Getting Started
You need `git`, `wget`, `python3` and [tmux](https://github.com/tmux/tmux/wiki) to use monoinit.

[Here](https://tmuxcheatsheet.com/) is the tmux cheatsheet.

This script is expected to run only on *NIX systems. If you're on windows, please use Windows Subsystem for Linux.

Use the following command to get monoinit in your project:
```bash
wget https://raw.githubusercontent.com/hackarmour/monoinit/main/main.py -O ~/.local/bin/monoinit.py
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
        "hook": "lint"
    }
}
```

Here `socket` and `client` are the names of repos inside the monorepo. The goal of this file to let monoinit know all the common commands these projects have. For instance, when `run` command is ran at the root of the monorepo, monoinit searches for `run` in all of the repos, executes them together and aggregates the outputs and shows them all together. There's no point of running the command when the shell is inside one of the repo folders. The `hook` field is optional and is not a command, it is executed each time when you run `git add` anywhere in the project.

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

## Other Features
- git log: Running `git log` will output a beautified git log graph.

![image](https://user-images.githubusercontent.com/83999665/159155974-a5bf031b-3948-4759-93e4-2b5f1a32d144.png)

___

### Team

- Project Lead - [@ujjwal-kr](https://github.com/ujjwal-kr)
- Devs - [@TheEmperor342](https://github.com/TheEmperor342), [@mrHola21](https://github.com/mrHola21)
