import sy.*;
import ty.*;
import java.io.*;
import java.util.*;

class student
{
      int rno;
      int tytm,sytm,gt;
      double per;
      String name;
      
      student(int rno, String name)
      {
             this.rno = rno;
             this.name = name;
      }
      public static void main(String args[])
       {
             Scanner sc = new Scanner(System.in);
             System.out.print("Enter the Number of Student : ");
             int n = sc.nextInt();
             student s[] = new student[n];    
             Symarks sy[] = new Symarks[n];  
             Tymarks ty[] = new Tymarks[n];  
             for (int i=0;i<n;i++)   
             {
                 System.out.print("\nEnter the roll no of the student : ");
                 int r = sc.nextInt();
                 
                 System.out.print("\nEnter the Name of Student : ");
                 String name = sc.next();
                 
                 System.out.print("Enter the marks of sy computer total out of 200 : ");
                 int c = sc.nextInt();
                 
                 System.out.print("Enter the marks of sy math total out of 200 : ");
                 int m = sc.nextInt();

                 System.out.print("Enter the marks of sy Electronics total out of 200 : ");
                 int e = sc.nextInt();

                 System.out.print("Enter the marks of ty Theory total out of 200 : ");
                 int th = sc.nextInt();

                 System.out.print("Enter the marks of ty Practical total out of 200 : ");
                 int pr = sc.nextInt();


                 //System.out.print("Enter the percentage of Student : ");
                 //float p = sc.nextFloat();
                 
                 s[i] = new student(r, name);
                 sy[i] = new Symarks(c, m, e);
                 ty[i] = new Tymarks(th, pr);
                 
                 //st[i].sytm = sy[i].ct+sy[i].mt+sy[i].et;
                // st[i].tytm = sy[i].ct+sy[i].mt+sy[i].et;
                 
                 
             }
             System.out.println("\n Roll no\tName\tcomTotal\tmathTotal\tElcTotal\tTheory\tprc: ");
             for (int i=0;i<n;i++)
             System.out.println( s[i].rno+"\t\t"+s[i].name+"\t"+sy[i].ct+"\t\t"+sy[i].mt+"\t\t"+sy[i].et+"\t\t"+ty[i].tm+"\t"+ty[i].pm); 
            
       }
}
