# EDA de Vendas da Black Friday
Este repositório contém um script em Python para realizar uma Análise Exploratória de Dados (EDA) sobre o conjunto de dados de vendas da Black Friday. O objetivo é compreender o comportamento de compra do cliente, especialmente em relação ao valor da compra, para diversos produtos de diferentes categorias. O conjunto de dados foi fornecido pela empresa de varejo "ABC Private Limited" e inclui informações sobre clientes, produtos e detalhes das compras do mês passado.

### Histórico do Conjunto de Dados
A empresa "ABC Private Limited" compartilhou o resumo de compras de vários clientes para produtos de alto volume do mês passado. O conjunto de dados inclui os seguintes detalhes:

 - Dados Demográficos do Cliente:

1. Idade
2. Sexo
3. Estado Civil
4. Tipo de Cidade
5. Cidade Atual
-  Detalhes do Produto:
1. ID do Produto
2. Categoria do Produto
- Detalhes da Compra:
1. Valor Total da Compra do Mês Passado

## Utilização do Conjunto de Dados
1. Baixe o script e o conjunto de dados.
2. Substitua df = pd.read_csv() pelo caminho do seu arquivo CSV na linha correspondente.
###  Executando no Jupyter Notebook
1. Abra o Jupyter Notebook no diretório do script.

   ```
   jupyter notebook
   ```
2. Abra o script no notebook e execute as células conforme necessário.

## Análise Básica do Conjunto de Dados
O código realiza uma análise estatística descritiva do conjunto de dados, exibindo estatísticas resumidas para cada coluna.

### 1. Verificação de Valores Ausentes
Identifica e imprime a contagem de valores ausentes por coluna no conjunto de dados.

### 2. Verificação de Valores Exclusivos
Identifica e imprime a contagem de valores exclusivos por coluna no conjunto de dados.

### 3. Distribuição de Compras
Exibe um histograma que representa a distribuição das compras no conjunto de dados.

### 4. Verificação de Outliers
Utiliza um boxplot para identificar e imprimir os valores considerados outliers no conjunto de compras.

### 5. Análise por Gênero
Apresenta um gráfico de barras que mostra o total de compras realizado por cada gênero.

### 6. Análise por Estado Civil
Exibe um gráfico de barras representando o total de compras por estado civil.

### 7. Análise por Ocupação
Mostra o total de compras realizado por cada ocupação através de um gráfico de barras.

### 8. Média de Compra por Ocupação
Apresenta a média de compra para cada ocupação em um gráfico de barras.

### 9. Compras por Cidade
Exibe um gráfico de barras representando o total de compras em cada categoria de cidade.

### 10. Compras por Faixa Etária
Mostra o total de compras realizado em cada faixa etária através de um gráfico de barras.

## Nota

Antes de executar o script, certifique-se de ter o arquivo CSV correto no mesmo diretório e ajuste o caminho na linha df = pd.read_csv(). Este script foi desenvolvido para fins educacionais e pode ser personalizado conforme necessário para atender aos requisitos específicos do seu conjunto de dados.

## Kaggle Dataset
Este projeto utiliza o conjunto de dados disponível no Kaggle. Você pode encontrar o conjunto de dados [aqui](https://www.kaggle.com/datasets/pranavuikey/black-friday-sales-eda).



# English Version

# Black Friday Sales EDA
This repository contains a Python script for performing Exploratory Data Analysis (EDA) on the Black Friday sales dataset. The goal is to understand customer purchasing behavior, especially in relation to the purchase amount, for various products across different categories. The dataset was provided by the retail company "ABC Private Limited" and includes information about customers, products, and purchase details from the last month.

### Dataset History
The company "ABC Private Limited" shared the purchase summary of various customers for high-volume products from the last month. The dataset includes the following details:

- Customer Demographics:

1. Age
2. Gender
3. Marital Status
4. City Type
5. Current City
- Product Details:
1. Product ID
2. Product Category
- Purchase Details:
1. Total Purchase Amount for the Last Month

## Dataset Usage
1. Download the script and dataset.
2. Replace df = pd.read_csv() with the path to your CSV file in the corresponding line.
### Running in Jupyter Notebook
1. Open Jupyter Notebook in the script directory.

   ```
   jupyter notebook
   ```
2. Open the script in the notebook and execute the cells as needed.

## Basic Dataset Analysis
The code performs a descriptive statistical analysis of the dataset, displaying summary statistics for each column.

### 1. Missing Values Check
Identifies and prints the count of missing values per column in the dataset.

### 2. Unique Values Check
Identifies and prints the count of unique values per column in the dataset.

### 3. Purchase Distribution
Displays a histogram representing the distribution of purchases in the dataset.

### 4. Outliers Check
Uses a boxplot to identify and print values considered outliers in the purchase dataset.

### 5. Gender Analysis
Presents a bar chart showing the total purchases made by each gender.

### 6. Marital Status Analysis
Displays a bar chart representing the total purchases by marital status.

### 7. Occupation Analysis
Shows the total purchases made by each occupation through a bar chart.

### 8. Average Purchase by Occupation
Presents the average purchase for each occupation in a bar chart.

### 9. Purchases by City
Displays a bar chart representing the total purchases in each city category.

### 10. Purchases by Age Group
Shows the total purchases made in each age group through a bar chart.

## Note
Before running the script, make sure to have the correct CSV file in the same directory and adjust the path in the line df = pd.read_csv(). This script was developed for educational purposes and can be customized as needed to meet the specific requirements of your dataset.

## Kaggle Dataset
This project uses the dataset available on Kaggle. You can find the dataset [here](https://www.kaggle.com/datasets/pranavuikey/black-friday-sales-eda).