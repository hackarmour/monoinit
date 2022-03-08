# MonoInit

Monorepo initialiser for hackarmour written in python.

## How to use

- Make sure to have python3 installed.
- Clone the repo.
- run `python3 main.py` and follow the instructions.
- You can get a list of all the commands by typing `help` in the shell.

Meant to be shipped with each monorepo (main.py is standalone) for better tooling. Expects a file called `workflow.json` at the root of monorepo. The file has config for different commands the shell can run. Here's an example config:

```json
{
    "nodeServer": {
        "folder": "nodeServer",
        "install": "npm i",
        "run": "npm run start",
        "test": "npm run test"
    },
    "todoClient": {
        "folder": "todoClient",
        "install": "npm i",
        "run": "npm run start",
        "build": "npm run build && npm export"
    },
    "goServer": {
        "folder": "goServer",
        "run": "go run",
        "build": "go build",
        "test": "go test",
        "install": "go mod vendor"
    }
}
```

Here `nodeServer`, `todoClient`, `goServer` are the names of repos inside the monorepo. The goal of this file to let monoinit know all the common commands all these projects has. For instance, when `run` command is ran at the root of the monorepo, monoinit searches for `run` in all of the repos, executes them together and aggregates the outputs and shows them all together. There's no point of running the command when the shell is inside one of the repo folders.

## Screenshot of the shell
![image](https://cdn.discordapp.com/attachments/840914901462810654/947486773821444106/unknown.png)


### Team

- Project Lead - [@ujjwal-kr](https://github.com/ujjwal-kr)
- Devs - [@mrHola21](https://github.com/mrHola21), [@TheEmperor342](https://github.com/TheEmperor342)
