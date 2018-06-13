################################
######## MySQL Database ########
################################

### Importing all libraries

# This step assumes that the user has already installed the libraries using either Anaocnda or pip or homebrew or any other Python package manager 
import pandas as pd
import numpy as np
import mysql.connector
from sqlalchemy import create_engine


### Making a database connection & fetching data; Change the variables for your own credentails
con_2 = mysql.connector.connect(user='your_databse_username', password='your_database_password',
                              host='your_database_host_url',
                              database='your_database_name')


df_2 = pd.read_sql_query('SELECT * FROM catalog LIMIT 100;', con_2)
df_2.head() # Default is 5 rows Use df.head(n='Some Number') to modify


con_2.close() # It is a good practice to close the connection post the querying part is completed



##########################################
######## Amazon Redshift Database ########
##########################################

### Importing all libraries

# This step assumes that the user has already installed the libraries using either Anaocnda or pip or homebrew or any other Python package manager 
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine


### Making a database connection & fetching data; Change the variables for your own credentails
# Option 1
con = psycopg2.connect(dbname= 'your_database_name', 
                       host='your_database_host_url', 
                       port= 'port_number', user= 'your_database_username', password= 'your_database_password')

cur_1 = con.cursor()
cur_1.execute("SELECT * FROM public.catalog LIMIT 100;")
cur_1.fetchall()

# Option 2
conn = create_engine('postgresql://`username`:`password`@`host_url`:`port_number`/`database`') 
## Replace the words inside of backticks with your actual credentails, remember to remove the backticks once done

df = pd.read_sql_query('SELECT * FROM public.catalog LIMIT 100;', conn)

df.head() # Default is 5 rows Use df.head(n='Some Number') to modify
