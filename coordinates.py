import csv
import haversine as hs

miestas1=input("Input city name: ")
x1=float(input("Input latitude: "))
y1=float(input("Input longitude: "))



with open('cities.csv', 'r', newline='', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csvfile)
    rows = list(csv_reader)
    print(rows)

l=[]
for i in rows:

    miestas=i[0]
    x=(i[1].replace('(', '').replace(')', '').split(','))[0]
    x=float(x)
    y=(i[1].replace('(', '').replace(')', '').split(','))[1]
    y=float(y)
    cordinate_1 = (x, y)
    cordinate_2 = (x1, y1)
    z = round(hs.haversine(cordinate_1, cordinate_2),2)
    print(f'The distance between {miestas} and {miestas1} is {z} km')
    dictas={"miestas":miestas, "atstumas": z}
    l.append(dictas)


minatstumas = min(l, key=lambda x:x['atstumas'])
print(f'Arciausiai - {minatstumas} km')