
#include <stdio.h>

int main(void) {
    int n;  //가로의 길이
    int m;  //세로의 길이
    int i,j;

    scanf("%d %d", &n, &m);
    if(n>1000)
    {
        printf("row is under than 1000");
        return 0;
    }
    else
    {
        if(m>1000)
            printf("colum is under than 1000");
        else
        {
            for(j=1; j<=m; j++)
            {
                for(i=1; i<=n; i++)
                printf("*");
            printf("\n");
            }

        }


    }

    return 0;
}