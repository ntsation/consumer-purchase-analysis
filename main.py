import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_csv()
# analise basica do conjunto de dados ---------------------------------------------------------------------------
desc_stats = df.describe(include='all')
print(desc_stats)

# verificaçao de valores ausentes -------------------------------------------------------------------------------
missing_values = df.isnull().sum
print('Valores Ausuntes por Coluna:')
print(missing_values)

# verificaçõa de valores exclusivos -----------------------------------------------------------------------------
unique_values = df.nunique()
print('Valores Exclusivos por Coluna:')
print(unique_values)

# Distribuição de compras ---------------------------------------------------------------------------------------
plt.figure(figsizee=(10, 6))
plt.hist(df['Purchase'], bins=30,color='blue', edgecolor='black')
plt.title('Distribuição de Compras')
plt.xlabel('Valor da Compra')
plt.ylabel('Frequencia')
plt.grid(True)
plt.show()

# Verificação de outliers -----------------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Purchase'])
plt.title('Boxplot de Compras')
plt.xlabel('Valor da Compra')
plt.show()

mean_purchase = df['Purchase'].mean()
std_purchase = df['Purchase'].std()

Q1 = df['Purchase'].quantile(0.25)
Q3 = df['Purchase'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[(df['Purchase'] < lower_limit) | (df['Purchase'] > upper_limit)]

print("Limite Inferior:", lower_limit)
print("Limite Superior:", upper_limit)
print("Número de Outliers:", len(outliers))
print(outliers)

# analise de genero ------------------------------------------------------------------------------------------------
gender_purchase = df.groupby('Gender')['Purchase'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=gender_purchase.index, y=gender_purchase.values)
plt.title('Compras por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Total de Compras')
plt.show()

# analise por estado civil ------------------------------------------------------------------------------------------
marital_status_purchase = df.groupby('Marital_Status')['Purchase'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=marital_status_purchase.index, y=marital_status_purchase.values)
plt.title('Compras por Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Total de Compras')
plt.show()

# analise por ocupação ----------------------------------------------------------------------------------------------
occupation_purchase = df.groupby('Occupation')['Purchase'].sum()

plt.figure(figsize=(14, 6))
sns.barplot(x=occupation_purchase.index, y=occupation_purchase.values)
plt.title('Compras por Ocupação')
plt.xlabel('Ocupação')
plt.ylabel('Total de Compras')
plt.show()

# analise de ocupação vs compra ---------------------------------------------------------------------------------------
avg_purchase_by_occupation = df.groupby('Occupation')['Purchase'].mean()

plt.figure(figsize=(14, 6))
sns.barplot(x=avg_purchase_by_occupation.index, y=avg_purchase_by_occupation.values)
plt.title('Média de Compra por Ocupação')
plt.xlabel('Ocupação')
plt.ylabel('Média de Compra')
plt.show()

# analise de compra por cidade ----------------------------------------------------------------------------------------
city_purchase = df.groupby('City_Category')['Purchase'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=city_purchase.index, y=city_purchase.values)
plt.title('Compras por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Total de Compras')
plt.show()

# analise de compra por faixa etaria ----------------------------------------------------------------------------------
age_purchase = df.groupby('Age')['Purchase'].sum()

plt.figure(figsize=(12, 6))
sns.barplot(x=age_purchase.index, y=age_purchase.values)
plt.title('Compras por Faixa Etária')
plt.xlabel('Faixa Etária')
plt.ylabel('Total de Compras')
plt.show()
