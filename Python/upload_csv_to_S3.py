#!/usr/bin/python3
### Import Libraries ###

import pandas as pd
import psycopg2
import boto3
from datetime import datetime
from io import StringIO


### Global Variables ###

current_date = datetime.now().date()
current_date = str(current_date)

directory = 'sample-s3-folder/sample-data' + '_' + current_date + '.csv'


### Database Queries ###

SQL_QUERY = """SELECT * FROM public.catalog LIMIT 100;"""


### Database Connection ###

REDSHIFT_CONN = psycopg2.connect(host='',
                                    user='',
                                    port=,
                                    password='',
                                    dbname='')


### Data Extraction ###

data_df = pd.read_sql(SQL_QUERY, REDSHIFT_CONN)


### Upload to S3 ###

csv_buffer = StringIO()
data_df.to_csv(csv_buffer, index = False)
s3_resource = boto3.resource('s3',
                            aws_access_key_id='',
                            aws_secret_access_key='')
s3_resource.Object('prod-redshift', directory).put(Body=csv_buffer.getvalue())


### Global Variables ###

REDSHIFT_CONN.close

