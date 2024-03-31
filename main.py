from file_oraganizer import File_Organizer
from evaluator import Evaluator
from result_printer import Result_Printer

def main() :
    names = File_Organizer.run()
    eval_result = Evaluator.run(names);
    Result_Printer.run(eval_result);

main()