def fibonacci(n):
    """this function returns nth fibonacci series"""
    
    if n == 0 or n == 1:
        return n
    return fibonacci( n - 1 ) + fibonacci( n - 2 )

#Taking input in form of list
lst=list(map(int,input("Enter List of Number: ").split(",")))
j = 0
i = 0

#Runniing while loop which runs till the input list ends
while j <= ( len( lst ) - 1 ):

    if fibonacci( i ) == lst[ j ]:  # condition to check wether jth element is in fibonacci series by checking single elements 
        print( lst[ j ], "is valid")
        print()
        i = 0 #take i = 0 to start fibonacci series from 0 again
        j += 1 #iterate j to check next element of list


    elif fibonacci( i ) < lst[ j ]:   #if jth element of list is not in fibonacci series and less than j
        i += 1  #iterate i to check next fibonacci number
    
        
    else:
        print( lst[ j ], "is invalid" )
        print()
        j += 1
        i = 0