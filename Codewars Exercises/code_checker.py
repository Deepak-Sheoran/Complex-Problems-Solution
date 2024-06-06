class Checker:
    def __init__(self, function, answer):
        self.function = function
        self.answer = answer

    def check(self):
        if self.function == self.answer:
            return "Right Answer"
        else:
            return "Wrong Answer"
