#include <stdio.h>
#include <stdlib.h>
void main()
{
     int i,n;
     float avwt=0, avtat=0;
     printf("Enter the Number of process :");
     scanf("%d",&n);
     
     int at[n], bt[n],wt[n], tat[n];
     printf("Enter the Arrival time : ");
     for (i=0;i<n;i++)
         scanf("%d",&at[i]);
     
    // printf("Enter the Burst time : ");
     for (i=0;i<n;i++)
     {
         bt[i] = rand()%10;
     }
     
     int temp[10];
     temp[0] = 0;
     for (i=1;i<n;i++) 
     {

         temp[i]= temp[i-1] + bt[i-1];
         
     }
     for (i=0;i<n;i++)
     {
         wt[i]=temp[i] - at[i]; 
         avwt+=wt[i];
         tat[i]=at[i] + bt[i];
         avtat+=tat[i]; 
     }
     avwt/=n;
     avtat/=n;
     printf("\npro\tat\tbt\twt\ttat");
     for (i=0;i<n;i++)
     {
         printf("\np%d\t%d\t%d\t%d\t%d\t",i+1,at[i],bt[i],wt[i],tat[i]);
     }
     printf("\nAverage Waiting Time : %f\nAverage turn around time : %f\n\n",avwt,avtat);
}
            
/*

Output :




ty28@pc56:~/TY28/OS/ASSIGNMENT_03/Set_B$ ./a.out
Enter the Number of process :4
Enter Processes : 1 2 3 4
Enter the Arrival time : 0 0 0 0
Enter the Burst time : 3 2 5 7

pro	at	bt	wt	tat : 

1	0	2	0	2

2	0	3	2	5

3	0	5	5	10

4	0	7	10	17

Average Waiting Time  is : 4.250000


Average turn around Time  is: 8.500000

            
*/
     
