class KBC:
    """
    A class to represent a KBC (quiz) question.

    Attributes:
        question (str): The question text.
        optiona (str): Option A.
        optionb (str): Option B.
        optionc (str): Option C.
        optiond (str): Option D.
        correctoption (str): The correct option (A/B/C/D).
    """

    def __init__(self, question, optiona, optionb, optionc, optiond, correctoption):
        """
        Initialize the KBC question with options and correct answer.

        Args:
            question (str): The question text.
            optiona (str): Option A.
            optionb (str): Option B.
            optionc (str): Option C.
            optiond (str): Option D.
            correctoption (str): The correct option (A/B/C/D).
        """
        self.question = question
        self.optiona = optiona
        self.optionb = optionb
        self.optionc = optionc
        self.optiond = optiond
        self.correctoption = correctoption.upper()

    def display_question(self):
        """
        Returns the formatted question and options.

        Returns:
            str: The question and its options.
        """
        return (
            f"Q: {self.question}\n"
            f"A: {self.optiona}\n"
            f"B: {self.optionb}\n"
            f"C: {self.optionc}\n"
            f"D: {self.optiond}"
        )

# List of KBC questions
questions = [
    KBC("What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", "B"),
    KBC("What is the capital of USA?", "New York", "Washington DC", "Los Angeles", "Chicago", "C"),
    KBC("Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", "B"),
]

# Quiz loop
for idx, question in enumerate(questions, start=1):
    print(f"\nQuestion {idx}:")
    print(question.display_question())
    answer = input("Enter Your Option (A/B/C/D): ").upper()
    if answer == question.correctoption:
        print("Correct Answer")
    else:
        print("Wrong Answer")
        break





