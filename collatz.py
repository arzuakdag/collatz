# Create the collatz() function with input validation


def collatz(): 
    print("What is your choice of number?")


    try: 
        number = int(input())
        print(number)
    except ValueError: 
        print("You need to use an integer!") #outcome if input value is NOT an integer 

    while number !=1: 
        print("Moving on to next calculation.")
        if number % 2 == 0: 
            number = number // 2 
            print("//2") #calculation applied to even value 
            print(number)
        elif number % 2 == 1: 
            number = 3 * number + 1
            print("3 * number + 1") #calculation applied to odd value
            print(number)
        else: 
            break #equivalent to outcome of calculation equals 1 

collatz()