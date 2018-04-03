import os
import sys

import matplotlib

from com.sparksamples.util import path


if not 'SPARK_HOME' in os.environ :
  os.environ['SPARK_HOME'] = "/usr/local/spark-2.3.0-bin-hadoop2.7"
sys.path.append(SPARK_HOME + "/python")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)
import numpy as np
import pylab as P


def main():
    sc = SparkContext(appName="PythonApp")
    raw_data = sc.textFile(path)
    num_data = raw_data.count()
    records = raw_data.map(lambda x: x.split(","))
    x = records.map(lambda r: float(r[-1]))

    sqrt_targets = records.map(lambda r: np.sqrt(float(r[-1]))).collect()
    P.hist(sqrt_targets, bins=40, color='lightblue', normed=True)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(16, 10)

    P.show()


if __name__ == "__main__":
    main()