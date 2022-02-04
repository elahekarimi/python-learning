from data import QUESTIONS_data
from question_model import Question
from quize_brain import QuizeBrain

question_bank = []
for questions in QUESTIONS_data:
    questions_text = questions["text"]
    questions_answer = questions["text"]
    new_question = Question(questions_text, questions_answer)
    question_bank.append(new_question)

quiz = QuizeBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()