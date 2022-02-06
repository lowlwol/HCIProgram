# include <stdio.h>

int main()
{
    FILE *fpi, *fpo;
    fpi = fopen("Matrix.txt", "r");
    fpo = fopen("Matrix_R.txt", "w");
    int i, j;
    char c;
    fprintf(fpo, "[[");
    while((c=fgetc(fpi)) != EOF)
    {
        if     (c == '\t') fprintf(fpo, ", ");
        else if(c == '\n') fprintf(fpo, "], [");
        else               fprintf(fpo, "%c", c);
    }
    fprintf(fpo, "]");

    fclose(fpi);
    fclose(fpo);
}