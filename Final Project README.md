This project performs a comprehensive analysis of the Penn World Table (PWT) version 10.0 dataset to understand and explain differences in economic performance across countries. The main steps and objectives of the analysis are summarized as follows:

### 1. **Importing and Preparing Data**
- The project starts by importing necessary libraries and the Penn World Table dataset.
- A subset of the dataset is created, focusing on key economic variables such as GDP, employment, human capital, labor share, total factor productivity, and population for the years 2010 to 2019.

### 2. **Descriptive Statistics**
- Descriptive statistics are computed for each year from 2010 to 2019 to provide a summary of the data.
- For detailed analysis, the year 2019 is selected as it is the latest year with the most complete data.
- Missing data is handled by discarding countries with NaN values.

### 3. **Generating New Variables and Further Descriptive Analysis**
- New variables such as GDP per worker, GDP per hour worked, GDP per unit of human capital, and GDP per hour of human capital are generated.
- Descriptive statistics for these new variables are computed.
- The project identifies the richest and poorest countries based on GDP per worker.
- Percentile ranks for GDP per worker, GDP per hour worked, GDP per unit of human capital, and GDP per hour of human capital are calculated to understand the distribution of these metrics across countries.

### 4. **Variance Analysis**
- The variance and log variance of the newly created GDP measures are calculated.
- Ratios between different percentiles (e.g., 90th to 10th, 95th to 5th) are computed to analyze income inequality.

### 5. **Regression Analysis**
- An ordinary least squares (OLS) regression is performed to determine the relationship between GDP per worker and factors such as human capital and average hours worked.
- The regression results indicate that increases in human capital are positively correlated with GDP per worker, whereas increases in average hours worked are negatively correlated.

### 6. **Scatterplots**
- Scatterplots are produced to visualize the relationships between key economic variables (capital, human capital, average annual hours worked, labor share, total factor productivity) and log GDP measures (per capita, per worker, per hour worked, per unit of human capital).

### 7. **Measures of Success**
- New variables representing the interaction between capital and human capital are generated.
- Descriptive statistics and variance analysis of these new interaction terms are provided.
- Success measures are computed to evaluate how well these new interaction terms explain the variation in economic output across countries.

### Summary:
The project aims to understand the determinants of economic performance across countries by:
- Analyzing key economic indicators from the Penn World Table dataset.
- Generating new metrics to provide deeper insights.
- Performing regression analysis to identify key drivers of GDP per worker.
- Visualizing the data through scatterplots to highlight relationships between variables.
- Assessing the explanatory power of combined factors like capital and human capital.

The findings highlight the significant role of human capital in driving economic performance while providing a detailed quantitative assessment of income disparities and economic inequalities among countries.
