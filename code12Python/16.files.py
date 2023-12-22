# f = open('sample.txt','r')
# data =  f.read(5)
# print(data)
# f.close()

# #write file
# f = open('sample.txt','w')
# f.write("ok sorry")
# f.close()

#with 
with open('sample.txt','r') as f:
    a  = f.read()
with open('sample.txt','w') as f:
    a = f.write("me")
print(a)        