from utils.user_input import User_Input
from utils.file_organizer import File_Organizer
from utils.evaluator import Evaluator
from utils.result_printer import Result_Printer

def main() :
    inputs = User_Input()
    file_organizer = File_Organizer(inputs.delete_file_flag, inputs.total_problem, inputs.target_problem)
    ids = file_organizer.run()

    evaluator = Evaluator(ids, inputs);
    Result_Printer.run(evaluator);

    inputs.check_feedback_id()
    if inputs.feedback_id_flag : file_organizer.feedback_ids(ids)

main()