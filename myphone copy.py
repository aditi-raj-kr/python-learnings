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


userBudget = int(input("Enter your value"))
minimumPrice = 1000000000000
for name in phoneDic:
    if phoneDic[name]["price"] < minimumPrice:
        minimumPrice = phoneDic[name]["price"]
if(userBudget )