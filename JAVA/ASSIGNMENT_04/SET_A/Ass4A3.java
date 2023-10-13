import java.io.*;
import java.util.*;

class Ass4A3
{
      public static void main(String[] args) throws IOException
      {
             FileReader f= new FileReader("mm.txt");
             FileWriter f1= new FileWriter("mm1.txt");
             Scanner sc = new Scanner(f);
             String ch;
             while (sc.hasNext())
             {
                   
                   ch = sc.nextLine();
                   f1.write(ch);
                   
                   

              }
              System.out.println("Copy Finished......");
              f.close();
              f1.close();
       }
}
/*
Output :

ty28@pc58:~/TY28/JAVA/ASSIGNMENT_04/SET_A$ javac Ass4A3.java
ty28@pc58:~/TY28/JAVA/ASSIGNMENT_04/SET_A$ java Ass4A3
Copy Finished......
*/
