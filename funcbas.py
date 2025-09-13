def cal(c,d):
    return [c + d, c - d, c * d, c / d]

# c = add(2,6)

# list = [
#     [1, 8, 1],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(list[0].count(list[0][0]))

# a, b = 1,2

# print (c[0])

def runCode():
    def takeInput():
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        return a, b

    while True:
        i ,j = takeInput()
        c = cal(i, j)
        print("Results: ", c)
        if 0 in c:
            print("Exiting the program.")
            break
    
