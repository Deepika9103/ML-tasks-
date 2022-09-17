class Titandex:
    def __init__(self,name,height,strength):
        self.name=name
        self.height=height
        self.strength=strength
        self.winning_streak=winning_streak
        print("The intial winning streak is",self.winning_streak)

    def TitanvsScout(self,name1,strength2):
        self.name1=name1
        self.strength2=strength2
        if(self.strength==self.strength2):
            self.winning_streak=0
            print("its a draw")
            print(f"the new winning streak of {self.name} is {self.winning_streak}")
        elif(self.strength>self.strength2):
            print("Titan wins")
            self.winning_streak+=1
            winning_streak==self.winning_streak
            print(f"the new winning streak of {self.name} is {self.winning_streak}")
        else:
            self.winning_streak=0
            print("Scouts wins")
            print(f"the new winning streak of {self.name} is {self.winning_streak}")

    def TitanvsTitan(self,name2,strength3):
        self.name2=name2
        self.strength3=strength3

        if(self.name.lower()==self.name2.lower()):
            print("Titan cannot play with itself")
        elif (self.name!=self.name2 and self.strength==self.strength3):
            self.winning_streak=0
            print("Draw")
            print(f"the new winning streak of {self.name} is {self.winning_streak}")
        elif(self.name!=self.name2 and self.strength>self.strength3):
            print("Titan1 wins")
            self.winning_streak+=1
            print(f"the new winning streak of {self.name} is {self.winning_streak}")
        elif(self.name!=self.name2 and self.strength<self.strength3):
            print("Titan2 wins")
            self.winning_streak=0
            print(f"the new winning streak of {self.name} is {self.winning_streak}")

name=input("Enter the name of the Titan ")
strength=int(input("Enter the strength of the Titan "))
height=int(input("Enter the height of the Titan "))
winning_streak=0
round1=Titandex(name,height,strength)
i=0
while(i!=3):
    print('Select from the options below')
    print('1.Scout')
    print('2.Titan')
    print('3.Quit')
    n=int(input("Enter your choice"))
    if(n==1):
        name1=input("Enter the name of the Scout ")
        strength2=int(input("Enter the strength of the Scout "))
        round1.TitanvsScout(name1,strength2)
    elif(n==2):
        name2=input("Enter the name of the Titan ")
        strength3=int(input("Enter the strength of the Titan "))
        ws=0
        round1.TitanvsTitan(name2,strength3)
    elif(n==3):
        break
    else:
        continue


        



