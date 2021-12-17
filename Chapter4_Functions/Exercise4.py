# If input is dibizible by 3 return "Fizz"
# If input is dibizible by 5 return "Buzz"
# If input is dibizible by 3 and 5 return "FizzBuzz"
# If if input is nor divizible by 3 or 5 will return the number itself

def fizzbuzz(number):
    message = ""
    if not int(number) % 3:
        message += "Fizz"
    if not int(number) % 5:
        message += "Buzz"
    if (int(number) % 3) and (int(number) % 5):
        message = number
    return message


number = input("introduceti un numar:")
print(fizzbuzz(number))
