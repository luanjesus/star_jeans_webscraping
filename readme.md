<div style="text-align:center">
  <img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/star_jeans.png" alt="">
</div>

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
 <a href="#data-source">Data Source</a> • 
 <a href="#eda--jupyter-notebook">EDA</a> • 
 <a href="#technologies">Technologies</a>  
</p>


## Business Problem

### The following business problems have been identified:

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
- To get all product ids and other basic information from these products.
**H&M By Product**: https://www2.hm.com/en_us/productpage.{product_id}.html
- To get other more detailed product information.

### Created DataSet
| Columns                 | Type Data |
| ----------------------- | --------- |
| product_id              | text      |  
| product_name            | text      |  
| product_department      | text      |  
| product_category        | text      |  
| product_fit             | text      |  
| product_model           | text      |  
| product_price           | float     |
| product_pieces          | int       |
| price_per_pieces        | float     |
| cotton_sheel            | float     |
| elastomultiester_sheel  | float     |
| lyocell_sheel           | float     |
| polyester_sheel         | float     |
| rayon_sheel             | float     |
| spandex_sheel           | float     |
| cotton_pck_lining       | float     |
| polyester_pck_lining    | float     |
| start_scrapy            | datetime  |
| end_scrapy              | datetime  |
| tonality_color          | text      |
| material                | text      |
| style                   | text      |   
| color                   | text      |

## EDA - Jupyter Notebook

Exploratory Data Analysis (EDA) is an essential step in any data science project. It helps to uncover patterns and relationships in the data that may not be immediately apparent. In this project, EDA was used to gain insights into the American market for men's jeans and to answer the business problem questions.

The EDA was performed using Python and Jupyter Notebook. The notebook contains detailed explanations of the data analysis techniques used, as well as visualizations and tables to help communicate the findings.

Through the EDA, we were able to determine the necessary raw materials/compositions for making pants in comparison with the five most produced products by H&M. We also analyzed the sets of models, styles, and fits produced by H&M and found out which ones were the most produced. Furthermore, we explored the tonality and colors used by H&M, and we identified the 10 most commonly used varieties. Lastly, we defined the most suitable characteristics to compose an initial set of products for Star Jeans, and we determined the best prices for these products based on the average prices of similar products offered by H&M and other competitors in the American market.

