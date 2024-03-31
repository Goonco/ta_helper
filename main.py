from file_oraganizer import File_Organizer
from evaluator import Evaluator
from result_printer import Result_Printer

def main() :
    names = File_Organizer.run()
    ev = Evaluator(names);
    rp = Result_Printer(results=ev.evaluate());
    rp.generate_result();

main()