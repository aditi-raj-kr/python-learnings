class KBC:
    

    def __init__(self, question, optiona , optionb, optionc,optiond, correctoption):
       self.question = question
       self.optiona = optiona        
       self.optionb = optionb
       self.optionc = optionc   
       self.optiond = optiond
       self.correctoption = correctoption
    
    def display_question(self):
        return f"Q: {self.question}\nA: {self.optiona}\nB: {self.optionb}\nC: {self.optionc}\nD: {self.optiond}"
    

        
 

q1= KBC("What is the capital of India?", "Mumbai", "Delhi", " Kolkata ", " Chennai","B")
q2= KBC("What is the capital of USA?", "New York", "Washington DC", " Los Angeles ", " Chicago","C")
q3= KBC("Which planet is known as the Red Planet?", "Venus", "Mars", " Jupiter ", " Saturn","B")

a = [q1, q2, q3]


for i in range(len(a)):
    print(a[i].display_question())
    answer =input("Enter Your Option: ").upper()
    if answer == a[i].correctoption:
        print("Correct Answer")
    else:
        print("Wrong Answer")
        break





