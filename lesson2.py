print('ex. 1')
n = int(input('Input number: '))
if n % 2 == 0:
    print('четное')
else:
    print('нечетное')

###################################################################
print('ex. 2')
day = input('Какой сегодня день? ')
if day == 'суббота' or day == 'воскресенье':
    print('Сегодня выходной!')
elif day == 'среда':
    print('Мне снгодня к стоматологу в 15.30')
elif day in ['понедельник', 'вторник', 'четверг', 'пятница']:
    print('Сегодня будний день')
else:
    print('Incorrect data')

######################################################################
print('ex. 3')
n = int(input('Input number value: '))
text = input('Input str value: ')
for _ in range(n):
    print(text)

######################################################################
print('ex. 4')
message = input()
cnt = 0
for i in range(len(message)):
    if message[i] in 'уеыаоэяиюё':
        cnt += 1
print(cnt)

######################################################################
print('ex. 5')
num = int(input())
sum = 0
while num >= 0:
    sum += num
    num = int(input())
print(sum)