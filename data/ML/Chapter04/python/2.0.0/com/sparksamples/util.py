import os
import sys
from pyspark.sql.types import *
from pyspark.sql import SQLContext

PATH = "/tmp/data/ML/Chapter04/data"
SPARK_HOME = "/usr/local/spark-2.3.0-bin-hadoop2.7"

# override data path from environment
if 'DATA_PATH' in os.environ :
    PATH = os.environ['DATA_PATH']

# allow us to override SPARK_HOME
if not 'SPARK_HOME' in os.environ :
  os.environ['SPARK_HOME'] = SPARK_HOME

sys.path.append(SPARK_HOME + "/python")

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession

master = "spark://spark-master:7077"
if 'MASTER' in os.environ :
    master = os.environ['MASTER']
# master = "local[2]"
conf = SparkConf().setAppName("First Spark App").setMaster(master)
sc = SparkContext(conf=conf)
spark = SparkSession(sc)


def get_user_data():
    custom_schema = StructType([
        StructField("no", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("gender", StringType(), True),
        StructField("occupation", StringType(), True),
        StructField("zipCode", StringType(), True)
    ])
    
    sql_context = SQLContext(sc)

    user_df = sql_context.read \
        .format('com.databricks.spark.csv') \
        .options(header='false', delimiter='|') \
        .load("%s/ml-100k/u.user" % PATH, schema = custom_schema)

    return user_df


def get_movie_data_df():
    custom_schema = StructType([
        StructField("no", StringType(), True),
        StructField("moviename", StringType(), True),
        StructField("date", StringType(), True),
        StructField("f1", StringType(), True), StructField("url", StringType(), True),
        StructField("f2", IntegerType(), True), StructField("f3", IntegerType(), True),
        StructField("f4", IntegerType(), True), StructField("f5", IntegerType(), True),
        StructField("f6", IntegerType(), True), StructField("f7", IntegerType(), True),
        StructField("f8", IntegerType(), True), StructField("f9", IntegerType(), True),
        StructField("f10", IntegerType(), True), StructField("f11", IntegerType(), True),
        StructField("f12", IntegerType(), True), StructField("f13", IntegerType(), True),
        StructField("f14", IntegerType(), True), StructField("f15", IntegerType(), True),
        StructField("f16", IntegerType(), True), StructField("f17", IntegerType(), True),
        StructField("f18", IntegerType(), True), StructField("f19", IntegerType(), True)
    ])

    sql_context = SQLContext(sc)

    movie_df = sql_context.read \
        .format('com.databricks.spark.csv') \
        .options(header='false', delimiter='|') \
        .load("%s/ml-100k/u.item" % PATH, schema = custom_schema)
    return movie_df


def get_movie_data():
    return sc.textFile("%s/ml-100k/u.item" % PATH)


def get_rating_data():
    return sc.textFile("%s/ml-100k/u.data" % PATH)


