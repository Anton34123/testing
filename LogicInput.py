import Core


def test(correct_answers: dict):
    scores = 0

    for answer in correct_answers:
        if input(answer) == correct_answers[answer]:
            scores += 1

    print(f"Ваши баллы: {scores}.")

