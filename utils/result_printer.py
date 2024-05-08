MESSAGES = {
    'heading1' : "### 채점 결과 ♪(^∇^\*)",
    'cl' : "\n<br/>\n",
    'tableheader' : "",
    'heading2' : '### 오답자 확인 (っ °Д °;)っ',
    'heading3' : lambda num: f"#### {num}차 채점",
}

class Result_Printer :
    __result_file = None
    __eval_results = None
    __solution = None
    __fail_results = None

    __max_iteration = None
    __cur_iter = None

    @staticmethod
    def run(evaluator) :
        Result_Printer.__max_iteration = evaluator.max_iteration
        Result_Printer._generate_tableheader();

        Result_Printer.__eval_results = evaluator.evaluations
        Result_Printer.__fail_results = evaluator.fail_results
        Result_Printer.__solution = evaluator.solution
        
        Result_Printer.__result_file = open("result.md", "w", encoding="utf-8")
        Result_Printer._generate_result()
        Result_Printer._generate_fail()
        Result_Printer.__result_file.close()

    @staticmethod
    def _generate_tableheader() :
        MESSAGES["tableheader"] += "|   학번   |"
        res = ""
        about = ""
        line = "\n| :--: |"
        for i in range(Result_Printer.__max_iteration) :
            res += f"결과#{i+1} |"
            about += f"비고#{i+1} |"
            line += " :--: | :--: |"
        MESSAGES["tableheader"] += res + about + line;

    @staticmethod
    def _generate_result() :
        Result_Printer._printOnFile(MESSAGES["heading1"])
        Result_Printer._printOnFile(MESSAGES["cl"])
        Result_Printer._printOnFile(MESSAGES["tableheader"])
        
        for idx in range(len(Result_Printer.__eval_results[0])) :
            Result_Printer._printOnFile(Result_Printer._generateResultRow(idx))

    @staticmethod
    def _generateResultRow(studentIdx) :
        res_row = f"|{Result_Printer.__eval_results[0][studentIdx]['id']}|"

        saveCorrect = ""
        saveReason = ""
        for iter in range(Result_Printer.__max_iteration) :
            correct, reason = Result_Printer.__eval_results[iter][studentIdx]['result'];
            
            if correct : 
                saveCorrect += "✅|"
                saveReason += " |"
            else : 
                saveCorrect += "⛔|"
                saveReason += f"{reason}|"
        
        return res_row + saveCorrect + saveReason

    @staticmethod
    def _generate_fail() :
        Result_Printer._printOnFile(MESSAGES["cl"])
        Result_Printer._printOnFile(MESSAGES['heading2'])
        Result_Printer._printOnFile(MESSAGES["cl"])
        
        for iter in range(Result_Printer.__max_iteration) :
            Result_Printer._printOnFile(MESSAGES["cl"])
            Result_Printer._printOnFile(MESSAGES['heading3'](iter + 1))
            Result_Printer._printOnFile(MESSAGES["cl"])

            Result_Printer._printOnFile(Result_Printer._generateFailRow({
                'id' : "solution",
                'result' : Result_Printer.__solution[iter]
            }))
            for res in Result_Printer.__fail_results[iter] :
                Result_Printer._printOnFile(Result_Printer._generateFailRow(res))

    @staticmethod
    def _printOnFile(str) :
        print(str, file=Result_Printer.__result_file)
    
    @staticmethod
    def _generateFailRow(result) :
        res_row = f"\n* {result['id']}"
        res_row += f"\n\n```\n{result['result']}```"
        return res_row