To access the Jupyter Notebook used for the EDA, please [click here](https://github.com/luanjesus/star_jeans_webscraping/blob/main/eda.ipynb).

## Answers to the Business Analysis

### 1. What are the necessary raw materials/compositions for making these pants comparing with the five most produce products from H&M?

By grouping the 'material' field ('denim' and 'regular') with the percentage information of the external (sheel) and internal ompositions (pocket lining) of the fabric. We can see that H&M has 35 varieties of compositions for creating pieces. A strategy that he customer can use to check which materials/compositions will be used in their parts is to replicate the most built models among the 5 varieties. 
Assuming that the customer will initially use the sets of materials and compositions of the five cases most created by the competitor, he main materials would be: 

<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/business_problem_answer1.PNG" alt="">
          
<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/business_problem_answer1-2.PNG" alt="">
At least 80% of the products must be Denim and 20% a different material classified as 'Normal'.     

**For cases using Denim:**
- Between 40% - 45% must use 100% cotton in sheel. 
- For the rest of the cases with Denim (55% to 60%), a variation between 98% and 99% of cotton in sheel can be used and for the rest of he sheel, use spandex (1% to 2%).
- Regarding the composition of the pocket lining, 75% of Denim products must use a mixture of 35% cotton and 65% polyester and the rest 00% cotton. 

**For cases using 'Normal':**
- All pieces will use 100% cotton in sheel. 
- And Regarding the composition of the pocket lining, all cases will use 35% cotton and 65% polyester.

### 2. What are the sets of models, styles and fits produced by H&M and which is the most produced?

**All sets produced with the combination of model, style and fit**
<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/business_problem_answer2.PNG" alt="">

- **Types of Models:** slim, regular, loose, relaxed, skinny, joggers, straight, ripped.
- **Types of Styles:** normal, trashed, checked, no_fade, patterned, print
- **Types of Fits:** slim, regular, loose, relaxed and skinny
- **The most produced model:** slim 
- **The most produced style:** normal 
- **The most produced fit:** slim

### 3. What are the tonality and colors used by H&M and what are the 10 most used varieties?

- **All/Top10 Tonalities:**  dark, light and other (Neutral is the most common, the others is olive, graphite, etc.).
- **All Colors:**  black, blue, gray, light, purple, beige, cream, green and white.
- **All Colors:**  black, blue, gray, light, purple, beige and cream.

- **In the cases of the 10 most used tones:** 60% are of the 'other' type and of these, at least 50% are of the neutral type (for the colors blue, black and white) and the others are tones such as beige, graphite and olive.

- **The most used colors:** Approximately 58% blue, 23% black, 13% gray, 3% white, 2% cream and 1% purple.

- **Note 1:** Approximately 49% of the products are composed of other neutral tones.
- **Note 2:** Approximately 57% of the products are composed of blue colors.

<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/business_problem_answer3-1.PNG" alt="">
<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/business_problem_answer3-2.PNG" alt="">
<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/business_problem_answer3-3.PNG" alt="">

### 4. What are the most suitable characteristics to compose an initial set of products for Star Jeans and what are the best prices for these products?

- **Material:** Denim.
- **Style:** Normal.
- **Sheel Composition:** 100% Cotton or Cotton with a maximum of 2% spandex .
- **Sheel Pocket Lining:** 100% Cotton or 35% Cotton and 65% of Polyester.
- **Tonality/Color:** Netral/Blue, Netral/Black, Dark/Blue, Light/Blue, Dark/Gray and Light/Gray.
- **Fit/Model:** Slim, Regular, Loose, Relaxed, Skinny, Regular/Joggers, Regular/Straight, Skinny/Ripped, Relaxed/Joggers.

**Best prices for each type of part:**

| product_fit |	product_model | cotton_sheel | spandex_sheel | cotton_pck_lining | polyester_pck_lining	| tonality_color | color       |   mean      | std       | min       |   max   |
| ----------- | ------------- | ------------ | ------------- | ----------------- | -------------------- | -----------    | ----------- | ----------- | --------  | --------- | ------- |
|   loose	  |     loose	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |     dark	     |  blue       |  44.99	     |   0.00	 |  44.99	 |  44.99  |
|   loose	  |     loose	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |    light	     |  blue       |  41.66	     |   2.46	 |  39.99	 |  44.99  |
|   loose	  |     loose	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |    light	     |  gray       |  39.99	     |   0.00	 |  39.99	 |  39.99  |
|   loose	  |     loose	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |    other	     |  blac       |  39.99	     |   0.00	 |  39.99	 |  39.99  |
|   loose	  |     loose	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |    other	     |  blue       |  40.82	     |   1.90	 |  39.99	 |  44.99  |
|   regular	  |     regular	  |      0.98	 |   0.02	     |    0.35	         |   0.65	            |     dark	     |  gray       |  34.99	     |   0.00	 |  34.99	 |  34.99  |
|   regular	  |     regular	  |      0.98	 |   0.02	     |    0.35	         |   0.65	            |    light	     |  blue       |  24.99	     |   0.00	 |  24.99	 |  24.99  |
|   regular	  |     regular	  |      0.99	 |   0.01	     |    0.35	         |   0.65	            |    other	     |  blue       |  34.99	     |   7.39	 |  24.99	 |  39.99  |
|   regular	  |     regular	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |    other	     |  blue       |  19.99	     |   0.00	 |  19.99	 |  19.99  |
|   regular	  |     straight  |      0.99	 |   0.01	     |    0.35	         |   0.65	            |    other	     |  blue       |  39.99	     |   5.35	 |  34.99	 |  44.99  |
|   relaxed	  |     relaxed	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |     dark	     |  blue       |  38.74	     |   5.63	 |  29.99	 |  44.99  |
|   relaxed	  |     relaxed	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |    light	     |  blue       |  36.66	     |   4.92	 |  29.99	 |  39.99  |
|   relaxed	  |     relaxed	  |      1.00	 |   0.00	     |    0.35	         |   0.65	            |    other	     |  blue       |  38.81	     |   5.46	 |  29.99	 |  44.99  |
|   skinny	  |     ripped	  |      0.98	 |   0.02	     |    0.35	         |   0.65	            |    light	     |  blue       |  39.99	     |   0.00	 |  39.99	 |  39.99  |
|   skinny	  |     ripped	  |      0.98	 |   0.02	     |    0.35	         |   0.65	            |    other	     |  blue       |  39.99	     |   0.00	 |  39.99	 |  39.99  |
|   skinny	  |     skinny	  |      0.98	 |   0.02	     |    0.35	         |   0.65	            |    other	     |  blue       |  29.99	     |   0.00	 |  29.99	 |  29.99  |
|   skinny	  |     skinny	  |      0.99	 |   0.01	     |    0.35	         |   0.65	            |     dark	     |  blue       |  24.99	     |   0.00	 |  24.99	 |  24.99  |
|   skinny	  |     skinny	  |      0.99	 |   0.01	     |    0.35	         |   0.65	            |    other	     |  blue       |  24.99	     |   0.00	 |  24.99	 |  24.99  |
|   slim	  |     slim	  |      0.99	 |   0.01	     |    0.35	         |   0.65	            |    light	     |  blue       |  23.32	     |   2.46	 |  19.99	 |  24.99  |
|   slim	  |     slim	  |      0.99    |   0.01	     |    0.35	         |   0.65	            |    other	     |  blue       |  22.49	     |   2.67	 |  19.99	 |  24.99  |


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

