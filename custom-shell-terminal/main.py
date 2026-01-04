import os
import subprocess

def myshell():
    while True:

        cwd = os.getcwd()
        user_input = input("{} $$".format(cwd))

        if not user_input.strip():
            continue

        commands = user_input.split()
        cmd = commands[0]
        args = commands[1:]


        if cmd == "exit":
            break
        elif cmd == "cd":
            try:
                target_dir = args[0] if args else os.path.expanduser("-")
                os.chdir(target_dir)
            except FileNotFoundError:
                print(f"cd- no such file or directory: {args[0]}")


        else:
            try:
                subprocess.run(commands)
            except FileNotFoundError:
                print(f"\"{cmd}\"- command not found")


if __name__ == "__main__":
    myshell()