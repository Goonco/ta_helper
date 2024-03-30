from evaluator import Evaluator
from result_printer import Result_Printer

def main() :
    ev = Evaluator();
    rp = Result_Printer(results=ev.evaluate());
    rp.generate_result();

main()