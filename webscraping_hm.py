import os
import logging
import functions_hm as hm

from   datetime import datetime

if __name__ == "__main__":
    # loggings    
    date_time = datetime.now()
    format_datetime_logger = date_time.strftime("%Y%m%d%H%M%S")
    start_datetime_scrapy  = date_time.strftime("%Y-%m-%d %H:%M:%S")
    
    #get abusolute path dir from webscraping_hm.py
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    logging.basicConfig(
        filename = os.path.join(dir_path, 'webscraping_hm/repos/logs',  format_datetime_logger + '.txt' ),
        level    = logging.DEBUG,
        format   = '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt  = '%Y-%m-%d %H:%M:%S'
    )

    logger = logging.getLogger( 'webscraping_hm' )
    
     
    # parameters
    main_url = 'https://www2.hm.com/en_us/'
    url_showcase = main_url+'men/products/jeans.html'

    headers = {
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
        'Accept-Language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
        'referer': 'https://www.google.com/',
        'cookie': 'DSID=AAO-7r4OSkS76zbHUkiOpnI0kk-X19BLDFF53G8gbnd21VZV2iehu-w_2v14cxvRvrkd_NjIdBWX7wUiQ66f-D8kOkTKD1BhLVlqrFAaqDP3LodRK2I0NfrObmhV9HsedGE7-mQeJpwJifSxdchqf524IMh9piBflGqP0Lg0_xjGmLKEQ0F4Na6THgC06VhtUG5infEdqMQ9otlJENe3PmOQTC_UeTH5DnENYwWC8KXs-M4fWmDADmG414V0_X0TfjrYu01nDH2Dcf3TIOFbRDb993g8nOCswLMi92LwjoqhYnFdf1jzgK0'
    }



    logger.info("Starting Webscraping from " + url_showcase)
    
    # >>>>>> Extraction  
    #showcase data
    data_scraped = hm.get_showcase_data( url_showcase, headers )
    logger.info("Extraction of Showcase page Done!")
    
    #product details
    df_raw = hm.get_product_details( data_scraped,  main_url, headers)
    logger.info("Extraction of Products by ID Done!")

    # >>>>>> Transformation
    file_csv = ( dir_path.replace('\\', '/') + '/webscraping_hm/repos/csv/' + format_datetime_logger + '.csv' )

    data_cleaned = hm.data_cleaning( df_raw, start_datetime_scrapy, file_csv )
    logger.info("Data Cleaning Done!")

    # >>>>>> Insertion
    hm.data_insertion( data_cleaned, start_datetime_scrapy)
    logger.info("Data Insertion Done!")