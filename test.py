# f1 = input("Choose the first number: ")
# f2 = input("Choose the second number: ")

f1, f2 = 1, 1
sequence = [[f1,f2]]
count = 1

#Rows
for numbers in range(0,3):
    #columns
    # count = 2
    for items in range(0,numbers+1):
        new_element = [f1,-f2]
        sequence.append(new_element)
        count+=1
        print(sequence)
        
  
