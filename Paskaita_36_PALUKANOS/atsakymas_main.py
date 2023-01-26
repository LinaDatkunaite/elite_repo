from atsakymas_palukanos import Paskola

paskola = Paskola()
while True:
    try:
        print()
        pasirinkimas = int(input("Pasirinkite veiksmą:\n1 - įvesti paskolos duomenis,\n2 - parodyti paskolos informaciją\n3 - paskaičiuoti paskolos mokėjimo grafiką\n4 - baigti darbą\n"))
        if pasirinkimas == 1:
            paskola.suma = int(input("Įveskite paskolos sumą (eurais)\n"))
            paskola.terminas = int(input("Įveskite paskolos atidavimo terminą (mėnesiais)\n"))
            paskola.palukanos = int(input("Įveskite paskolos palūkanų procentą (pvz., 10)\n"))
        if pasirinkimas == 2:
            paskola.paskolos_informacija()
        if pasirinkimas == 3:
            paskola.mokejimo_grafikas()
        if pasirinkimas == 4:
            print("Programa baigta")
            break
    except:
        print("Neteisingas pasirinkimas")