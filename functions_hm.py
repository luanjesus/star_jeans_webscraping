import re
import logging
import requests
import pandas as pd
import numpy  as np
import functions_db as fdb

from bs4 import BeautifulSoup
from datetime import datetime

# ============================================
#             AUXLIARY FUNCTIONS
#=============================================

#Verify and create new columns relative with each type of data in conjunt of columns 
def adjust_data(df_aux, df_ref, columns, extension_column):
  SIZE_DF_AUX = len(df_aux)
 

  for c in columns:         
    data = c.replace( extension_column , "" )
    for count in df_aux:
      for i in range(SIZE_DF_AUX):
        
        if count == 0:
          df = df_aux.loc[ df_aux[0].str.contains(data, na=True), 0 ]
          df.name = c 
          df_ref = pd.concat( [df_ref, df ], axis=1 )
          df_ref = df_ref.iloc[:, ~df_ref.columns.duplicated( keep='last')]

        elif count < df_aux.shape[1]:
          df = df_aux.loc[ df_aux[count].str.contains(data, na=True), count ]
          df.name = "aux"
          df_ref = pd.concat( [df_ref, df ], axis=1 )

          id = df_ref.loc[ df_ref["aux"].isnull() == False ].index.values

          if len(id) != 0:
            count = 0
            for i in range(len(df_ref)):
              if i in id :                 
                df_ref[c][i] = df_ref["aux"][id].values[count]
                count += 1
              i += i
          
          df_ref = df_ref.drop("aux", axis=1)
 
  return df_ref

# create new columns with all types of compositions
def create_sub_compositions(df, main_column_name, extension ):
  df_aux     = df[ main_column_name ].str.split( ",", expand=True)
  columns_name_list = get_columns_name(df[main_column_name].unique())
  columns_name_list = [ x.replace(x, x+extension) for x in columns_name_list]
  df_ref = pd.DataFrame( index=np.arange( len( df ) ), columns=columns_name_list )
  df_adjusted = adjust_data( df_aux, df_ref, columns_name_list, extension )
  df = pd.concat( [df, df_adjusted], axis=1) 
  
  for col in columns_name_list:
    df[col] = df[col].apply( lambda x: int( re.search( "\d+", x ).group(0) )/100 if pd.notnull( x ) else 0 )

  return df

# return columns name from data
def get_columns_name(data):
  columns_name = []

  for item in data:
    if not pd.isnull(item):
      columns_name += re.findall(r'\b[a-zA-Z]+\b', item)

  return np.unique(columns_name)


# ===========================================================
#              MAIN FUNCTIONS
#============================================================

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DATA COLLECTION FROM JEANS FOR MEN SHOWCASE 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Parameters
# url: url page showcase
# headers: headers to using in requests 
def get_showcase_data(url , headers):
    logger = logging.getLogger( 'webscraping_hm' )
    # Request to URL
    page = requests.get(url, headers= headers)

    # Beautiful soup object
    soup = BeautifulSoup( page.text , "html.parser" )

    # =========== Pagination ==============
    # Getting data number of items per page and the total of items and calculating the size of page
    class_load_more_hading = soup.find( "h2", class_ = "load-more-heading")
    items_shown            = int(class_load_more_hading.get("data-items-shown"))
    items_total            = int(class_load_more_hading.get("data-total"))
    size_page              = np.ceil( items_total / items_shown ) * items_shown
    logger.debug("TOTAL PRODUCTS: %s", str(items_total))
    
    # Buil page with all products
    full_page = url+"?&offset=0&page-size="+str(round(size_page))
    
    res = requests.get(full_page, headers= headers)
    
    soup = BeautifulSoup( res.text , "html.parser" )

    products = soup.find( "ul" , class_ = "products-listing small" )
    product_list = products.find_all( "article", class_="hm-product-item")


    #product_id
    product_id = [ p.get( "data-articlecode" ) for p in product_list ]

    #product_category
    product_category = [ p.get( "data-category" ) for p in product_list ]

    #product_name
    product_name_list = products.find_all( "a", class_ = "link" )
    product_name = [ p.text for p in product_name_list ]

    #product_price
    price_list = products.find_all( "span", class_ = "price regular" )
    product_price = [ p.text.replace( "$ ", "" ) for p in price_list ]

    #createing data
    data = pd.DataFrame( [product_id, product_name, product_category, product_price ] ).T
    data.columns = ["product_id", "product_name", "product_category", "product_price" ]

    #including if NaN colomns color_name, product_compositions and product_size
    #these data will be get from product detail page
    data["color_name"] = np.nan
    data["product_composition"] = np.nan
    data["product_size"] = np.nan
    data["product_fit"] = np.nan
    data["product_pieces"] = 1

    # product_category: removing preffix "men_"
    data[ "product_department" ] = data[ "product_category" ].apply(  lambda x: x.split("_")[0])
    data[ "product_model" ]      = data[ "product_category" ].apply(  lambda x: x.split("_")[2])
    data[ "product_category" ]   = data[ "product_category" ].apply(  lambda x: x.split("_")[1])

    return data

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#       DATA COLLECTION BY PRODUCTS 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Parameters 
# 1: data - data_screped by function get_showcase_data()

