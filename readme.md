<div>![]('https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/star_jeans.png')</div>

# Star Jeans
## Status of Project
✅ Done!

## About
In this project, a fictional Brazilian company aims to enter the American fashion market by setting up an e-commerce store for selling men's jeans. The objective is to keep the operating costs low and scale up as they acquire more customers. 

In addition to defining the target audience and product, the company wishes to gain insights into the American market for this segment, in order to set competitive prices for its products.

The company considers its main competitor to be the H&M, a real large-scale American fashion company. Thus, the Brazilian company hires a Data Science consulting firm to answer some business problem questions.

<p align="center">
 <a href="#About">About</a> •
 <a href="#Business-problem">Business Problem</a> •
 <a href="#data-source">Technologies</a> • 
 <a href="#eda-jupyter-notebook">Technologies</a> • 
 <a href="#technologies">Technologies</a>  
</p>


## Business Problem

The following business problems have been identified:

    1. What are the necessary raw materials/compositions for making these pants comparing with the five most produce products from H&M?
    2. What are the sets of models, styles and fits produced by H&M and which is the most produced?
    3. What are the tonality and colors used by H&M and what are the 10 most used varieties?
    4. What are the most suitable characteristics to compose an initial set of products for Star Jeans and what are the best prices for these products?

### Tasks to answer the questions:

To answer these questions, an automatic ETL (extract, transform, and load data) process with web scraping was created to collect the data from H&M's website. The data was collected for a few days, inserted into an SQLite database, and an exploratory data analysis (EDA) was performed for each business problem.

The following tasks were performed to answer the business problem questions:

    Analyze where and what data can be extracted from the H&M website.
    Extract the Data.
    Define the Schema (table columns).
    Define the Infrastructure (API, CSV, TXT, database).
    Design the ETL process.
    Schedule the table update.
    Answer business problem with EDA.
    Deliver the final product.

## Data Source

    **H&M Showcase**: https://www2.hm.com/en_us/men/products/jeans.html
        To get all product ids and other basic information from these products.
    **H&M By Product**: https://www2.hm.com/en_us/productpage.{product_id}.html
        To get other more detailed product information.

## EDA - Jupyter Notebook

Exploratory Data Analysis (EDA) is an essential step in any data science project. It helps to uncover patterns and relationships in the data that may not be immediately apparent. In this project, EDA was used to gain insights into the American market for men's jeans and to answer the business problem questions.

The EDA was performed using Python and Jupyter Notebook. The notebook contains detailed explanations of the data analysis techniques used, as well as visualizations and tables to help communicate the findings.

Through the EDA, we were able to determine the necessary raw materials/compositions for making pants in comparison with the five most produced products by H&M. We also analyzed the sets of models, styles, and fits produced by H&M and found out which ones were the most produced. Furthermore, we explored the tonality and colors used by H&M, and we identified the 10 most commonly used varieties. Lastly, we defined the most suitable characteristics to compose an initial set of products for Star Jeans, and we determined the best prices for these products based on the average prices of similar products offered by H&M and other competitors in the American market.

To access the Jupyter Notebook used for the EDA, please click [here]('https://github.com/luanjesus/star_jeans_webscraping/blob/main/eda.ipynb').

## Technologies

The following tools, libraries and IDE were used in building the project:

- [Python](https://www.python.org/)
- [Jupyter Notebook](https://jupyter.org/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Maptplot Lib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Requests API](https://requests.readthedocs.io/en/latest/)
- [Beautiful Soap 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [SQLite](https://www.sqlite.org/index.html)
- [Visual Studio Code](https://code.visualstudio.com/)

