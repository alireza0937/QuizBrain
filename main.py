from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = list()


for a in range (len(question_data)) :

    question_text = question_data[a]['text']
    question_answer = question_data[a]["answer"]
    new_object = Question(question_text, question_answer)
    question_bank.append(new_object)


quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()
quiz_brain.still_has_question()

while quiz_brain.still_has_question() :
    quiz_brain.next_question()
