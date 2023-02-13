class QuizBrain :
    def __init__(self, q_list) :
        self.question_number = 0
        self.question_list = q_list
        self.score = 0 

    def next_question(self):
        
        Userchoice = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} True / False: ")
        self.check_answer(Userchoice)
        self.question_number += 1
        return self.question_number

    def still_has_question(self) :
        if self.question_number <= len(self.question_list) :
            return True
        else :
            return False

    def check_answer(self, input) :
        if input == self.question_list[self.question_number].answer :
            self.score += 1
            print(self.score)
        else:
            print("Wrong answer...")

        print(f"{self.score}/{self.question_number + 1}")