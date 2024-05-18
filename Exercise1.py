num1 = [1,2,'moon',3,'fruit']
num2 = [4,5,'sun',6,'appel']
new_num = dict()
for i in range(len(num1)):
    new_num.update({num1[i]:num2[i]})
print(new_num)
     

