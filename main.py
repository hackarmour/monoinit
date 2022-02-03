# === IMPORT MODULES === #
import os, sys, argparse

# === FIND OUT THE PLATFORM === #
platforms = {
    'linux1': 'Linux',
    'linux2': 'Linux',
    'posix': 'Linux',
    'linux': 'Linux',
    'darwin': 'OS X',
    'win32': 'Windows'
}
if sys.platform not in platforms:
    print("Unsupported Operating System Type")
    exit()
else:
    if platforms[sys.platform] == "Windows":
        pathDiff = "\\"
    else:
        pathDiff = "/"

# === TO GET ALL THE FILES FROM A PATH === #
def _(path):
    files = []
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)): files += _(os.path.join(path, i))
        elif (
            i.endswith(".py")       or
            i.endswith(".html")     or
            i.endswith(".js")       or
            i.endswith(".mjs")      or
            i.endswith(".ejs")      or
            i.endswith(".css")
        ): files.append(os.path.join(path, i))
    return files

# === MAIN COMMAND === #
def monoinit(args) -> str:
    global pathDiff

    # === CHECK IF MONOREPO EXISTS === #
    c = os.getcwd()
    if not args.allFiles:
        if os.path.join(c, args.monorepo) not in \
            [os.path.join(c, o) for o in os.listdir(c) if os.path.isdir(os.path.join(c, o))]:
            return "This monorepo doesn't exist."

    # === TODOS === #
    if args.getTodos:
        todos = {}
        path = c
        
        if args.allFiles: 
            for i in os.listdir(path): todos[i] = {}
        else: todos[args.monorepo] = {}

        for j in _(f"{path}{pathDiff}{args.monorepo if args.monorepo is not None else ''}"):
            with open(j, 'r') as f:
                for lineNo, item in enumerate(f.readlines()):
                    if "TODO" in item:
                        if j not in list(todos.keys()):
                            todos[j[len(c)+1:].split(pathDiff)[0]][j] = [f"{lineNo+1}. | {item}"]
                        else:
                            todos[j[len(c)+1:].split(pathDiff)[0]][j].append(f"{lineNo+1}. | {item}")

        fancyReturn = ""
        newline = "\n\t"
        # print(todos)
        for i in list(todos.keys()):
            fancyReturn += f"MonoRepo: {i}\n"
            for j in list(todos[i].keys()):
                fancyReturn += f"\tFile: {j[len(c)+1:]}\n"
                for k in todos[i][j]:
                    fancyReturn += f"\t\t{k}\n"
        return fancyReturn

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--monorepo", "-m",
        metavar="monorepo",
        help="Choose a monorepo to run the command on",
        required=False
    )
    parser.add_argument(
        "--getTodos", "-gt",
        action='store_true',
        help="Find Todo comments from files in a monorepo and display them",
        default=False
    )
    parser.add_argument(
        "--allFiles", "-a",
        action='store_true',
        help="Run commands in all monorepos",
        default=False
    )

    args = parser.parse_args()
    print(str(monoinit(args)))
