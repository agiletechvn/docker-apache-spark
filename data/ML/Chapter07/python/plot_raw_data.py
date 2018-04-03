import os
import sys

import matplotlib

from com.sparksamples.util import path


if not 'SPARK_HOME' in os.environ :
  os.environ['SPARK_HOME'] = "/usr/local/spark-2.3.0-bin-hadoop2.7"
sys.path.append(os.environ['SPARK_HOME'] + "/python")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)
import numpy as np
import pylab as P


def main():
    
    master = "spark://spark-master:7077" 
    # master = "local[2]"
    conf = SparkConf().setAppName("PythonApp").setMaster(master)
    sc = SparkContext(conf=conf)

    raw_data = sc.textFile(path)
    num_data = raw_data.count()
    records = raw_data.map(lambda x: x.split(","))
    x = records.map(lambda r : float(r[-1]))
    print (records.first())
    print (x.first())
    targets = records.map(lambda r: float(r[-1])).collect()
    print (targets)
    P.hist(targets, bins=40, color='lightblue', normed=True)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(40, 10)
    P.show()

    log_targets = records.map(lambda r: np.log(float(r[-1]))).collect()
    P.hist(log_targets, bins=40, color='lightblue', normed=True)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(16, 10)
    P.show()


if __name__ == "__main__":
    main()