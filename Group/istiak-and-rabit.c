#include <stdio.h>
#include <string.h>
#include <math.h>
int main()
{
    char str1[100] = "2 3 2";
    char newString[10][10];
    int i, j, ctr;
    fgets(str1, sizeof str1, stdin);
    j = 0;
    ctr = 0;
    for (i = 0; i <= (strlen(str1)); i++)
    {
        if (str1[i] == ' ' || str1[i] == '\0')
        {
            newString[ctr][j] = '\0';
            ctr++; //for next word
            j = 0; //for next word, init index to 0
        }
        else
        {
            newString[ctr][j] = str1[i];
            j++;
        }
    }
    int ind = 0;
    int z = 0;
    int a = atoi(newString[0]);
    int r = atoi(newString[1]);
    int n = atoi(newString[2]);
    while (n > 0)
    {

        z += (a * pow(r,(n - 1)));
        n -= 1;
    };

    printf("%d", z);

    return 0;
}

