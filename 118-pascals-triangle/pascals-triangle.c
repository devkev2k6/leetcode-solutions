#include <stdlib.h>
int** generate(int numRows,int* returnSize,int** returnColumnSizes){
    *returnSize=numRows;
    int** triangle = (int**)malloc(numRows*sizeof(int*));
    *returnColumnSizes=(int*)malloc(numRows*sizeof(int));
    for(int i=0;i<numRows;i++){
        int rowSize=i+1;
        (*returnColumnSizes)[i] = rowSize;
        triangle[i]=(int*)malloc(rowSize*sizeof(int));
        triangle[i][0]=1;
        triangle[i][rowSize-1]=1;
        for(int j=1;j<rowSize-1;j++){
            triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j];
        }
    }
    return triangle;
}