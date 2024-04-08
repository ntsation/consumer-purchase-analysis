# EDA de Vendas da Black Friday
Este repositório contém um Jupyter Notebook em Python para realizar uma Análise Exploratória de Dados (EDA) sobre o conjunto de dados de vendas da Black Friday. 

O objetivo é compreender o comportamento de compra do cliente, especialmente em relação ao valor da compra, para diversos produtos de diferentes categorias. O conjunto de dados foi fornecido pela empresa de varejo "ABC Private Limited" e inclui informações sobre clientes, produtos e detalhes das compras do mês passado.

### Histórico do Conjunto de Dados
A empresa "ABC Private Limited" compartilhou o resumo de compras de vários clientes para produtos de alto volume do mês passado. O conjunto de dados inclui os seguintes detalhes:

 - Dados Demográficos do Cliente:
   - . Idade
   - .Sexo
   - .Estado Civil
   - .Tipo de Cidade
   - .Cidade Atual

- .Detalhes do Produto:
   - .ID do Produto

   - .Categoria do Produto

- .Detalhes da Compra:

   - . Valor Total da Compra do Mês Passado

###  Executando no Jupyter Notebook
1. Abra o Jupyter Notebook no diretório do script.

2. Abra o script no notebook e execute as células conforme necessário.

## Análise Básica do Conjunto de Dados
O código realiza uma análise estatística descritiva do conjunto de dados, exibindo estatísticas resumidas para cada coluna.

- 1. ```Verificação de Valores Ausentes```

      Identifica e imprime a contagem de valores ausentes por coluna no conjunto de dados.

- 2. ```Verificação de Valores Exclusivos```

      Identifica e imprime a contagem de valores exclusivos por coluna no conjunto de dados.

- 3. ```Distribuição de Compras```

      Exibe um histograma que representa a distribuição das compras no conjunto de dados.

- 4. ```Verificação de Outliers```

      Utiliza um boxplot para identificar e imprimir os valores considerados outliers no conjunto de compras.

- 5. ```Análise por Gênero```

      Apresenta um gráfico de barras que mostra o total de compras realizado por cada gênero.

- 6. ```Análise por Estado Civil```

      Exibe um gráfico de barras representando o total de compras por estado civil.

- 7. ```Análise por Ocupação```

      Mostra o total de compras realizado por cada ocupação através de um gráfico de barras.

- 8. ```Média de Compra por Ocupação```

      Apresenta a média de compra para cada ocupação em um gráfico de barras.

- 9. ```Compras por Cidade```

      Exibe um gráfico de barras representando o total de compras em cada categoria de cidade.

- 10. ```Compras por Faixa Etária```

      Mostra o total de compras realizado em cada faixa etária através de um gráfico de barras.

## Nota

Antes de executar o script, certifique-se de ter o arquivo CSV correto no mesmo diretório e caso necessário ajuste o caminho na linha ```df = pd.read_csv()```. 

## Kaggle Dataset
Este projeto utiliza o conjunto de dados disponível no Kaggle. Você pode encontrar o conjunto de dados [aqui](https://www.kaggle.com/datasets/pranavuikey/black-friday-sales-eda).

