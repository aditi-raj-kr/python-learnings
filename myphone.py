



# details=list(phoneDic.values())
# minPrice = 100000000
# max=0

# print(details[0])
# for detail in details:
#     print(minPrice)
#     if (minPrice > detail["price"]):
#        minPrice = detail["price"]
#     elif (maxPrice<detail["price"]):
#         maxPrice = detail["price"]
                
# print(minPrice)


def getBudget(mp):
    a = int(input("Enter Your Budget"))
    if mp > a:
       print("sorry But we Dont Have any")
       return getBudget()
    return a

def showProductAccBudget(products, budget):
    for name in products:
        if products[name]["price"] <= budget:
            print(name," ", products[name]["price"])

def getMinPrice(c):
    print(c)
    minValue = c["samsung"]["price"]
    print(minValue)
    for i in c:
        print(i)
        if (c[i]["price"] < minValue) :
            print('i m if')
            minValue = c[i]["price"]
            print(minValue)
    return(minValue)

def runCode():
    phoneDic ={
        "samsung" : {
            "price" : 50000, 
            "piece" : 15
        } , 
        "apple" :{
            "price" : 100000,
            "piece" : 10
        }, 
        "oppo" :{
            "price" : 20000,
            "piece" : 15
        } 
    }

    minValue = getMinPrice(phon eDic)
   # budget = getBudget()
   # showProductAccBudget(phoneDic, budget)
    print(minValue)

runCode()


 