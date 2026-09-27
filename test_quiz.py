import unittest

from quiz import QUESTIONS, ask_question, normalize_answer


class QuizTests(unittest.TestCase):
    def test_questions_have_four_choices_and_valid_keys(self):
        for _, options, correct in QUESTIONS:
            self.assertEqual(len(options), 4)
            self.assertIn(correct, "ABCD")

    def test_answer_validation(self):
        self.assertEqual(normalize_answer(" c "), "C")
        self.assertIsNone(normalize_answer("E"))
        self.assertIsNone(normalize_answer(""))

    def test_invalid_input_is_retried_before_scoring(self):
        responses = iter(["X", "c"])
        messages = []
        score = ask_question(*QUESTIONS[0], input_fn=lambda _: next(responses), output_fn=messages.append)
        self.assertEqual(score, 1)
        self.assertIn("Please enter A, B, C or D.", messages)


if __name__ == "__main__":
    unittest.main()
