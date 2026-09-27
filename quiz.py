"""English-language general knowledge quiz for the terminal."""

QUESTIONS = [
    ("What is the capital of France?", ("Berlin", "Madrid", "Paris", "Rome"), "C"),
    ("Which planet is known as the Red Planet?", ("Earth", "Mars", "Jupiter", "Venus"), "B"),
    ("Who painted the Mona Lisa?", ("Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"), "C"),
    ("Which animal is known for running at very high speeds on land?", ("Hippo", "Lion", "Cheetah", "Snake"), "C"),
    ("Which civilization built the pyramids of Giza?", ("Egyptians", "Greeks", "Romans", "Mayans"), "A"),
    ("What is the process by which plants make food using sunlight?", ("Photosynthesis", "Respiration", "Transpiration", "Germination"), "A"),
    ("What is Earth's highest mountain above sea level?", ("K2", "Kangchenjunga", "Lhotse", "Mount Everest"), "D"),
    ("What is the chemical symbol for gold?", ("Au", "Ag", "Pb", "Fe"), "A"),
]


def normalize_answer(value):
    """Accept A-D, ignoring surrounding spaces and case; reject other input."""
    answer = value.strip().upper()
    return answer if answer in {"A", "B", "C", "D"} else None


def ask_question(question, options, correct, input_fn=input, output_fn=print):
    output_fn(question)
    for letter, option in zip("ABCD", options):
        output_fn(f"{letter}) {option}")
    while True:
        answer = normalize_answer(input_fn("Your answer (A-D): "))
        if answer is not None:
            break
        output_fn("Please enter A, B, C or D.")
    if answer == correct:
        output_fn("Correct!\n")
        return 1
    output_fn(f"Incorrect. The correct answer was {correct}.\n")
    return 0


def main(input_fn=input, output_fn=print):
    score = sum(ask_question(*item, input_fn=input_fn, output_fn=output_fn) for item in QUESTIONS)
    output_fn(f"Quiz finished! Your final score is: {score}/{len(QUESTIONS)}")
    return score


if __name__ == "__main__":
    main()
