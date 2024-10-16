import random
class Personality:
    def __init__(self):
        self.personalities = ["INTJ"," ESTJ", "ENTJ", "ESFJ", "ENFJ", "ISTJ", "ISFJ", "INFJ", "ESTP", "ESFP", "ENTP", "ENFP", "ISTP", "ISFP", "INTP", "INFP"]
    def sort(self, name):
        print(name, "has the personality type", random.choice(self.personalities))
personality = Personality()
personality.sort("Bob")