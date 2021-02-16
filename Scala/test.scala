import scala.io.StdIn.{readLine, readInt}
import scala.math._
import scala.collection.mutable.ArrayBuffer
import java.io.PrintWriter
import scala.io.Source

object basic{
    def main(args: Array[String]){
        var guessedNumber = 0
       
       do{
           print("guess the number: ")
           guessedNumber = readLine.toInt
       }while(guessedNumber != 10)

       printf("You guessed the special number: %d\n", guessedNumber )
       
    }
       
}