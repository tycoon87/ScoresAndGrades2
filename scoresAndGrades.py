import random
def randomNum():
    random_num = random.randint(60,100)
    return random_num  

for i in range(11):
    n = randomNum()
    if( i == 10):
        print("End of program. Bye")
    elif( n < 69 ):
        print("score: "), +n, ("; your grade is D")
    elif( n < 79 ):
        print("score: "), +n, ("; your grade is C")
    elif ( n < 89):
        print("score: "), +n, ("; your grade is B")
    elif ( n < 101):
        print("score: "), +n, ("; your grade is A")