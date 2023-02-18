import functions_db as fdb
import pandas as pd

#connection
connection = fdb.database_conetion( 'database_hm', '/webscraping_hm/database')

query_delete_all = "DELETE FROM SHOWCASE_HM"
query_select_all = "SELECT COUNT(*) QTD_PRODUCT, START_SCRAPY FROM SHOWCASE_HM GROUP BY START_SCRAPY"
query_showcase_schema = """
        CREATE TABLE showcase_hm (
            product_id              TEXT,          
            product_name            TEXT,     
            product_department      TEXT,          
            product_category        TEXT,                  
            product_fit             TEXT,          
            product_model           TEXT,            
            product_price           REAL,          
            product_pieces          INTEGER,          
            price_per_pieces        REAL,            
            color_name              TEXT,          
            cotton_sheel            REAL,          
            elastomultiester_sheel  REAL,          
            lyocell_sheel           REAL,          
            polyester_sheel         REAL,          
            rayon_sheel             REAL,          
            spandex_sheel           REAL,          
            cotton_pck_lining       REAL,          
            polyester_pck_lining    REAL,          
            size_number_cm          INTEGER,          
            size_model              TEXT,          
            start_scrapy            TEXT,          
            end_scrapy              TEXT,
            PRIMARY KEY (product_id, start_scrapy, end_scrapy)

            )
        """
'''
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
'''

#fdb.delete_data(connection, query_delete_all)
#fdb.create_table(connection, query_showcase_schema)
#fdb.insert_data(data, 'showcase_hm', connection, 'replace')
print(fdb.get_data(connection, query_select_all))
connection.close()