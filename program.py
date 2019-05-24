def addition (numb_1, numb_2):
    result=numb_1+numb_2
    return result

def subtraction (numb_1, numb_2):
    result=numb_1-numb_2
    return result

def multiplication (numb_1, numb_2):
    result=numb_1*numb_2
    return result

def division (numb_1, numb_2):
    result=numb_1/numb_2
    return result

def factorial (numb_1):
    if numb_1==0:
        return 0
    if numb_1==1:
        return 1
    return numb_1 * factorial(numb_1-1)
