# сложение
def addition (numb_1, numb_2):
    result=numb_1+numb_2
    return result

# вычитание
def subtraction (numb_1, numb_2):
    result=numb_1-numb_2
    return result

# умножение
def multiplication (numb_1, numb_2):
    result=numb_1*numb_2
    return result

# деление
def division (numb_1, numb_2):
    result=numb_1/numb_2
    return result

# факториал
def factorial (numb_1):
    if numb_1==0:
        return 0
    if numb_1==1:
        return 1
    return numb_1 * factorial(numb_1-1)

# изменение знака числа
def change_sign (numb_1):
    return -(numb_1)

# процент
def persent (numb_1):
    return (numb_1)/100
    
