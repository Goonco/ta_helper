SRC_PATH = {
    'ids' : 'src/ids.txt',
    'solution' : 'src/solution.py',
    'target': lambda id: f"target/*{id}*.py",
}

MESSAGES = {
    'check_delete_file' : '과제 파일 정리를 진행하시겠습니까?',
    'get_total_problem' : '문제의 총 개수를 입력해 주세요.',
    'get_target_problem' : '평가할 문제 번호를 입력해 주세요.',

    'check_ignore_space' : '채점 시 띄어쓰기를 무시하겠습니까?',
    'get_essentials' :  '[필수1,필수2,...] 필수어를 입력해주세요. (없으면 Enter) : ',
    'get_forbiddens' : '[금지1,금지2,...] 금지어를 입력해주세요. (없으면 Enter) : ',

    'get_iteration' : '반복 실행 횟수를 입력해주세요.',
    'get_inputs' : lambda iter : f'#{iter} [입력1,입력2,...] 실행 시 입력값을 입력해주세요. (없으면 Enter) : ',

    'check_feedback_id' : '정답 처리된 id를 제외하도록 ids.txt를 업데이트하시겠습니까?'
}