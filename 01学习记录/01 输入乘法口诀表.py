from tkinter import N


for item in range(1, 10):
    a=1
    while a <= item:
        print(a,"*", item, "=", a*item,end='\t')
        a += 1
    print('')
