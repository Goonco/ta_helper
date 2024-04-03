MESSAGES = {
    'heading' : "### 채점 결과 ♪(^∇^\*)",
    'cl' : "<br/>\n",
    'tableheader' : "|   학번   | 결과 |   비고    |\n| :------: | :--: | :-------: |"
}

class Result_Printer :
    __result_file = open("result.md", "w", encoding="utf-8")
    __eval_results = ''

    @staticmethod
    def run(eval_results) :
        Result_Printer.__eval_results = eval_results
        Result_Printer._generate_result()

    @staticmethod
    def _generate_result() :
        Result_Printer._printOnFile(MESSAGES["heading"])
        Result_Printer._printOnFile(MESSAGES["cl"])
        Result_Printer._printOnFile(MESSAGES["tableheader"])
        
        for res in Result_Printer.__eval_results :
            Result_Printer._printOnFile(Result_Printer._generateResultRow(res))

        Result_Printer.__result_file.close()

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