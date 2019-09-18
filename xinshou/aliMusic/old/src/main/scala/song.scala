import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

object song{
  def main(args: Array[String]){
    val conf = new SparkConf().setMaster("local").setAppName("tianchi")
    val sc = new SparkContext(conf)

    val songs = sc.textFile("data/mars_tianchi_songs.csv").map(x => x.split(",")).cache()

    //每个艺人有多少歌曲
    val arts_songNum = songs.map{x => (x(1), x(0))}.groupByKey().mapValues(x => x.size)

    //艺人有多少,歌曲有多少
    val arts_Num = arts_songNum.count()
    val songsNum = songs.count()
    arts_songNum.take(10).foreach(println)

    val arts_song_init = songs.map(x => (x(1), (x(2), x(3)))).groupByKey()//.mapValues{(x1, x2) =>
    val sortedSongByHot = arts_song_init.mapValues{x => x.toArray.sortBy(y => (y._1.toInt, y._2.toInt))}


    arts_song_init.take(10).foreach(println)
    val aArts = arts_song_init.first._2
    val tt = aArts.map(x => (x._1.toInt, x._2.toInt))//.sortBy(x._1)
    tt.foreach(println)
    sc.stop()
  }
}
