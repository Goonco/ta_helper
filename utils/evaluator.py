import subprocess
import glob
import sys

from utils.common import SRC_PATH, y_or_n_input

class Evaluator :
    def __init__(self, names):
        self.ignore_space = self.check_ignore_space() # execute_solution에서 ignore_space 확인하므로 필히 먼저 실행!
        self.essentials = self.check_essentials()
        self.forbiddens = self.check_forbiddens()

        self.names = names
        self.solution = self.execute_solution()
        self.evaluations = None

    def run(self) :
        self.evaluate();
        return self.evaluations

    def evaluate(self) :
        self.evaluations = []
        for name in self.names :
            exec_res = self.execute_script(name)
            self.evaluations.append({ 'name' : name, 'result' : exec_res})
    
    def execute_solution(self) :
        solution_file = glob.glob(SRC_PATH['solution'])

        if len(solution_file) == 0 :
            print(f"solution.py 파일이 존재하지 않습니다. 자세한 내용은 ReadMe를 확인해 주세요.")
            sys.exit(-1)
        
        exec_result = subprocess.run(['python', solution_file[0]], capture_output=True, shell=True, text=True)
        return self.space_filter(exec_result)
    
    def execute_script(self, name) :
        path = glob.glob(SRC_PATH['target'](name))

        if len(path) == 1 :
            exec_result = subprocess.run(['python', path[0]], capture_output=True, shell=True, text=True)
            return self.compare_to_solution(self.space_filter(exec_result), path[0])
        elif len(path) == 0 :
            return (False, "미제출")
        else :
            return (False, "동일한 이름 한개 이상 존재")
        
    def compare_to_solution(self, exec_result, path) :
        if self.solution != exec_result : return (False, "출력 결과 오류")

        with open(path, "r", encoding="utf-8") as file:
            file_str = file.read()
        
            for forbidden in self.forbiddens :
                if len(forbidden) != 0 and (forbidden in file_str) : return (False, f"금지어 {forbidden} 존재")
        
            for essential in self.essentials :
                if len(essential) != 0 and (essential not in file_str) : return (False, f"필수어 {essential} 없음")

        return (True, "")
        
    def check_ignore_space (self) :
        return y_or_n_input("채점 시 띄어쓰기를 무시하시겠습니까?")
    
    def check_essentials (self) :
        return input("[필수1,필수2,...] 필수어를 입력해주세요. (없으면 Enter) ").split(',')
    
    def check_forbiddens (self) :
        return input("[금지1,금지2,...] 금지어를 입력해주세요. (없으면 Enter) ").split(',')
        
    def space_filter(self, exec_result) :
        if self.ignore_space : 
            return exec_result.stdout.replace(" ", "")
        else :
            return exec_result.stdout