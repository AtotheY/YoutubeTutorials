def fizzBuzz(num):
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            print 'fizzbuzz'
        elif i % 3 == 0:
            print 'fizz'
        elif i % 5 == 0:
            print 'buzz'
        else:
            print i

num = 150
fizzBuzz(num)