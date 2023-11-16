#include <stdio.h>
#include <stdlib.h>

struct fnode{
    int pno;
    int freq;
}frame[5];

int str[30],fr,n,pno1;

int pagefound(int pno1)
{
    for (int i=0;i<fr;i++)
        if (frame[i].pno==pno1)
           return i;
    return -1;
}

int free_pg()
{
    for (int i=0;i<fr;i++)
        if (frame[i].pno==-1)
           return i;
    return -1;
}

int getmru()
{
    int max=0;
    for (int i=0;i<fr;i++)
        if (frame[i].freq > frame[max].freq)
           max=i;
    return max;
}

int main()
{
    int flag=0, cnt=0, fcnt=0;

    printf("Enter the No of frames : ");
    scanf("%d",&fr);
    printf("Enter the No String elelments : ");
    scanf("%d",&n);
    for (int i=0;i<n;i++)
    {
        printf("Enter the String : ");
        scanf("%d",&str[i]);
    }

    for (int i=0;i<fr;i++)
    {
        frame[i].pno = -1;
        frame[i].freq = 0;
    }

    // int ctime;
    printf("\nPageNo\t Frames\t   States\t Frequency\n");
    for (int i=0;i<n;i++)
    {
        pno1 = str[i];
        flag=0;
        int j = pagefound(pno1);
        if (j==-1)
        {
            fcnt++;
            j=free_pg();
            if (j==-1)
               j = getmru();
            frame[j].pno = pno1;   
            flag=1;
            frame[j].freq=1;
        }
        else
            frame[j].freq++;

        printf(" %d\t",pno1);

        for (int i=0;i<fr;i++)
            printf(" %d ",frame[i].pno);
        if (flag==1)
           printf("\tYes\t%d\n",frame[j].freq);
        else
        {
            printf("\tNo\t%d\n",frame[j].freq);
            cnt++;
        }
        // printf(" %d\n",frame[i].freq);
    }
    printf("\nTotal No of page fault : %d",fcnt);
    printf("\nTotal No of page Hit : %d\n\n",cnt);
}

/*PS F:\backup -6-1-2023\Users\dell\TYBSc_CS_23\OS> cd "f:\backup -6-1-2023\Users\dell\TYBSc_CS_23\OS\" ; if ($?) { gcc test.c -o test } ;
if ($?) { .\test }
Enter the No of frames : 3
Enter the No String elelments : 16
Enter the String : 12
Enter the String : 15
Enter the String : 12
Enter the String : 18
Enter the String : 6
Enter the String : 8
Enter the String : 11
Enter the String : 12
Enter the String : 19
Enter the String : 12
Enter the String : 6
Enter the String : 8
Enter the String : 12
Enter the String : 15
Enter the String : 19
Enter the String : 8

PageNo   Frames   States          Frequency
 12      12  -1  -1     Yes     1
 15      12  15  -1     Yes     1
 12      12  15  -1     No      2
 18      12  15  18     Yes     1
 6       6  15  18      Yes     1
 8       8  15  18      Yes     1
 11      11  15  18     Yes     1
 12      12  15  18     Yes     1
 19      19  15  18     Yes     1
 12      12  15  18     Yes     1
 6       6  15  18      Yes     1
 8       8  15  18      Yes     1
 12      12  15  18     Yes     1
 15      12  15  18     No      2
 19      12  19  18     Yes     1
 8       8  19  18      Yes     1

Total No of page fault : 14
Total No of page Hit : 2
*/
