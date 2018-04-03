name := "scala-spark-app"

version := "1.1.1"

scalaVersion := "2.11.8"

val sparkVersion = "2.3.0"

libraryDependencies += "org.apache.spark" %% "spark-core" % sparkVersion
libraryDependencies += "org.apache.spark" %% "spark-mllib" % sparkVersion

    
