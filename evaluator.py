import subprocess
import glob
import sys


def target_path(name) :
    return "target/*{}*.py".format(name)

SRC_PATH = {
    'names' : 'src/names.txt',
    'solution' : 'src/solution.py',
    'target' : target_path
}

def read_names():
    try :
        names = []
        with open(SRC_PATH['names'], 'r', encoding='utf-8') as f:
            for name in f :
                names.append(name.strip())
        return names
    
    except FileNotFoundError :
        print(f"name.txt 파일이 존재하지 않습니다. 자세한 내용은 ReadMe를 확인해 주세요.")
        sys.exit(-1)

def execute_solution() :
    solution_file = glob.glob(SRC_PATH['solution'])

    if len(solution_file) == 0 :
        print(f"solution.py 파일이 존재하지 않습니다. 자세한 내용은 ReadMe를 확인해 주세요.")
        sys.exit(-1)
    
    solution = subprocess.run(['python', solution_file[0]], capture_output=True, shell=True, text=True)
    return solution.stdout

class Evaluator :
    def __init__(self) :
        self.names = read_names();
        self.sol_string = execute_solution();
    
    def execute_script(self, name) :
        path = glob.glob(SRC_PATH['target'](name))

        if len(path) == 1 :
            solution = subprocess.run(['python', path[0]], capture_output=True, shell=True, text=True)
            if self.sol_string == solution.stdout :
                return (True, "")
            else :
                return (False, "출력 결과 오류")
        elif len(path) == 0 :
            return (False, "미제출")
        else :
            return (False, "동일한 이름 한개 이상 존재")

    def evaluate(self) :
        evaluation = []
        for name in self.names :
            exec_res = self.execute_script(name)
            evaluation.append({ 'name' : name, 'result' : exec_res})
        return evaluation