def get_product_details(data, main_url, headers):    
    logger = logging.getLogger( 'webscraping_hm' )

    content_not_mapped = []
    id_cont_not_mapped = []

    count = len(data)
    for pid in data["product_id"]:
        logger.debug("PRODUCT ID: %s - QTD TO FINISH:%s", pid, str(count))
        count -= 1
        #print(">> PRODUCT: "+ str(pid) + " TIME: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # ========== STARTING REQUEST BY PRODUCT
        # URL with product detail 
        url = main_url + 'productpage.' + pid + '.html'
        
        #product detail page
        page = requests.get( url, headers = headers )

        # Soup object
        soup = BeautifulSoup(page.text , "html.parser")


        # ========== GETTING DATA
        # product_color
        data_color = soup.find("a", class_ = "filter-option miniature active")
        data.loc[data["product_id"] == pid, "color_name"] = data_color["data-color"]
            
        # GETTING DIV CONTENT TO GET COMPOSITIONS DATA
        content = soup.find("div", class_ = "content")
        content_list = content.find_all("div")

        #print(" TIME FOR: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for c in content_list:
            dt = c.dt.text

            # product_composition
            if dt.lower() == "composition":
                value = c.ul.text
                data.loc[ data["product_id"] == pid, "product_composition"] = value
            
            # product_size
            elif dt.lower() == "size":
                value = c.dd.text
                data.loc[ data["product_id"] == pid, "product_size"] = value
            
            # product_fit
            elif dt.lower() == "fit":
                value = c.dd.text
                data.loc[ data["product_id"] == pid, "product_fit"] = value

            # product_pieces
            elif dt.lower() == "pieces/pairs":
                value = c.li.text
                data.loc[ data["product_id"] == pid, "product_pieces"] = int( value )
            
            # table if possible tables that was not mapped
            else:
                if dt.lower() not in content_not_mapped:
                    content_not_mapped.append( dt.lower() )
                    id_cont_not_mapped.append( pid )


            # ====== CREATING PRICES PER NUMBER OF PIECES (real price per product)
            price        = float( data.loc[ data["product_id"] == pid, "product_price" ].values[0] )
            value_pieces = int( data.loc[ data["product_id"] == pid, "product_pieces"].values[0] )

            if value_pieces <= 1:
                data.loc[data["product_id"] == pid, "price_per_pieces"]  = price
            else: 
                data.loc[data["product_id"] == pid, "price_per_pieces"] = round( ( price / value_pieces ), 3)

    logger.debug("DATA COMPOSITION NOT USED : " + pd.DataFrame( content_not_mapped, id_cont_not_mapped ) ) 

    return data

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#              DATA CLEANING
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Parameters
# data_raw: data after extraction
# star_datetime_scrapy: datetime when the extrations started
def data_cleaning( data, star_datetime_scrapy, file_csv ):    
    logger = logging.getLogger( 'webscraping_hm' )

    # product_name:  including "_" and removing "®", ":" and "-"
    data[ "product_name" ] = data[ "product_name" ].apply( lambda x: x.lower().replace( " ", "_")) 
    data[ "product_name" ] = data[ "product_name" ].apply( lambda x: x.replace( "®", ""))  
    data[ "product_name" ] = data[ "product_name" ].apply( lambda x: x.replace( ":", "")) 
    data[ "product_name" ] = data[ "product_name" ].apply( lambda x: x.replace( "-", "")) 

    # product_pieces: change to int type
    data[ "product_pieces" ] = data[ "product_pieces" ].astype( int )

    # product_price: change to float type
    data[ "product_price"] = data[ "product_price" ].astype( float )    

    # color_name: removing "/" and including "_" 
    data[ "color_name" ] = data[ "color_name" ].apply( lambda x: x.replace( "/", " " ).lower() )
    data[ "color_name" ] = data[ "color_name" ].apply( lambda x: x.replace( " ", "_" ) )

    # product_fit: removing "\n" and suffix "_fit" 
    data[ "product_fit" ] = data[ "product_fit" ].apply( lambda x: x.replace( "\n", "" ).lower() )
    data[ "product_fit" ] = data[ "product_fit" ].apply( lambda x: x.replace( " fit", "" ) )

    # replaces in product_composition to start extraction data
    data[ "product_composition" ] = data[ "product_composition" ].apply( lambda x: x.replace( "Shell: " , "") )
    data[ "product_composition" ] = data[ "product_composition" ].apply( lambda x: x.replace( "\n", "") ) 
    data[ "product_composition" ] = data[ "product_composition" ].apply( lambda x: x.replace( "Pocket lining:", ":") ) 
    data[ "product_composition" ] = data[ "product_composition" ].apply( lambda x: x.replace( "Pocket:", ":") ) 
    data[ "product_composition" ] = data[ "product_composition" ].apply( lambda x: x.replace( "Lining:", ":") ) 

    # creating sheel composition
    data[ "product_sheel_composition" ] = data[ "product_composition" ].apply( lambda x: x.split(":")[0].lower() ) 
    data[ "product_sheel_composition" ] = data[ "product_composition" ].apply( lambda x: x.split(":")[0].lower() )
    data[ "product_sheel_composition" ] = data[ "product_composition" ].apply( lambda x: x.split(":")[0].lower() )

    # creating Pocket Lining composition
    data[ "product_pck_lining_composition" ] = data[ "product_composition" ].apply( lambda x: x.split(":")[1].lower() if  len(x.split(":")) > 1 else np.nan ) 
    data[ "product_pck_lining_composition" ] = data[ "product_composition" ].apply( lambda x: x.split(":")[1].lower() if  len(x.split(":")) > 1 else np.nan ) 
    data[ "product_pck_lining_composition" ] = data[ "product_composition" ].apply( lambda x: x.split(":")[1].lower() if  len(x.split(":")) > 1 else np.nan ) 

    # creating new columns with all types of compositions divided by sheel and pocket lining
    data = create_sub_compositions(data, "product_sheel_composition", "_sheel")
    data = create_sub_compositions(data, "product_pck_lining_composition", "_pck_lining")
    data = data.drop(["product_composition", "product_sheel_composition", "product_pck_lining_composition"], axis=1)

    # dividing size in centimeter and model (waist / leg length)
    data["size_number_cm"]    = data["product_size"].apply( lambda x: re.search( "\d+(?:\.\d+)?(?=\s*(?:cm))", x).group(0) if pd.notnull( x ) else  np.nan)
    data["size_model"] = data["product_size"].str.extract( "(\d+/\\d+$|\d+$|\w$)")
    data = data.drop( "product_size", axis=1 )

    # creating column with datetime of start and end of webscrapy
    data["start_scrapy"] = star_datetime_scrapy
    data["end_scrapy"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data.to_csv( file_csv )
    logger.debug( f'CSV CREATE >>> {file_csv}')
    return data



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#              DATA INSERTION
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Parameters
# data: dataframe with cleaned and prepared data to insert in database



def data_insertion( data, datetime_scrapy ):
    logger = logging.getLogger( 'webscraping_hm' )

    # Data Insert
    data_insert = data[[
       'product_id',             
       'product_name',      
       'product_department',     
       'product_category',               
       'product_fit',            
       'product_model',            
       'product_price',          
       'product_pieces',         
       'price_per_pieces',         
       'color_name',             
       'cotton_sheel',           
       'elastomultiester_sheel', 
       'lyocell_sheel',          
       'polyester_sheel',        
       'rayon_sheel',            
       'spandex_sheel',          
       'cotton_pck_lining',      
       'polyester_pck_lining',   
       'size_number_cm',         
       'size_model',             
       'start_scrapy',           
       'end_scrapy'             

    ]]


    #connection
    connection = fdb.database_conetion( 'database_hm', '/webscraping_hm/database')
    fdb.insert_data(data_insert, 'showcase_hm', connection, 'append')

    query_select = 'SELECT COUNT(*) QTD_DATA_INSERTED FROM SHOWCASE_HM WHERE START_SCRAPY = ' + "'" + datetime_scrapy + "'"
    res = fdb.get_data(connection, query_select)
    logger.debug(f'QTD DATA INSERTED: {res[0]}')

    return None


