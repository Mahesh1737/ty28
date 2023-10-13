#include<stdio.h>
#include<sys/types.h>
//#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>
//void ChildProcess(int);
//void ParentProcess(int);
void bubble_sort();
void insertion_sort();
int a[10],n;
void bubble_sort()
{
     int i,j,temp;
     for (i=0;i<n-1;i++)
         for (j=0;j<n-1-i;j++)
         {
             if (a[j]>a[j+1])
             {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
             }   
         }
}

void insertion_sort()
{
     int i,j,key;
     for (i=1;i<n;i++)
     {
         key=a[i];
         j=i-1;
         for(j>0;a[j]>key;j--)
         {
               a[j+1]=a[j];
               
         }
         a[j+1]=key;
      }
}               
        

int main()
{
    int i;
    printf("Enter the size of array:");
    scanf("%d",&n);
    
    printf("Enter array elements : ");
    for (i=0;i<n;i++)
        scanf("%d",&a[i]);
    printf("Array Elements : ");
    for (i=0;i<n;i++)
        printf("%d\t",a[i]);  
    printf("\n");
    
    pid_t pid;
    pid=fork();
    
    if (pid==0)
    {
       printf("\nI am child process..");
       printf("\nMy Id: %d",getpid());
       bubble_sort();
       printf("\nSorted array element using bubble sort: ");
       for (i=0;i<n;i++)
       printf("%d\t",a[i]);  
       
       printf("\n");
    }
    
    else
        if (pid>0)
        {
            wait(NULL);
            printf("I am parent process");
            printf("\nMy Id: %d\n",getpid());
            insertion_sort() ;
            printf("\nSorted array element using insertion sort : ");
            for (i=0;i<n;i++)
            printf("%d\t",a[i]);  
       
            printf("\n");
        }
   
}


/*

Output :

ty28@pc61:~/TY28/OS/ASSIGNMENT_01$ cc ass1b1.c
ty28@pc61:~/TY28/OS/ASSIGNMENT_01$ ./a.out
Enter the size of array:5
Enter array elements : 4
5
6
3
2
Array Elements : 4	5	6	3	2	

I am child process..
My Id: 18282
Sorted array element using bubble sort: 2	3	4	5	6	
I am parent process
My Id: 18275

Sorted array element using insertion sort : 2	3	4	5	6	

*/
 

