word = input("Введите слово: ")

count = len(word)

if count % 2 != 0:
    number = count // 2
    print(word[number])
else:
    number = count // 2
    print(word[number-1:number+1])
