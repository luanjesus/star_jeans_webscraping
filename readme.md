<h2>✅ Project Done!</h2>

<span style="color: yellow;"><strong>Disclaimer:</strong> The following context is completely fictitious. The company, context and business issues were created exclusively for the development of the project and are based on a project from <a href="https://comunidadeds.com/?utm_source=linkedin&utm_medium=company-page">Comunidade DS</a>.</span>

For a more comprehensive and detailed view of the exploratory data analysis, please refer to the following Jupyter notebook.

[![EXPLORATORY DATA ANALYSIS - Jupyter](https://img.shields.io/badge/Exploratory%20Data%20Analysis-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://github.com/luanjesus/star_jeans_webscraping/blob/main/eda.ipynb)

# Star Jeans

<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/star_jeans.png" alt="">

# 1.0. About
In this project, a fictional Brazilian company aims to enter the American fashion market by setting up an e-commerce store for selling men's jeans. The objective is to keep the operating costs low and scale up as they acquire more customers. 

In addition to defining the target audience and product, the company wishes to gain insights into the American market for this segment, in order to set competitive prices for its products.

The company considers its main competitor to be the H&M, a real large-scale American fashion company. Thus, the Brazilian company hires a Data Science consulting firm to answer some business problem questions.

<p align="center">
 <a href="#About">About</a> •
 <a href="#Business-problem">Business Problem</a> •
 <a href="#data-source">Data Source</a> • 
 <a href="#eda-jupyter-notebook">EDA</a> •
 <a href="#conclusions">Conclusions</a> •  
 <a href="#technologies">Technologies</a>  
</p>


# 2.0. Business Problem

## 2.1. The following business problems have been identified:

    1. What are the necessary raw materials/compositions for making these pants comparing with the five most produce products from H&M?
    2. What are the sets of models, styles and fits produced by H&M and which is the most produced?
    3. What are the tonality and colors used by H&M and what are the 10 most used varieties?
    4. What are the most suitable characteristics to compose an initial set of products for Star Jeans and what are the best prices for these products?

## 2.2. Solution Strategy

1. Data Collection: Collecting data from H&M's website using web scraping, which is an automated method of extracting large amounts of data from websites. H&M is a retail firm that offers clothing and accessories at a fair price.

2. Data Cleaning: It involves fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.

3. ETL Design: ETL (Extract, Transform, Load) is an automated process that extracts the necessary information for analysis from raw data, transforms it into a format that meets business needs, and loads it into a database. The following are the steps involved in ETL design:

    Designing the ETL architecture.
    Defining the dependencies between jobs, which can sometimes depend on the state of other jobs.
    Using windows task scheduler to schedule and run jobs automatically. Windows task scheduler runs in the background and executes scheduled jobs known.
    Using the Python logging module to generate and store logs. The logging module allows you to track events when your code runs so that when it crashes, you can check the logs and identify the cause.

<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/etl-job-flow.PNG" alt="">

4. Answer business problem with EDA.

# 3.0. Data Source

**H&M Showcase**: https://www2.hm.com/en_us/men/products/jeans.html
- To get all product ids and other basic information from these products.

**H&M By Product**: https://www2.hm.com/en_us/productpage.{product_id}.html
- To get other more detailed product information.

## 3.1 Created DataSet
| Columns                 | Description |
| ----------------------- | --------- |
| product_id              | Unique Id for each product      |  
| product_name            | Jeans' name      |  
| product_department      | Jeans' Department (Men)      |  
| product_category        | Jeans' Category      |  
| product_fit             | Jeans' Fit      |  
| product_model           | Jenas' Model      |  
| product_price           | Total Price     |
| product_pieces          | Quantity of pieces      |
| price_per_pieces        | Price per piece unit     |
| cotton_sheel            | Percentage of Cotton sheel composition     |
| elastomultiester_sheel  | Percentage of Elastomultiester sheel composition     |
| lyocell_sheel           | Percentage of Lyocell sheel composition     |
| polyester_sheel         | Percentage of Polyester sheel composition     |
| rayon_sheel             | Percentage of Rayon sheel composition     |
| spandex_sheel           | Percentage of Spandex sheel composition     |
| cotton_pck_lining       | Percentage of Cotton Pocket Lining composition     |
| polyester_pck_lining    | Percentage of Polyester Pocket Lining composition      |
| start_scrapy            | Time scrapy started  |
| end_scrapy              | Time scrapy ended  |
| tonality_color          | Tonality of color      |
| material                | Fabric used |
| style                   | Jeans' style      |   
| color                   | Jeans' color      |

# 4.0. EDA Jupyter Notebook

Exploratory Data Analysis (EDA) is an essential step in any data science project. It helps to uncover patterns and relationships in the data that may not be immediately apparent. In this project, EDA was used to gain insights into the American market for men's jeans and to answer the business problem questions.

The EDA was performed using Python and Jupyter Notebook. The notebook contains detailed explanations of the data analysis techniques used, as well as visualizations and tables to help communicate the findings.

Through the EDA, we were able to determine the necessary raw materials/compositions for making pants in comparison with the five most produced products by H&M. We also analyzed the sets of models, styles, and fits produced by H&M and found out which ones were the most produced. Furthermore, we explored the tonality and colors used by H&M, and we identified the 10 most commonly used varieties. Lastly, we defined the most suitable characteristics to compose an initial set of products for Star Jeans, and we determined the best prices for these products based on the average prices of similar products offered by H&M and other competitors in the American market.

To access the Jupyter Notebook used for the EDA, please [click here](https://github.com/luanjesus/star_jeans_webscraping/blob/main/eda.ipynb).

## 4.1. Answers to the Business Analysis

### 4.1.1. What are the necessary raw materials/compositions for making these pants comparing with the five most produce products from H&M?

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

### 4.1.2. What are the sets of models, styles and fits produced by H&M and which is the most produced?

**All sets produced with the combination of model, style and fit**
<img src="https://github.com/luanjesus/star_jeans_webscraping/blob/main/repos/img/business_problem_answer2.PNG" alt="">

- **Types of Models:** slim, regular, loose, relaxed, skinny, joggers, straight, ripped.
- **Types of Styles:** normal, trashed, checked, no_fade, patterned, print
- **Types of Fits:** slim, regular, loose, relaxed and skinny
- **The most produced model:** slim 
- **The most produced style:** normal 
- **The most produced fit:** slim

### 4.1.3. What are the tonality and colors used by H&M and what are the 10 most used varieties?

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

### 4.1.4. What are the most suitable characteristics to compose an initial set of products for Star Jeans and what are the best prices for these products?

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

# 5.0. Conclusions

Based on the analysis conducted, we can conclude that Star Jeans can start by producing denim pants with a normal style and a variety of fits such as slim, regular, loose, relaxed, skinny, regular joggers, regular straight, skinny ripped, and relaxed joggers. For the material, they can use 100% cotton or cotton with a maximum of 2% spandex for the sheel, and a pocket lining made of 100% cotton or 35% cotton and 65% polyester. The tonality and color options that are recommended are neutral/blue, neutral/black, dark/blue, light/blue, dark/gray, and light/gray.

Moreover, by analyzing the products produced by H&M, we can see that the most produced model, style, and fit are slim, normal, and slim, respectively. Additionally, H&M uses a variety of tonalities and colors in their products, with neutral being the most common. The prices of Star Jeans products can be competitive with the prices of H&M, as shown in the analysis of the best prices for each type of part.

Overall, the analysis provides a good starting point for Star Jeans to produce high-quality denim pants that are competitive in terms of style, fit, and price with those of their main competitor.

# 6.0. Next Steps to Improve

Certainly! Here are some ideas for next steps to improve:

- Conduct customer surveys or focus groups to gather feedback on product features, packaging, and pricing.
- Expand product offerings to meet the needs and preferences of a wider range of customers.
- Develop and implement a loyalty program to reward and retain customers.
- Analyze customer data to identify patterns and preferences, and use that information to improve marketing strategies and customer - experiences.
- Partner with influencers or other brands to reach new audiences and expand the customer base.
- Monitor and respond to customer reviews to improve product quality and customer satisfaction.
- Offer promotions or discounts to incentivize repeat purchases and attract new customers.

# 7.0. Technologies

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

# 8.0. Authors

[@luanjesus](https://www.linkedin.com/in/luanjesus/)

I am a Data Analyst with a degree in Computer Engineering with +6 years of experience in managing, developing and improving transactional communications journeys as a CCM Systems Analyst. I also develop data products using machine learning techniques to solve business issues.

My main objective is to work as a data scientist, developing data products with Machine Learning techniques and statistical analysis to help companies make their strategic decisions in the best possible way.