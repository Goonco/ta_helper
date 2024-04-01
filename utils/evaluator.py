import subprocess
import glob
import sys

from setting import SRC_PATH

LV = {
    'weak' : 0,
    'normal' : 1,
    'strong' : 2,
}

class Evaluator :
    __solution = ''
    __level = LV['normal']

    @staticmethod    
    def run(names) :
        print('''
0. weak : 띄어쓰기를 모두 제외한 상태에서 정답과 비교
1. default : 정답과 단순 비교
2. strong : 필수어, 금지어 설정 가능
              ''')
        Evaluator.__level = int(input("채점 강도를 선택해주세요 : "))

        Evaluator.__solution = Evaluator._execute_solution()
        return Evaluator._evaluate(names)

    @staticmethod
    def _evaluate(names) :
        evaluation = []
        for name in names :
            exec_res = Evaluator._execute_script(name)
            evaluation.append({ 'name' : name, 'result' : exec_res})
        return evaluation
    
    @staticmethod
    def _execute_solution() :
        solution_file = glob.glob(SRC_PATH['solution'])

        if len(solution_file) == 0 :
            print(f"solution.py 파일이 존재하지 않습니다. 자세한 내용은 ReadMe를 확인해 주세요.")
            sys.exit(-1)
        
        exec_result = subprocess.run(['python', solution_file[0]], capture_output=True, shell=True, text=True)
        return Evaluator._level_filter(exec_result)
    
    @staticmethod
    def _execute_script(name) :
        path = glob.glob(SRC_PATH['target'](name))

        if len(path) == 1 :
            exec_result = subprocess.run(['python', path[0]], capture_output=True, shell=True, text=True)
            if Evaluator.__solution == Evaluator._level_filter(exec_result) :
                return (True, "")
            else :
                return (False, "출력 결과 오류")
        elif len(path) == 0 :
            return (False, "미제출")
        else :
            return (False, "동일한 이름 한개 이상 존재")
        
    @staticmethod
    def _level_filter(exec_result) :
        if Evaluator.__level == LV['weak'] : 
            return exec_result.stdout.replace(" ", "")
        elif Evaluator.__level == LV['normal'] : 
            return exec_result.stdout
        elif Evaluator.__level == LV['strong'] : 
            return exec_result.stdout