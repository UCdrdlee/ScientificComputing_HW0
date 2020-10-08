"""
fizzbuzz

Write a python script which prints the numbers from 1 to 100,
but for multiples of 3 print "fizz" instead of the number,
for multiples of 5 print "buzz" instead of the number,
and for multiples of both 3 and 5 print "fizzbuzz" instead of the number.
"""
# for each integer from 1 to 100,
for i in range(1,101):
    # check if the integer is divisible by both 3 and 5. And if so, print "fizzbuzz"
    if (i%3==0)&(i%5==0):
        print('fizzbuzz')
    # if the above condition is not met check if it is divisible by either 3 or 5.
    # If so, print 'fizz' or 'buzz', respectively.
    elif (i%3==0):
        print('fizz')
    elif (i%5==0):
        print('buzz')
    # if the integer is divisible neither by these numbers, print the integer value.
    else:
        print(i)
