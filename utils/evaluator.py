import subprocess
import glob
import sys
import time

from utils.common import SRC_PATH

class Evaluator :
    def __init__(self, ids, ignore_space_flag, essentials, forbiddens, inputs ):
        self.inputs = inputs

        self.ignore_space_flag = ignore_space_flag
        self.essentials = essentials
        self.forbiddens = forbiddens

        self.ids = ids
        self.solution = self.execute_solution()
        self.evaluations = None

        self.time_out = 5

    def run(self) :
        self.evaluate();
        return self.evaluations

    def evaluate(self) :
        self.evaluations = []
        for id in self.ids :
            exec_res = self.execute_script(id)
            self.evaluations.append({ 'id' : id, 'result' : exec_res})
    
    def execute_solution(self) :
        solution_file = glob.glob(SRC_PATH['solution'])

        if len(solution_file) == 0 :
            print(f"solution.py 파일이 존재하지 않습니다. 자세한 내용은 ReadMe를 확인해 주세요.")
            sys.exit(-1)
        
        exec_result = subprocess.run(['python', solution_file[0]], input=self.inputs, capture_output=True, shell=True, text=True)
        return self.space_filter(exec_result.stdout)
    
    def execute_script(self, id) :
        path = glob.glob(SRC_PATH['target'](id))

        if len(path) == 1 :
            process = subprocess.Popen(['python', path[0]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            for inp in self.inputs :
                process.stdin.write(inp)
            process.stdin.close()
            start_time = time.time()

            force_break_flag = False
            while True :
                return_code = process.poll()
                if return_code is not None : 
                    break
                if time.time() - start_time > self.time_out: 
                    process.terminate()
                    force_break_flag = True
                    break
                time.sleep(1)
            
            if force_break_flag : return (False, "시간 초과")
            exec_result, _ = process.communicate()

            return self.compare_to_solution(self.space_filter(exec_result), path[0])
        elif len(path) == 0 :
            return (False, "미제출")
        else :
            return (False, "동일한 id의 파일이 한개 이상 존재")
        
    def compare_to_solution(self, exec_result, path) :
        if self.solution != exec_result : return (False, "출력 결과 오류")

        with open(path, "r", encoding="utf-8") as file:
            file_str = file.read()
        
            for forbidden in self.forbiddens :
                if len(forbidden) != 0 and (forbidden in file_str) : return (False, f"금지어 {forbidden} 존재")
        
            for essential in self.essentials :
                if len(essential) != 0 and (essential not in file_str) : return (False, f"필수어 {essential} 없음")

        return (True, "")
        
    def space_filter(self, exec_result) :
        if self.ignore_space_flag : 
            return exec_result.replace(" ", "")
        else :
            return exec_result