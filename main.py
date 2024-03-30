import subprocess
import glob

def execute_script(script_path) : 
    paths = glob.glob('target/' + script_path)

    if len(paths) == 1 :
        solution = subprocess.run(['python', glob.glob('target/' + script_path)], capture_output=True, shell=True, text=True)
        return solution.stdout
    elif len(paths) == 0 :
        print("사람 없어요")
        return -1
    else:
        print("사람 여러명이요")
        return -1

def read_names():
    try :
        names = []
        with open('names.txt', 'r', encoding='utf-8') as f:
            for name in f :
                names.append(name.strip())
        return names
    
    except FileNotFoundError :
        print(f"Error: File name not found.")
        return False

def main() :
    solution = subprocess.run(['python', 'solution.py'], capture_output=True, shell=True, text=True).stdout

    names = read_names()    
    for name in names :
        result = execute_script("*{}*.py".format(name))
        if solution == result :
            print(f"{name} : O)")
        else :
            print(f"{name} : X)")
            print(result)


# ======================

main()