#include <stdio.h>

int main()
{
    int n;
    printf("Enter the of processs : ");
    scanf("%d", &n);

    int at[n], bt[n], rt[n], ct, remain = 0, time = 0;
    int avgtat = 0, avgwt = 0, smallest;
    
    for (int i = 0; i < n; i++)
    {
        printf("Enter the arrival time : ");
        scanf("%d", &at[i]);
    }
    for (int i = 0; i < n; i++)
    {
        printf("Enter the Burst time : ");
        scanf("%d", &bt[i]);
        rt[i] = bt[i];
    }

    printf("\nProcess\tAt\tBt\tWt\tTat\n");
    for (time = 0; remain != n; time++)
    {
        smallest = -1;
        for (int i = 0; i < n; i++)
        {
            if (at[i] <= time && rt[i]>0 && (smallest==-1 || rt[i] < rt[smallest]))
                smallest = i;
        }
        rt[smallest]--;

        if (rt[smallest] == 0)
        {
            remain++;
            ct = time + 1;
            printf("\n P[%d] \t%d\t%d\t%d\t%d ", smallest + 1, at[smallest], bt[smallest], ct - bt[smallest] - at[smallest], ct - at[smallest]);
            avgtat+=(ct - at[smallest]);
            avgwt+=(ct - bt[smallest] - at[smallest]);
        }
    }
    avgtat /= n;
    avgwt /= n;

    printf("\n");
    printf("\nTotal avgTaT : %d", avgtat);
    printf("\nTotal avgwt : %d\n", avgwt);

    return 0;
}

/*
Output : 

Enter the of processs : 3
Enter the arrival time : 0
Enter the arrival time : 1
Enter the arrival time : 2
Enter the Burst time : 4
Enter the Burst time : 3
Enter the Burst time : 6

Process At      Bt      Wt      Tat

 P[1]   0       4       0       4
 P[2]   1       3       3       6
 P[3]   2       6       5       11

Total avgTaT : 7
Total avgwt : 2

*/