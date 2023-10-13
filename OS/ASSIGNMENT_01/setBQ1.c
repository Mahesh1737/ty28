#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<sys/wait.h>

void bubblesort(int [], int);
void insertionsort(int [], int);
void ChildProcess(int);
void ParentProcess(int);


void main()
{
     int n, pid , arr[10];
     printf("\nEnter Size of array : ");
     scanf("%d",&n);
     printf("\nEnter %d array element : ",n);
     for (int i=0;i<n;i++)
     {
         scanf("%d",&arr[i]);
     }
     
     printf("\nArray elements are : ",n);
     for (int i=0;i<n;i++)
     {
         printf(" %d ",arr[i]);
     }
     
     
    pid=fork();
    if (pid==0)
    {
       //ChildProcess(pid);
       insertionsort(arr, n);
    }
    else if(pid > 0)
    {
       wait(NULL);
       //ParentProcess(pid);
       bubblesort(arr, n);
    }
    else
          printf("\nUnsuccessful execution preocess not created \n");
}

void ChildProcess(int pid)
{
     printf("\nI am Child Process..............\n");
     printf("I am Parent Process ID : %d \n",getpid());
     printf("My Child Process ID : %d \n\n",getppid());
}

void ParentProcess(int pid)
{
     printf("\nI am Parent process.............\n");
     printf("I am Parent Process ID : %d \n",getpid());
     printf("My Child Process ID : %d \n\n",pid);
}

void bubblesort(int arr[], int n)
{
     printf("Bubble sort is : ");
     for (int i=0;i<n;i++)
         for (int j=0;j<n;j++)
         {
             if (arr[j] > arr[j+1])
             {
                int temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
             }
         }
}

void insertionsort(int arr[], int n)
{
    int i, key, j;
    printf("Insertion sort is : ");
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
 
        /* Move elements of arr[0..i-1],
           that are greater than key,
           to one position ahead of
           their current position */
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
    
