import csv
with open('visit_log.csv', mode='r', encoding = 'utf-8') as infile, \
    open('funnel.csv', mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    writer.writerow(['user_id', 'source', 'category'])
    
    for row in reader:
        user_id, source = row
        
        if source == 'other':
            category = 'Продукты'
        elif source == 'context':
            category = 'Электроника'
        elif source == 'email':
            category = 'Одежда'
        else:
            category = ''
        
        if category:
            writer.writerow([user_id, source, category])