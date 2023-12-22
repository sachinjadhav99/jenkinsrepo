# n = 0
# product =1
# for i in range(n):
#     product =product*(i+1)
# print(product)

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product *(i+1)
#     return product

# print(factorial_iter(5))        

# #find 3 Greatest Number
# def maximum(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3    
        
# m = maximum(3,4,9)
# print("The value of the maximum is"+ str(m))        

#print *
n = 6
for i in range(n):
    print("*" * (n-i)) 