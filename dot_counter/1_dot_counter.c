#include <stdio.h>
#include <stdlib.h>

#define INPUT_DIR "in.txt"
#define OUTPUT_DIR "out.txt"
#define MAX_LEN 20
#define SIZE_ROW 8
#define SIZE_COL 4


int main()
{
	FILE *fpi = fopen(INPUT_DIR, "r");
    FILE *fpo = fopen(OUTPUT_DIR, "w");
    char cNum[MAX_LEN];
    double block_height = (double)(200) / SIZE_ROW;
    double block_width  = (double)(200) / SIZE_COL;
    double x, y;
    int t;
    int row, col;
    int t_sum[SIZE_ROW][SIZE_COL];
    int counter[SIZE_ROW][SIZE_COL];
    int t_avg[SIZE_ROW][SIZE_COL];
    int i, j;
    for(i=0; i<SIZE_ROW; i++)
    {
        for(j=0; j<SIZE_COL; j++)
        {
            t_sum[i][j] = 0;
            counter[i][j] = 0;
        }
    }    

    // read from input and sort
    // fscanf stops at \n or \t
    // read a line (N0. & x & y & t) each loop
    while(fscanf(fpi, "%s", cNum) == 1)
    {
        fscanf(fpi, "%s", cNum);
        // x, y have an offset of -100
        x = (double)(atoi(cNum) + 100);
        fscanf(fpi, "%s", cNum);
        y = (double)(atoi(cNum) + 100);
        fscanf(fpi, "%s", cNum);
        t = atoi(cNum);

        row = (int)(y / block_height);
        col = (int)(x / block_width);

        // could be out of range when x or y is 200
        if(row == SIZE_ROW) row--;
        if(col == SIZE_COL) col--;

        t_sum[row][col] += t;
        counter[row][col] ++;
    }

    // calculate the average time and print to output
    for(i=0; i<SIZE_ROW; i++)
    {
        for(j=0; j<SIZE_COL; j++)
        {
            if(counter[i][j]) 
                t_avg[i][j] = t_sum[i][j] / counter[i][j];
            else
                t_avg[i][j] = 0;
            fprintf(fpo, "%d \t", t_avg[i][j]);
        }
        fprintf(fpo, "\n");
    }
    fclose(fpi);   
    fclose(fpo);
} 