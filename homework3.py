          # 1st program
line1 = 'возведение числа 9 в степень 0.5, после умножение на 5 ='
print(line1,(9**0.5)*5)
          # 2nd program
print('результат логического выражения (99.9 > 99.8) and (1000 != 1000.1):', (99.9 > 99.8) and (1000 != 1000.1))
          # 3rd program
line3 = 'сумма серединных чисел от исходных данных 1234 и 5678 ='
number3 = (1234//10) % 100 + (5678//10) % 100
print(line3, number3)
          # 4th program
numb1 = 13.42
numb2 = 42.13
numb1i = int(numb1)  # целая часть первого числа
numb1f = round((numb1 % 1), 2)*100  # round, чтобы округлить до двух цифр после запятой
numb1f = int(numb1f)  # дробная часть первого числа
numb2i = int(numb2)  # целая часть второго числа
numb2f = round((numb2-numb2i), 2)*100
numb2f =int(numb2f)  # дробная часть второго числа
print(numb1i, ' ', numb1f, ' ', numb2i, ' ', numb2f)
line4 = '(numb1i == numb2f) or (numb1f == numb2i)'
print('составляем логическое выражение',line4,'и получаем результат:',(numb1i == numb2f) or (numb1f == numb2i))