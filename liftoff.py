def countdown1():
    for i in range(10,0,-1):
        print(i,end=' ')
    print("lift off")
# countdown1()    

number_list :list[int]=[10,9,8,7,6,5,4,3,2,1]
def countdown2():
    for i in number_list:
        print(i, end=" ")
    print("lift off")
countdown2()        