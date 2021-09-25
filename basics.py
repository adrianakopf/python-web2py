# -*- coding: utf-8 -*-

#Read and load the two number from web page, then calculate and show the result to the user in the web page.
#To view the results, create a 'View' with the same name of the method in this case: "request_vars". Test the link on the browser

def request_vars():
    num1= 0
    num2 = 0
    total = 0
    if request.post_vars:
        num1 = float(request.post_vars.num1)
        num2 = float(request.post_vars.num2)
        total= num1+num2

        # T translate text in multiple languages
        # Take answer and report back to the user as a popup message
        response.flash = T ("The total is " + str (total))
    return locals()


#import python random library
import random
#create isPrime method/function
def isPrime(num):
    counter = 2
    while counter <num-1:
        if num%counter==0:
            return False
        counter = counter + 1
    return True


#create the randowm_number method/function to test numbers between 3 and 20 and check if is prime or not
def random_number():
    x = random.randint(3,20)
    result = isPrime(x)
    return locals()


#Display message
def helloworld():
    msg = "Hello from the Controller!"
    return locals()
