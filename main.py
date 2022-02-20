# === IMPORT MODULES === #
import os, typing, argparse,sys

def git_ignore_scan()-> list:
    global ignore
    gitIgnore = False
    if ".gitignore" in os.listdir(PARENT_DIR):gitIgnore = True
    if gitIgnore:
        with open(f"{PARENT_DIR}/.gitignore",'r') as f:ignore = f.read().splitlines()
    return ignore

# === GET TODOS === #
def todos(folder: str) -> str:
    # === TO GET ALL THE FILES FROM A PATH === #
    def _(path: str) -> list:
        files = [file for root,dirs,file in os.walk(path)]
        files = [x for x in files[0] if x not in ignore]
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
    print(list(files.keys()))
    for i in list(files.keys()):
        fancyReturn += f"Path: {i[len(c)+1:]}\n\t{n.join(files[i])}\n"

    return fancyReturn

# === SHELL === #
def shell(command: str) -> typing.Any:
    global PARENT_DIR 
    global exit_
    # === CHANGE DIRECTORY === #
    if command.lower().startswith("cd"):
        if len((x := command.strip().split())) == 1: return "The path has not been supplied"
        elif len(x) > 2: return "Extra arguments passed"
        elif not os.path.isdir(x[1]): return "Cannot find the path specified"

        # === TO CHECK IF THE PATH SPECIFIED GOES BEYOND PARENT_DIR === #
        if PARENT_DIR not in os.path.abspath(x[1]):
            print("Path specified goes beyond the parent directory")
            return

        os.chdir(x[1])
    
    # === GET TODOS === #
    elif command.lower().startswith("todos"):
        if len(command.strip().split()) > 1: return "Extra arguments passed"
        return todos(os.getcwd())

    # === COMMIT MESSAGE === #
    elif command.lower().startswith("git"):
        # === KEEP THE CURRENT PATH === #
        cur_path = os.getcwd()

        # === CHANGE PATH TO PARENT DIRECTORY === #
        os.chdir(PARENT_DIR)

        # === IF THE COMMAND IS A COMMIT === #
        if command.lower().startswith("git commit -m"):
            # === COMMIT FORMATTING === #
            b = "\""
            commit = command.split(f"{b}")
            commit[1] = f'{os.path.basename(os.getcwd())}: {command.split(f"{b}")[1]}'

            # === RUN COMMAND === #
            os.system("\"".join(commit))
            
            # === EXIT FUNCTION === #
            return
        
        # === RUN THE GIT COMMAND SPECIFIED BY USER === #
        os.system(command)
        os.chdir(cur_path)
        
    # === HELP === #
    elif command.lower().startswith("help"):
        return """
Command: cd
    Usage: cd <path>
    Used to change the current working directory

Command: todos
    Usage: todos
    Used to get all the ToDos from monorepos/monorepo

Command: exit
    Usage: exit
    To exit the shell

You can use this shell as if you are using your terminal.
Any other command is executed by your default shell
"""

    # === TO EXIT === #     
    elif command.lower().startswith("exit") :
        exit_ = True

    else: os.system(command)

if __name__ == "__main__":
    # === SETUP ARGPARSE === #
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path',
        metavar='path/to/monorepo',
        type=str,
        nargs='+',
        help='Input monorepo path to monoinit'
    )

    # === GET ARGUMENTS === #
    args = parser.parse_args()

    # === IF THE PATH DOESN'T EXIST === #
    if not os.path.isdir(args.path[0]):sys.exit("Path not recognized")
    # === TO CHECK IF THE DIRECTORY CONTAINS MONOREPOS === #
    elif "workflow.json" not in os.listdir(args.path[0]):sys.exit("The path specified doesn't have a workflow.json file")

    # === CHANGE DIRECTORY TO THE PATH === #
    os.chdir(args.path[0])

    # === SAVE THE PATH TO PARENT DIR === #
    PARENT_DIR = os.getcwd()
    
    # === IF THIS TURNS TRUE, THE SCRIPT STOPS === #
    exit_ = False
    git_ignore_scan()

    while not exit_:
        # === GET AND PRINT OUTPUT === #
        print('\x1b[1;32;40m' + os.path.basename(os.getcwd()) + '\x1b[0m',end=" ")
        output = shell(input("\x1b[1;33;40m>\x1b[6;34;40m>\x1b[6;35;40m>\x1b[0m"))
        if output is None: continue
        else: print(output)
