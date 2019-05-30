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
    if result.is_integer()==True:
        return int(result)
    return round(result, 10)

# вызов расчетных шункций
def call (numb_1=0.0):
    while True: # для выполнения бесконечного количества раз

        operation = input()   # пользователь вводит операцию по формуле (numb_1 + numb_2) или (+ numb_2); разделение пробелом обязательно

        if operation == "clear": # если была нажата кнопка очистить, то возвращаемся в самое начало, а начальное значение становится равным нулю
            numb_1 = 0
            print(numb_1)
            continue

        operation_split = operation.split() # создается новый массив, который был получен путём разделения строки operation через пробел

        if len(operation_split)==1:
            operation_split.append("")

        #вызов сложения
        if operation_split[0] == "+" or operation_split[1] == "+": # узнается, какую операцию хотел произвести пользователь
            if operation_split[0] == "+":  # если пользователь ввел строку operation по формуле + numb_2 , то вызывается функция от имеющегося в памяти значения numb_1 (по умолчанию numb_1==0 ) и введенного numb_2
                numb_1= addition (numb_1, float(operation_split[1]))
            else:
                numb_1= addition (float(operation_split[0]), float(operation_split[2])) # иначе, вызывается функция от введенных numb_1 и numb_2

        #вызов вычитания
        elif operation_split[0] == "-" or operation_split[1] == "-":
            if operation_split[0] == "-":
                numb_1= subtraction (numb_1, float(operation_split[1]))
            else:
                numb_1= subtraction (float(operation_split[0]), float(operation_split[2]))

        #вызов вычитания
        elif operation_split[0] == "-" or operation_split[1] == "-":
            if operation_split[0] == "-":
                numb_1= subtraction (numb_1, float(operation_split[1]))
            else:
                numb_1= subtraction (float(operation_split[0]), float(operation_split[2]))

        #вызов умножения
        elif operation_split[0] == "*" or operation_split[1] == "*":
            if operation_split[0] == "*":
                numb_1= multiplication (numb_1, float(operation_split[1]))
            else:
                numb_1= multiplication (float(operation_split[0]), float(operation_split[2]))

        #вызов деления
        elif operation_split[0] == "/" or operation_split[1] == "/":
            if operation_split[0] == "/":
                numb_1= division (numb_1, float(operation_split[1]))
            else:
                numb_1= division (float(operation_split[0]), float(operation_split[2]))

        #вызов факториала
        elif operation_split[0] == "!" or operation_split[1] == "!":
            if operation_split[0] == "!":
                numb_1= float (factorial (numb_1))
            else:
                numb_1= float (factorial (float(operation_split[0])))

        numb_1=rounding (numb_1)
        print(numb_1)



call()
