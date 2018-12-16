import pyspark
from pyspark.sql import SQLContext
import json
import os

import subprocess
 
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

from functools import reduce  # For Python 3.x
from pyspark.sql import DataFrame

def unionAll(*dfs):
    return reduce(DataFrame.unionAll, dfs)




list_df =[]

root = "/datasets/twitter_internetarchive/2017/08/"
df = sqlContext.read.json(root + '/*/*/*.json.bz2').select('text','created_at')
aggregate_df = df.filter("LOWER(text) like '%trump%' or LOWER(text) like '%maga%'or LOWER(text) like '%obama%'\
                    or LOWER(text) like '%senate%'or LOWER(text) like '%congress%'or LOWER(text) like '%politics%'or LOWER(text) like '%policy%'\
                    or LOWER(text) like '%clinton%'or LOWER(text) like '%republican%'or LOWER(text) like '%democrat%'\
                    or LOWER(text) like '%gop%'or LOWER(text) like '%dnc%'")

aggregate_df.write.parquet('tweets_august.parquet')
'''
directory_day = [root+"%.2d" % i+'/' for i in range(10,15)]

def extract_tweets():
    for i,day in enumerate(directory_day):
        directory_hours = [day+"%.2d" % i+'/' for i in range(6,24)]
        for j,hour in enumerate(directory_hours):
                files = [hour+"%.2d" % i+".json.bz2" for i in range(30,60)]
                for k,filename in enumerate(files): 
                    try:
                        df = sqlContext.read.json(filename)
                        list_df.append(df)
                    except Exception as e:
                         pass  

    aggregate_df = unionAll(*list_df)       
    aggregate_df = aggregate_df.select('text','created_at')              
    aggregate_df = df.filter("LOWER(text) like '%trump%' or LOWER(text) like '%maga%'or LOWER(text) like '%obama%'\
                    or LOWER(text) like '%senate%'or LOWER(text) like '%congress%'or LOWER(text) like '%politics%'or LOWER(text) like '%policy%'\
                    or LOWER(text) like '%clinton%'or LOWER(text) like '%republican%'or LOWER(text) like '%democrat%'\
                    or LOWER(text) like '%gop%'or LOWER(text) like '%dnc%'")
    aggregate_df.write.parquet('tweets_charlottesville.parquet')

extract_tweets()
'''
