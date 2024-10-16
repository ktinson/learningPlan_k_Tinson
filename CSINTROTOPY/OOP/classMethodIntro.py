import random
class Personality:
    # def __init__(self):
     #self.personalities = [works] when not using class method
    personalities = ["INTJ"," ESTJ", "ENTJ", "ESFJ", "ENFJ", "ISTJ", "ISFJ", "INFJ", "ESTP", "ESFP", "ENTP", "ENFP", "ISTP", "ISFP", "INTP", "INFP"]
    @classmethod
    def sort(cls, name):#cls is class, we are using the varibale to refer to the class in the function
        #def sort(cls,name)
        print(name, "has the personality type", random.choice(cls.personalities))
        #random.choice(self.personalities)
#personality = Personality()
Personality.sort("Bob")
