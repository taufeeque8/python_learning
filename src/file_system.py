file = open('resources/application.ini', 'r')
for each in file:
    for chara in each:
        print(chara,end="")
