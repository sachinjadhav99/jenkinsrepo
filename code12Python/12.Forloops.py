# Fruits= ['Banana','Watermelon','Grapes','Mangoes']

# for items in Fruits:
#     print(items)

# for i in range(10):
#     print(i)
# else: 
#     print("This is inside false")    

# #Break Statment
# for i in range(10):
#     print(i)
#     if i ==5:
#         break
    
# #Coniues Statement
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# #pass Statement
# i= 4
# if i>0:
#     pass
# print("ok")    

# #practice set
# num = int(input("Enter the number"))
# for i in range(1,11):
#     print(str(num)+"X"+str(i)+ "="+ str(i*num))

#pratice set 4 no. even or odd
num = int(input("Enter the number: "))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime") 
else:
    print("This number is not Prime")       

    