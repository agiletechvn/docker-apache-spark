package linalg.vector

import breeze.linalg._
import breeze.stats.mean

/**
  * Created by manpreet.singh on 23/01/16.
  */
object SparseVectorSample {

  def main(args: Array[String]) {

    val sv:SparseVector[Double] = SparseVector(5)()
    // key from 0-5, key,value as x,y of vector
    sv(0) = 1
    sv(3) = 3
    sv(2) = 7
    val m = sv.mapActivePairs((i,x)=>x+1)
    println(m)

  }


}