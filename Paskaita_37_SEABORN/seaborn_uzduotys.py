import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.head(10).to_string())
print(type(mpg))

print(mpg.info())

# def kml(mpg):
#     return mpg*0.425144
# mpg['mpg'] = mpg['mpg'].apply(kml)
# mpg.rename(
#     columns={"mpg": "kml"}, inplace=True)
# print(mpg.head().to_string())


# 1 Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių turi kokią akseleraciją.
# sns.set_style('darkgrid')
# sns.distplot(mpg['acceleration'], kde=False)
# plt.show()

# 2 Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių turi kokius variklio tūrius.
# sns.set_style('darkgrid')
# sns.histplot(mpg['displacement'])
# plt.show()

# 3 Atspausdinkite histogramą, kurioje matytųsi, kokie yra cilindrų skaičiaus variantai.
# sns.set_style('whitegrid')
# sns.countplot( x = 'cylinders',  data=mpg, palette='cubehelix')
# plt.show()

# 4 Atspausdinkite histogramą, kurioje matytųsi, kiek yra pagaminimo metų variantų
# sns.set_style('darkgrid')
# ax = sns.countplot( x = 'model_year',  data=mpg, palette='colorblind')
# ax.bar_label(ax.containers[0])
# plt.show()

# 5 Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių lentelėje kokia šalis pagamino.
# sns.set_style('darkgrid')
# ax = sns.countplot( x = 'origin',  data=mpg, palette='rocket')
# ax.bar_label(ax.containers[0])
# plt.show()


# 6 Atspausdinkite histogramą, kurioje matytųsi, koks kurioje šalyje pagamintų
# automobilių variklio tūrio vidurkis.
# sns.set_style('darkgrid')
# ax = sns.barplot( x = 'origin', y = 'displacement', data=mpg, ci=False )
# ax.bar_label(ax.containers[0])
# plt.show()

#
# 6 Atspausdinkite sklaidos diagramą, kurios x ašis būtų 'displacement', y - 'acceleration',
# taip pat kiekvienas taškas atspindėtų šalį gamintoją ir cilindrų skaičių

# sns.set_style('darkgrid')
# sns.scatterplot(x = 'displacement', y = 'acceleration', data=mpg, hue = 'origin', size = 'cylinders', sizes=(10, 100), legend="full", palette='viridis')
# plt.show()

# 7 Atspausdinkite visas įmanomas sklaidos diagramas lentelėje, kur pagal taško spalvą matytumėm šalį gamintoją.
# Kokias tendencijas galima aiškiai išskirti?

# sns.pairplot( mpg, hue='origin', diag_kind='kde')
# plt.show()


# 8 Atspausdinkite stulpelinę diagramą, 'origin' x 'mpg'. Pabandykite interpretuoti rezultatą.
# sns.set_style('darkgrid')
# sns.boxplot( x = 'origin', y = 'mpg',  data=mpg)
# plt.show()

# 9 Sukurkite koreliacijų matricą. Jos pagrindu atspausdinkite mozaikinę diagramą.
correlation = mpg.corr()
print(correlation)
sns.heatmap(correlation, annot=True,cmap='vlag')
plt.show()

# 10 Atspausdinkite sklaidos diagramų rinkinį, kuriame kiekviena lentelė pagal šalį rodytų 'acceleration' ir 'mpg' sąntykį.
# sns.set_style('darkgrid')
# g = sns.FacetGrid(data=mpg, col = 'origin')
# g.map(sns.scatterplot, 'acceleration', 'cylinders')
# plt.show()