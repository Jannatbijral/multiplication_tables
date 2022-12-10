#program to print mutiplication tables
n=int(input("enter the no."))
for i in range(2,n+1):
    for j in range(1, 11):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
    print('==============')
