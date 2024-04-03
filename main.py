from utils.user_input import User_Input
from utils.file_organizer import File_Organizer
from utils.evaluator import Evaluator
from utils.result_printer import Result_Printer

def main() :
    inputs = User_Input()
    ids = File_Organizer(inputs.delete_file_flag, inputs.total_problem, inputs.target_problem).run()
    eval_result = Evaluator(ids, inputs.ignore_space_flag, inputs.essentials, inputs.forbiddens).run();
    Result_Printer.run(eval_result);

main()