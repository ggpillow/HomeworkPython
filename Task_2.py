array_boys = ["Martin", "Nikolay", "Denis", "Peter", "Kail", "Pol", "Artur"]
array_girls = ["Anna", "Nari", "Mary", "Olga", "Lena", "Rianna", "Beyonce"]
count = 0


if len(array_boys) == len(array_girls):
    array_boys.sort()
    array_girls.sort()

    for boy, girl in zip(array_boys, array_girls):
        print(boy, "и", girl)
else:
    print("Внимание, кто-то может остаться без пары.")