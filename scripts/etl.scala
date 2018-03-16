import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType}

val sqlContext = new SQLContext(sc)
val customSchema = StructType(Array(    
    StructField("last_name", StringType, true),
    StructField("first_name", StringType, true)))

val df = sqlContext.read.format("json").option("header", "true").schema(customSchema).load("/tmp/data/input.json")

val selectedData = df.select("first_name", "last_name")
selectedData.write.format("csv").option("header", "true").save("/tmp/data/output.csv")

System.exit(0)