MESSAGES = {
    'heading' : "### 채점 결과 ♪(^∇^\*)",
    'cl' : "<br/>\n",
    'tableheader' : "|   학번   |  성명  | 결과 |   비고    |\n| :------: | :----: | :--: | :-------: |"
}

class Result_Printer :
    def __init__(self, results) :
        self.file = open("result.md", "w", encoding="utf-8")
        self.results = results

    def generate_result(self) :
        self.printOnFile(MESSAGES["heading"])
        self.printOnFile(MESSAGES["cl"])
        self.printOnFile(MESSAGES["tableheader"])
        
        for res in self.results :
            self.printOnFile(self.printResultRow(res))

        self.file.close()

    def printOnFile(self, str) :
        print(str, file=self.file)

    def printResultRow(self, result) :
        res_row = "|{}|{}".format('20191599', result['name'])
        correct, reason = result['result'];
        
        if correct :
            res_row += "|✅|"
        else :
            res_row += "|⛔|{}|".format(reason)
        return res_row