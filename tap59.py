def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
num = input("Eded: ")

num_l = [int(i) for i in str(num)]

print(most_frequent(num_l))