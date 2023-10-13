import java.io.*;
import java.util.*;

 class Patient {
     int id;
     String pname;
     int age;
     int p_oxy_lev;
     int p_HRCT;
     
    Patient(int id, String pname,int age, int p_oxy_lev, int p_HRCT ) 
    {
        this.id = id;
        this.pname = pname;
        this.age = age;
        this.p_oxy_lev = p_oxy_lev;
        this.p_HRCT = p_HRCT;
    } 


    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("\nEnter the number Patients: ");
        int n = sc.nextInt();
        Patient pt[] = new Patient[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter id: ");
            int r = sc.nextInt();
            System.out.print("Enter Name of Patient: ");
            String r1 = sc.next();
            System.out.print("Enter Age of Patient: ");
            int  nm = sc.nextInt();
            System.out.print("Enter Oxygen lev of patient: ");
            int dm = sc.nextInt();
            System.out.print("Enter HCRT OF patient: ");
            int dn = sc.nextInt();

            pt[i] = new Patient(r, r1, nm, dm, dn);
        }
        
        for(int j=0;j<n;j++)
        {
           if(pt[j].p_oxy_lev < 95 && pt[j].p_HRCT > 10)
           {
              try
              {
                    throw new NullPointerException();
              }
              catch(Exception e)
              {
                   System.out.print("\n Patient "+pt[j].pname+"is covid Positive....... : ");
              }
              
           }
           else
           {
                   System.out.print("\n Patient Name :  "+pt[j].pname);
                   System.out.print("\n Patient Age :  "+pt[j].age);
                   System.out.print("\n Patient Oxy level :  "+pt[j].p_oxy_lev);
                   System.out.print("\n Patient HCRT :  "+pt[j].p_HRCT);
           }
    }
  }
}


/*


Output :

ty28@pc57:~/TY28/JAVA/ASSIGNMENT_04/SET_A$ java Patient

Enter the number Patients: 2
Enter id: 1
Enter Name of Patient: ma
Enter Age of Patient: 55
Enter Oxygen lev of patient: 94
Enter HCRT OF patient: 12
Enter id: 2
Enter Name of Patient: mk
Enter Age of Patient: 45
Enter Oxygen lev of patient: 96
Enter HCRT OF patient: 23

 Patient mais covid Positive....... : 
 Patient Name :  mk
 Patient Age :  45
 Patient Oxy level :  96
 Patient HCRT :  23ty28@pc57:~/TY28/JAVA/ASSIGNMENT_04/SET_A$ 



*/
