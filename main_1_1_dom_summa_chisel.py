# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

a = input('Введите число ')
dlinaChislo = len(a)
summa = 0
for i in range(dlinaChislo):
    summa = summa + int(a[i])
print(summa)



