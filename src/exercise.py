def main():
    #write your code below this line
    number1 = int(input())
    number2 = int(input())
    if(number1>number2):
        print(f"{number1} is greater than {number2}.")
    elif(number2>number1):
        print(f"{number1} is smaller than {number2}.")
    else:
        print(f"{number1} is equal to {number2}.")

if __name__ == '__main__':
    main()
