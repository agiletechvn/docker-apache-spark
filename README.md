## Start the cluster
```sh
./start.sh
```

## Running HelloWorld Analysis on the cluster

**Starting the Driver program using Spark Shell**  
```sh
docker exec -it spark-driver bash 
```

**Start the spark shell (Driver) program**  
```sh
spark-shell --master spark://spark-master:7077
```

**Execute following commands to run an analysis**  
```sh
val textFile = sc.textFile("/tmp/data/hellospark.txt")
textFile.count()
```

> Check the WebUI for master (127.0.0.1:8080) and worker (127.0.0.1:8081) to check the job details, and 127.0.0.1:4041 for event timeline.

## Stop the cluster
```sh
./stop.sh
```
