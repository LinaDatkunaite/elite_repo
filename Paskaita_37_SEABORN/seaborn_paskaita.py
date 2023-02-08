# seaborn - duomenu atvaizdavimo biblioteka padaryta and Matplotlib bet su daugiau elementu
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# pd.set_option('display.max_columns', None)
tips = sns.load_dataset('tips')
print(tips.shape)
print(tips.head())
# sns.displot(tips['total_bill'])

# su linija, jei nenorim linijos rasom kde=false
# sns.distplot(tips['total_bill'], kde=False, bins=20)

# kind = 'hex' - sugrupuoja aplinkinius taskus i sesiakampi
# kind = 'reg'su linija - tendencija
# kind = 'kde' rodo intensyvuma sugrupuoja
# 'hue' kategorizavimas/ grupavimas

# sns.jointplot(x = 'total_bill', y = 'tip', data=tips,hue='species')
# plt.show()


# sns.scatterplot( x = 'tip', y = 'total_bill', data=tips, hue = 'sex', size = 'size')
# plt.show()


# sns.pairplot( tips, hue='sex', diag_kind='hist')
# plt.show()

# grazina pagal vidurki defaultiskai
# sns.barplot( x = 'sex', y = 'total_bill', data=tips, hue='day', estimator=sum)
# plt.show()
#
# sns.countplot( x = 'smoker',  data=tips, hue = 'sex')
# plt.show()

# sns.boxplot( x = 'smoker', y = 'total_bill',  data=tips)
# plt.show()

# koreliacijos = tips.corr()
# print(koreliacijos)
# sns.heatmap(koreliacijos, annot=True)
# plt.show()

# g = sns.FacetGrid(data=tips, col = 'time', row='smoker')
# g.map(sns.scatterplot, 'tip', 'total_bill')
# plt.show()


# ci=False nuimti reference line
# sns.set_style('darkgrid') pasirinkti fona
# palette='cividis'

sns.set_style('darkgrid')
sns.barplot(x='sex', y='total_bill', data=tips, hue='day', estimator=sum, ci=False, palette='inferno')


# panaikina linijas aplink grafika
sns.despine()
plt.show()