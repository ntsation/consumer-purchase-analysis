# Purchase Analysis Project

## Overview

This project performs a comprehensive analysis of purchase data using Python libraries such as Pandas, Matplotlib, and Seaborn. The analysis includes descriptive statistics, visualizations, and insights into spending patterns based on gender, marital status, occupation, city, and age group.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [Visualizations](#visualizations)

## Installation

To run this project, ensure you have Python installed along with the following libraries:

- pandas
- matplotlib
- seaborn

You can install the required libraries using pip:

```bash
pip install pandas matplotlib seaborn
```

## Usage

1. Clone the repository or download the files.
2. Place your `train.csv` data file in the `./src/` directory.
3. Open the Jupyter Notebook and run each cell sequentially to perform the analysis.

```bash
jupyter notebook
```

4. Follow the instructions and observations provided in the notebook to understand the analysis.

## Data Description

The dataset (`train.csv`) should contain the following columns:

- **Purchase**: The purchase amount made by individuals.
- **Gender**: The gender of the individual (e.g., Male, Female).
- **Marital_Status**: Marital status of the individual (e.g., Single, Married).
- **Occupation**: The occupation of the individual.
- **City_Category**: The category of the city (e.g., A, B, C).
- **Age**: The age group of the individual.

## Visualizations

The analysis includes various visualizations to help understand the data better:

- **Purchase Distribution**: Histogram showing the distribution of purchase amounts.
- **Purchase Boxplot**: Boxplot to identify outliers in purchase amounts.
- **Purchases by Gender**: Bar plot comparing total purchases made by different genders.
- **Purchases by Marital Status**: Bar plot comparing total purchases based on marital status.
- **Purchases by Occupation**: Bar plot showing total purchases for each occupation.
- **Average Purchases by Occupation**: Bar plot showing average purchase amounts by occupation.
- **Purchases by City**: Bar plot visualizing total purchases by city category.
- **Purchases by Age Group**: Bar plot comparing total purchases across different age groups.