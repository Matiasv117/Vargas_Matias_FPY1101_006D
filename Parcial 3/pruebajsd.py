import csv
with open('sas.csv', 'w') as file:
    escritor = csv.writer(file)
escritor.writerow(['codigo','nombre','cantidad','precio'])