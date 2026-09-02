print ('put in 5 of your grades')
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())

total = s1 + s2 + s3 + s4 + s5
avg = int (total / 5)

valid_range = range(0, 101)

if avg not in valid_range:
    print ('what')

elif avg in range (90, 101):
    print ('good job on all As')

elif avg in range (80, 89):
    print ('nice average')

elif avg in range (60, 79):
    print ('pretty good')

elif avg in range (40, 59):
    print ('need a tutor')

elif avg in range (0, 39):
    print ('oof')

