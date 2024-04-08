import sys
import glob
import os

from utils.common import SRC_PATH

class File_Organizer :
    def __init__(self, delete_file_flag, total_problem, target_problem) :
        self.ids = []
        self.delete_file_flag = delete_file_flag
        self.total_problem = total_problem
        self.target_problem = target_problem

    def run(self) :
        self._read_ids()
        if self.delete_file_flag :
            for id in self.ids :
                self._organize(id)
        
        return self.ids
        
    def _organize(self,id) :
        paths = glob.glob(SRC_PATH['target'](id))
        p_len = len(paths)

        selection = self.target_problem - 1
        if p_len != 0 and p_len != self.total_problem :
            print(f"{id}를 파일명에 갖는 파일의 수가 {self.total_problem}보다 적거나 많습니다.")

            options = "0. 모두 제외\t"
            for i in range(len(paths)) :
                options += f"{i+1}. {paths[i][7:]}\t"
            print(options)

            selection = int(input("평가할 파일을 선택해 주세요. "))

        for i in range(p_len) :
            if i == selection : continue
            os.remove(paths[i])
    
    def _read_ids(self):
        try :
            with open(SRC_PATH['ids'], 'r', encoding='utf-8') as f:
                for id in f :
                    self.ids.append(id.strip())
        
        except FileNotFoundError :
            print(f"name.txt 파일이 존재하지 않습니다. 자세한 내용은 ReadMe를 확인해 주세요.")
            sys.exit(-1)

    def feedback_ids(self,eval_result) : 
        print(eval_result)
        try :
            with open(SRC_PATH['ids'], 'w', encoding='utf-8') as f:
                for res in eval_result :
                    if not res['result'][0] :
                        print(res['id'], file=f)
        
        except FileNotFoundError :
            print(f"name.txt 파일이 존재하지 않습니다. 자세한 내용은 ReadMe를 확인해 주세요.")
            sys.exit(-1)
