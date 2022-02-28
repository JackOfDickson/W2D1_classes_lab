class Student:
    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort
#Creating methods
    def talk(self):
        return "I can talk!"
    def say_favourite_language(self, fav_language):
        return f'I love {fav_language}'
