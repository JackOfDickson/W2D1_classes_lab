class Student:
    def __init__(self, input_name, input_cohort, input_fav_language):
        self.name = input_name
        self.cohort = input_cohort
        self.fav_language = input_fav_language
#Creating methods
    def talk(self):
        print("I can talk!")
    def say_favourite_language(self, fav_language):
        print(f'I love {fav_language}!')
