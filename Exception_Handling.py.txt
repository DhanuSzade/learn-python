try:
    a = int(input('enter the number:'))
    b = int(input('enter the number:'))
    c=a/b
    d=a*b
    e=a+b
    print(c)
    print(d)
    print(e)
except NameError as ex1:
    print('The user have not defined the variable')
except ZeroDivisionError:
    print('please provide number greater than 0')
except Execption as ex:
    print(ex)
else:
    print(c)
    print(d)
    print(e)
