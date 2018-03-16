## Start the cluster

```sh
# if you do not want to build the image for the first time, then already have built one for you from dockerhub
docker pull thanhtu/spark:2.3.0
# then start the network
./start.sh
# you can run build to rebuild the image
./build.sh
```

## Running HelloWorld Analysis on the cluster

**Starting the Driver program using Spark Shell**

```sh
docker exec -it spark-driver bash
```

**Start the spark shell (Driver) program**

```sh
spark-shell --master spark://spark-master:7077
# run from data file in shell
val textFile = sc.textFile("/tmp/data/hellospark.txt")
textFile.count()
```

**Run from script file**

```sh
MASTER=spark://spark-master:7077 spark-shell -i /scripts/parallelize.scala
MASTER=spark://spark-master:7077 spark-shell -i /scripts/etl.scala
```

> Check the WebUI for master (127.0.0.1:8080) and worker (127.0.0.1:8081) to check the job details, and 127.0.0.1:4041 for event timeline.

## Stop the cluster

```sh
./stop.sh
```
