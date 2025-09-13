'''coding'''
'''x=input["enter your coded Chat:"]
for i in range(0,len(x)):
    alpha=x[i]
    count = sum(char.isalpha() for char in i)
    if count == 2:
        i,j =1,2
        alpha[i],alpha[j] = alpha[j],alpha[i]
        print(alpha)
    else:
        print(sorry)'''


st = input("Enter message: ")

words = st.split(" ")

for i in words:
    stnew = []
    print(i)
    if (len(i)>=3):
        a = "hjd"
        b = "jde"
        stnew = [ a + i[1: ] + i[0]+ b]
        print(stnew)
    else:
        stnew = [i[1:]+i[0:]]
        print(stnew)
    print("".join(stnew))
print(words)
coding = True

    