import csv


with open('employee.csv', 'r') as f:
    # Creeam un obiect reader care contine date din fisier
    reader = csv.reader(f)

    # for row in reader:
    #     print(row)

    data = list(reader)

    # Primul element din lista sunt numele coloanelor
    print(data[0])

    # Restul elementelor sunt valorile de pe fiecare rand
    print(data[1])


with open('employee.csv', 'a', newline='') as f:
    # Creeam un obiect writer de care ne folosim sa scriem date in csv
    writer = csv.writer(f)

    writer.writerow(['George', 3000])
