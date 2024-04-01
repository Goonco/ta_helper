import sys
import glob
import os

from utils.common import SRC_PATH, y_or_n_input

class File_Organizer :
    __names = []
    __total = 0
    __target = 0

    @staticmethod
    def run() :
        gonnaDelete = File_Organizer._get_arguments()

        File_Organizer._read_names()
        if gonnaDelete :
            for name in File_Organizer.__names :
                File_Organizer._organize(name)
        
        return File_Organizer.__names
        
    @staticmethod
    def _organize(name) :
        paths = glob.glob(SRC_PATH['target'](name))
        p_len = len(paths)

        selection = File_Organizer.__target - 1
        if p_len != 0 and p_len != File_Organizer.__total :
            print("\n특정 이름을 가진 파일명이 적거나 많습니다.")

            options = "0. 모두 제외\t"
            for i in range(len(paths)) :
                options += f"{i+1}. {paths[i]}\t"
            print(options)

            selection = int(input("평가할 파일을 선택해 주세요. "))

        for i in range(p_len) :
            if i == selection - 1 : continue
            os.remove(paths[i])
    
    @staticmethod
    def _read_names():
        try :
            with open(SRC_PATH['names'], 'r', encoding='utf-8') as f:
                for name in f :
                    File_Organizer.__names.append(name.strip())
        
        except FileNotFoundError :
            print(f"name.txt 파일이 존재하지 않습니다. 자세한 내용은 ReadMe를 확인해 주세요.")
            sys.exit(-1)

    @staticmethod
    def _get_arguments() :

        gonna_delete = y_or_n_input("과제 파일 정리를 시작하시겠습니까?")
        if not gonna_delete : return False

        File_Organizer.__total = int(input("문제의 총 개수를 입력해 주세요. "))
        File_Organizer.__target = int(input("평가할 문제 번호를 입력해 주세요. "))
        return True

