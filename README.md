## Start the cluster

```sh
# if you do not want to build the image for the first time, then already have built one for you from dockerhub
docker pull thanhtu/spark:2.3.0
# then start the network, default is spark image which about to be built
./start.sh [thanhtu/spark]
# if you need to run sparkR you should use thanhtu/spark instead for spark-driver image
# you can run build to rebuild the image or to start your own spark image
./build.sh
```

## Running HelloWorld Analysis on the cluster

**Starting the Driver program using Spark Shell**

```sh
docker exec -it spark-driver bash
```

**Start the spark shell (Driver) program**

```sh
# go to data folder which contains code for spark book
# cd /tmp/data
spark-shell --master spark://spark-master:7077
# run from data file in shell
val textFile = sc.textFile("/tmp/data/hellospark.txt")
textFile.count()

# to start pyspark for python3, must run
# ln -s /usr/bin/python3 /usr/bin/python

# if not install sparkR, we can run R then
# if (!require('devtools')) install.packages('devtools', repos='http://cran.us.r-project.org')
# devtools::install_github('apache/spark@v2.3.0', subdir='R/pkg')
```

**Run from script file**

```sh
MASTER=spark://spark-master:7077 spark-shell -i /scripts/parallelize.scala
MASTER=spark://spark-master:7077 spark-shell -i /scripts/etl.scala
```

> Check the WebUI for master (127.0.0.1:8080) and worker (127.0.0.1:8081) to check the job details, and 127.0.0.1:4040 for event timeline.

## Stop the cluster

```sh
./stop.sh
```

> To run at your local computer, first install Spark, then link data folder to the same path as worker docker, or you have to deploy it on apache yarn(hadoop)

```sh
ln -s $PWD/data /tmp/data
```
