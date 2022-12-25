#Вычислить число c заданной точностью d

n = 1
number_pi = 0
while n < 1000000:
    elem_pi = ((1/n)-(1/(n+2)))*4
    number_pi = number_pi + elem_pi
    n = n+4
print(number_pi)

def accuracy_pi(d:str):
    str_sp = d.split('.')
    str_spfin = len(str_sp[-1])
    return str_spfin
print(round(number_pi, accuracy_pi('0.001')))