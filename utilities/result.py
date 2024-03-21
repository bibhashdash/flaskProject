from models import BallVector


def print_result(user_input: BallVector, correct_answer: BallVector) -> str:

    if any(val < 0 for val in (user_input.x, user_input.y, correct_answer.x, correct_answer.y)):
        return 'Invalid input please enter only positive values'

    x_difference = abs(user_input.x - correct_answer.x)
    y_difference = abs(user_input.y - correct_answer.y)

    if x_difference == 0 and y_difference == 0:
        return 'That was spot on!'
    elif x_difference <= 100 or y_difference <= 100:
        return 'Ooh! That was close'
    else:
        return 'You need to practice more!'
