
# can check SPARK_HOME before running

Sys.setenv(SPARK_HOME = "/usr/local/spark-2.3.0-bin-hadoop2.7")
.libPaths(c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib"), .libPaths()))

#load the Sparkr library
library(SparkR)
# look at setMethod(methodName), should be like methodRDD for signature PipelinedRDD
# https://github.com/apache/spark/blob/master/R/pkg/R/
# master <- "local[2]"
master <- "spark://spark-master:7077"
# change version for spark 2.11 to 1.5.0
sc <- sparkR.session(master = master, sparkHome = Sys.getenv("SPARK_HOME"), 
                    appName="First Spark App", sparkPackages="com.databricks:spark-csv_2.11:1.5.0")

user.purchase.history <- "data/UserPurchaseHistory.csv"
data <- read.df(user.purchase.history, "com.databricks.spark.csv", header="false")
head(data)
count(data)
printSchema(data)

# SparkR methods 

parseFields <- function(record) {
  Sys.setlocale("LC_ALL", "C") # necessary for strsplit() to work correctly
  parts <- strsplit(as.character(record), ",")
  list(name=parts[1], product=parts[2], price=parts[3])
}

parsedRDD <- SparkR:::lapply(data, parseFields)
SparkR:::cacheRDD(parsedRDD)
numPurchases <- SparkR:::countRDD(parsedRDD)

sprintf("Number of Purchases : %d", numPurchases)
getName <- function(record){
  record[1]
}

getPrice <- function(record){
  record[3]
}

nameRDD <- SparkR:::lapply(parsedRDD, getName)
nameRDD = SparkR:::collectRDD(nameRDD)
head(nameRDD)

uniqueUsers <- unique(nameRDD)
head(uniqueUsers)

priceRDD <- SparkR:::lapply(parsedRDD, function(x) { as.numeric(x$price[1])})
SparkR:::takeRDD(priceRDD,3)

totalRevenue <- SparkR:::reduce(priceRDD, "+")

sprintf("Total Revenue : %.2f", totalRevenue)

products <- SparkR:::lapply(parsedRDD, function(x) { list( toString(x$product[1]), 1) })
SparkR:::takeRDD(products, 5)
productCount <- SparkR:::reduceByKey(products, "+", 2L)
productsCountAsKey <- SparkR:::lapply(productCount, function(x) { list( as.integer(x[2][1]), x[1][1])})

productCount <- SparkR:::countRDD(productsCountAsKey)
mostPopular <- toString(SparkR:::collectRDD(productsCountAsKey)[[productCount]][[2]])
sprintf("Most Popular Product : %s", mostPopular)

# stop the current session
sparkR.session.stop()
