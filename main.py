from utils.file_oraganizer import File_Organizer
from utils.evaluator import Evaluator
from utils.result_printer import Result_Printer

def main() :
    names = File_Organizer.run()
    eval_result = Evaluator(names).run();
    Result_Printer.run(eval_result);

main()