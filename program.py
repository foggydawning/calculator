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

#возведение в заданную степень
def vozvedenie_n(numb_1, numb_2):
    result = numb_1 ** numb_2
    return result

#в озведенние в квадрат
def vozvedenie_2(numb_1):
    result = numb_1 ** 2
    return result

# возведенние в куб
def vozvedenie_3(numb_1):
    result = numb_1 ** 3
    return result

# синус числа
def sin(numb_1):
    import math
    result = math.sin(numb_1)
    return result

# косинус числа
def cos(numb_1):
    import math
    result = math.cos(numb_1)
    return result

# тангенс числа
def tang(numb_1):
    import math
    result = math.tan(numb_1)
    return result

# котангенс числа
def ctang(numb_1):
    import math
    result = math.cos(numb_1) / math.sin(numb_1)
    return result

# квадратный корень числа
def sqrt(numb_1):
    import math
    result = math.sqrt(numb_1)
    return result

#n-ый корень числа
def sqrt_n(numb_1, numb_2):
    result = numb_1 ** (1 / numb_2)
    return result

# округление числа
def rounding (result):
    if result.is_integer()==Treue:
        return int(result)
    return round(result, 10)        
