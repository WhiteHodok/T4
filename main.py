import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка дата-сета в DataFrame
df = pd.read_csv('forestfires.csv')

# Просмотр первых 5 строк дата-сета
print(df.head())

# Размер дата-сета
print('Размер дата-сета:', df.shape)

# Сводная информация о дата-сете
print(df.info())

# Описательные статистики
print(df.describe())

# Гистограмма для каждого признака
df.hist(bins=30, figsize=(20, 20))
plt.show()

# Тепловая карта корреляции между признаками
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Диаграммы рассеяния для наиболее коррелирующих признаков
sns.pairplot(df[['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'area']])
plt.show()

