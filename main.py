# === IMPORT MODULES === #
import os, typing

exit_ = False

# === GET TODOS === #
def todos(folder: str) -> str:

    # === TO GET ALL THE FILES FROM A PATH === #
    def _(path: str) -> list:
        files = []
        for i in os.listdir(path):
            if os.path.isdir(os.path.join(path, i)): files += _(os.path.join(path, i))
            elif (
                i.endswith(".py")       or
                i.endswith(".html")     or
                i.endswith(".js")       or
                i.endswith(".mjs")      or
                i.endswith(".ejs")      or
                i.endswith(".tsx")      or
                i.endswith(".ts")       or
                i.endswith(".jsx")      or
                i.endswith(".css")
            ): files.append(os.path.join(path, i))
        return files

    files, c = {}, os.getcwd()
    for i in _(folder):
        with open(i, 'r') as f:
            for lineNo, item in enumerate(f.readlines()):
                if not ("TODO" in item): continue

                if i not in list(files.keys()):
                    files[i] = [f"{lineNo+1}. | {item}"]
                else:
                    files[i].append(f"{lineNo+1}. | {item}")

    fancyReturn = ""

    n = "\n\t"
    for i in list(files.keys()):
        fancyReturn += f"Path: {i[len(c)+1:]}\n\t{n.join(files[i])}"
    return fancyReturn

# === SHELL === #
def shell(command: str) -> typing.Any:

    # === CHANGE DIRECTORY === #
    if command.startswith("cd"):
        if len((x := command.strip().split())) == 1: return "The path has not been supplied"
        elif len(x) > 2: return "Extra arguments passed"
        elif not os.path.isdir(x[1]): return "Cannot find the path specified"
        os.chdir(x[1])
    
    # === GET TODOS === #
    elif command.startswith("todos"):
        if len(command.strip().split()) > 1: return "Extra arguments passed"
        return todos(os.getcwd())

    # === COMMIT MESSAGE === #
    elif command.startswith("git commit -m"):
        b = "\""
        commit = f'{os.path.basename(os.getcwd())}: {command.split(f"{b}")[1]}'
        os.system(f'git commit -m \"{commit}\"')
        
    # === TO EXIT === #
    elif command.startswith("exit"):
        global exit_
        exit_ = True

    else: os.system(command)

if __name__ == "__main__":
    while not exit_:
        output = shell(input(f"◆ {os.getcwd()} ❯❯❯ "))
        if output is None: continue
        else: print(output)
