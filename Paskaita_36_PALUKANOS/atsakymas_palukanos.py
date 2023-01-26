class Paskola:
    def __init__(self):
        self.suma = 0
        self.terminas = 0
        self.palukanos = 0
        self._bendros_palukanos = 0
        self._bendra_suma = 0

    def paskolos_informacija(self):
        print()
        print("Paskolos informacija:")
        print("Suma:", self.suma, "eurų")
        print("Terminas:", self.terminas, "mėnesių")
        print("Palūkanos:", self.palukanos, "procentų")
        if self._bendra_suma != 0:
            print("Bendra palūkanų suma:", round(self._bendros_palukanos, 2), "eurų")
            print("Bendra mokėtina suma:", round(self._bendra_suma, 2), "eurų")
        else:
            print("Bendra palūkanų suma ir bendra mokėtina suma bus atvaizduota tik paskaičiavimus mokėjimo grafiką")

    def mokejimo_grafikas(self):
        grazintina_dalis = self.suma/self.terminas
        bendros_sumoketos_palukanos = 0
        bendra_sumoketa_suma = 0
        likutis = self.suma
        print()
        print("{:<8} {:<8} {:<12} {:<12} {:<8}".format("Mėnuo", "Dalis", "Likutis",
                                                     "Palūkanos", "Suma"))
        for menuo in range(1, self.terminas+1):
            menesio_palukanos = (likutis * self.palukanos) / 100 / 12
            likutis -= grazintina_dalis
            moketina_suma = grazintina_dalis + menesio_palukanos
            print("{:<8} {:<8} {:<12} {:<12} {:<8}".format(round(menuo, 2), round(grazintina_dalis, 2), round(likutis, 2), round(menesio_palukanos, 2), round(moketina_suma, 2)))
            bendros_sumoketos_palukanos += menesio_palukanos
            bendra_sumoketa_suma += moketina_suma
        print("{:<8} {:<8} {:<12} {:<12} {:<8}".format("Bendra:", round(self.suma, 2), "", round(bendros_sumoketos_palukanos, 2), round(bendra_sumoketa_suma, 2)))
        self._bendros_palukanos = bendros_sumoketos_palukanos
        self._bendra_suma = bendra_sumoketa_suma