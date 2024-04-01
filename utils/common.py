SRC_PATH = {
    'names' : 'src/names.txt',
    'solution' : 'src/solution.py',
    'target': lambda name: f"target/*{name}*.py",
}

def y_or_n_input (str) :
    while True :
        check_ignore_space = input(f"[Y/N] {str} ").lower()
        if check_ignore_space == 'y' : return True
        elif check_ignore_space == 'n' : return False