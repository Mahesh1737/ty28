import java.io.*;
import java.util.*;

class Ass4A2
{
      public static void main(String[] args) throws IOException
      {
             FileReader f= new FileReader("mm.txt");
             Scanner sc = new Scanner(f);
             String ch, ch2;
             while (sc.hasNext())
             {
                   StringBuilder ch1 = new StringBuilder();
                   ch = sc.next();
                   ch2 = ch.toUpperCase();
                   ch1.append(ch2);
                   ch1.reverse();
                   System.out.println(ch1);
              }
              f.close();
       }
}
/*
Output:

ty28@pc58:~/TY28/JAVA/ASSIGNMENT_04/SET_A$ java Ass4A2
HSEHAM
EROM
CSBYT
TNAILLIRB
TNEDUTS
*/
