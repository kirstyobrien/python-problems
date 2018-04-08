#Kirsty O'Brien
#Ex.5

with open('data/iris.csv') as f:
    for line in f:
        print(line.split(',')[0:4], end='')
