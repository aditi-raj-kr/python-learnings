'''coding'''
x=input["enter your coded Chat:"]
for i in range(0,len(x)):
    alpha=x[i]
    count = sum(char.isalpha() for char in i)
    if count == 2:
        i,j =1,2
        alpha[i],alpha[j] = alpha[j],alpha[i]
        print(alpha)
    else:
        print(sorry)

    