MESSAGES = {
    'heading1' : "### 채점 결과 ♪(^∇^\*)",
    'cl' : "\n<br/>\n",
    'tableheader' : "|   학번   | 결과 |   비고    |\n| :------: | :--: | :-------: |",
    'heading2' : '### 오답자 확인 (っ °Д °;)っ'
}

class Result_Printer :
    __result_file = None
    __eval_results = None
    __solution = None
    __fail_results = None

    @staticmethod
    def run(evaluator) :
        Result_Printer.__eval_results = evaluator.evaluations
        Result_Printer.__fail_results = evaluator.fail_results
        Result_Printer.__solution = evaluator.solution
        
        Result_Printer.__result_file = open("result.md", "w", encoding="utf-8")
        Result_Printer._generate_result()
        Result_Printer._generate_fail()
        Result_Printer.__result_file.close()

    @staticmethod
    def _generate_result() :
        Result_Printer._printOnFile(MESSAGES["heading1"])
        Result_Printer._printOnFile(MESSAGES["cl"])
        Result_Printer._printOnFile(MESSAGES["tableheader"])
        
        for res in Result_Printer.__eval_results :
            Result_Printer._printOnFile(Result_Printer._generateResultRow(res))

    @staticmethod
    def _generate_fail() :
        Result_Printer._printOnFile(MESSAGES["cl"])
        Result_Printer._printOnFile(MESSAGES['heading2'])
        Result_Printer._printOnFile(MESSAGES["cl"])

        for res in Result_Printer.__fail_results :
            Result_Printer._printOnFile(Result_Printer._generateFailRow(res))

    @staticmethod
    def _printOnFile(str) :
        print(str, file=Result_Printer.__result_file)

    @staticmethod
    def _generateResultRow(result) :
        res_row = "|{}".format(result['id'])
        correct, reason = result['result'];
        
        if correct :
            res_row += "|✅|"
        else :
            res_row += "|⛔|{}|".format(reason)
        return res_row
    
    @staticmethod
    def _generateFailRow(result) :
        res_row = f"\n* {result['id']}"
        res_row += f"\n```\n{result['result']}```"
        return res_row