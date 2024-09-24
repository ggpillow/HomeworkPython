array_boys = ["Martin", "Nikolay", "Denis", "Peter", "Kail", "Pol", "Artur"]
array_girls = ["Anna", "Nari", "Mary", "Olga", "Lena", "Rianna", "Beyonce"]
count = 0

if len(array_boys) == len(array_girls):
    array_boys.sort()
    array_girls.sort()

    for partner_boy in range(len(array_boys)):
        for partner_girl in range(1):
            print(array_boys[partner_boy], "и", array_girls[partner_girl + count])
            count += 1
else:
    print("Внимание, кто-то может остаться без пары.")