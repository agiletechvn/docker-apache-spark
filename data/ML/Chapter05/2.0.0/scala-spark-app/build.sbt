name := "scala-spark-app"

version := "1.1.1"
val sparkVersion = "2.3.0"
scalaVersion := "2.11.8"


libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-mllib" % sparkVersion
)

// https://mvnrepository.com/artifact/org.jblas/jblas
libraryDependencies += "org.jblas" % "jblas" % "1.2.4"
libraryDependencies += "com.github.scopt" %% "scopt" % "3.2.0"

libraryDependencies += "com.github.fommil.netlib" % "all" % "1.1.2" pomOnly()

// libraryDependencies += "net.sourceforge.f2j" % "arpack_combined_all" % "0.1"
// libraryDependencies += "com.github.fommil.netlib" % "netlib-native_ref-linux-x86_64" % "1.1" classifier "natives"
// libraryDependencies += "com.github.fommil.netlib" % "netlib-native_system-linux-x86_64" % "1.1" classifier "natives"

resolvers ++= Seq(
  "Apache Repository" at "https://repository.apache.org/content/repositories/releases"
)
    