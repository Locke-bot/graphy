// C++ program to demonstrate working of Guassian Elimination
// method
#include<bits/stdc++.h>
using namespace std;
 
#define N 9       // Number of unknowns
 
// function to reduce matrix to r.e.f.  Returns a value to
// indicate whether matrix is singular or not
int forwardElim(double mat[N][N+1]);
 
// function to calculate the values of the unknowns
void backSub(double mat[N][N+1]);
 
// function to get matrix content
void gaussianElimination(double mat[N][N+1])
{
    /* reduction into r.e.f. */
    int singular_flag = forwardElim(mat);
 
    /* if matrix is singular */
    if (singular_flag != -1)
    {
        printf("Singular Matrix.\n");
 
        /* if the RHS of equation corresponding to
           zero row  is 0, * system has infinitely
           many solutions, else inconsistent*/
        if (mat[singular_flag][N])
            printf("Inconsistent System.");
        else
            printf("May have infinitely many "
                   "solutions.");
 
        return;
    }
 
    /* get solution to system and print it using
       backward substitution */
    backSub(mat);
}
 
// function for elementary operation of swapping two rows
void swap_row(double mat[N][N+1], int i, int j)
{
    //printf("Swapped rows %d and %d\n", i, j);
    // cout <<  "pre swap1 shit " << i << " " << j <<endl;
    // for (int y=0; y < N; y++){
    //     for (int z=0; z < N+1; z++){
    //         cout << mat[y][z] << "   ";
    //     }
    //     cout << endl;
    // }     
    for (int k=0; k<=N; k++)
    {
        float temp = mat[i][k];
        cout << "swappo" << temp << " " << mat[j][k]<<endl;
        mat[i][k] = mat[j][k];
        mat[j][k] = temp;
    }
    // cout <<  "post swap1" << endl;
    // for (int y=0; y < N; y++){
    //     for (int z=0; z < N+1; z++){
    //         cout << mat[y][z] << "   ";
    //     }
    //     cout << endl;
    // }    
    // cout << "end post shit" << endl;    
}
 
// function to print matrix content at any stage
void print(double mat[N][N+1])
{
    for (int i=0; i<N; i++, printf("\n"))
        for (int j=0; j<=N; j++)
            printf("%lf ", mat[i][j]);
 
    printf("\n");
}
 
// function to reduce matrix to r.e.f.
int forwardElim(double mat[N][N+1])
{
    for (int k=0; k<N; k++)
    {
        // Initialize maximum value and index for pivot
        int i_max = k;
        float v_max = mat[i_max][k];
        cout << "I_MAX" << i_max << endl;
        /* find greater amplitude for pivot if any */
        for (int i = k+1; i < N; i++){
            cout << abs(mat[i][k]) << "abs" << v_max << " " << (abs(mat[i][k]) > v_max) << endl;
            if (abs(mat[i][k]) > v_max)
                v_max = mat[i][k], i_max = i;
        }

        /* if a prinicipal diagonal element  is zero,
         * it denotes that matrix is singular, and
         * will lead to a division-by-zero later. */
        if (!mat[k][i_max])
            return k; // Matrix is singular
        // cout <<  "pre swap1" << endl;
        // for (int y=0; y < N; y++){
        //     for (int z=0; z < N+1; z++){
        //         cout << mat[y][z] << "   ";
        //     }
        //     cout << endl;
        // }
        // cout << "end pre_swap" << endl; 
        /* Swap the greatest value row with current row */
        if (i_max != k){
            cout << "swap_row" << k << " k, i_max" << i_max << endl;
            swap_row(mat, k, i_max);
        }
 
        for (int i=k+1; i<N; i++)
        {
            /* factor f to set current row kth element to 0,
             * and subsequently remaining kth column to 0 */
            cout << "shit matrcx start" << endl;
            for (int y=0; y < N; y++){
                for (int z=0; z < N+1; z++){
                    cout << mat[y][z] << "   ";
                }
                cout << endl;
            }                 
            double f = mat[i][k]/mat[k][k];
            cout << i << " " << k << endl;
            cout << mat[i][k] << "_shit_" << mat[k][k] << " "<< f << endl;
            /* subtract fth multiple of corresponding kth
               row element*/
            cout << "shit curiously" << endl;
            for (int j=k+1; j<=N; j++){
                cout << mat[i][j] << " " << mat[k][j] << " " << f << endl;
                mat[i][j] -= mat[k][j]*f;
                cout << mat[i][j] << endl;
            }
            cout << "shit ended seroiusly" << endl;
            /* filling lower triangular matrix with zeros*/
            // mat[i][k] = 0;
            for (int y=0; y < N; y++){
                for (int z=0; z < N+1; z++){
                    cout << mat[y][z] << "   ";
                }
                cout << endl;
            }                 
            cout << "shit matrcx end" << endl;
        }
 
        //print(mat);        //for matrix state
    }
    //print(mat);            //for matrix state
    return -1;
}
 
// function to calculate the values of the unknowns
void backSub(double mat[N][N+1])
{
    double x[N];  // An array to store solution
 
    /* Start calculating from last equation up to the
       first */
    for (int i = N-1; i >= 0; i--)
    {
        /* start with the RHS of the equation */
        x[i] = mat[i][N];
 
        /* Initialize j to i+1 since matrix is upper
           triangular*/
        for (int j=i+1; j<N; j++)
        {
            /* subtract all the lhs values
             * except the coefficient of the variable
             * whose value is being calculated */
            x[i] -= mat[i][j]*x[j];
        }
 
        /* divide the RHS by the coefficient of the
           unknown being calculated */
        x[i] = x[i]/mat[i][i];
    }
 
    printf("\nSolution for the system:\n");
    for (int i=0; i<N; i++)
        printf("%lf\n", x[i]);
}
 
// Driver program
int main()
{
    /* input matrix */
    Fraction mat[N][N+1] =  {{Fraction("3", "1"), Fraction("2", "1"), Fraction("-4", "1"), Fraction("3", "1"), Fraction("9", "1"), Fraction("76000", "1")},
 {Fraction("2", "1"), Fraction("3", "1"), Fraction("3", "1"), Fraction("15", "1"), Fraction("8000", "1"), Fraction("45", "1")},
 {Fraction("5", "1"), Fraction("-3", "1"), Fraction("1", "1"), Fraction("12", "1"), Fraction("-4", "1"), Fraction("56", "1")},
 {Fraction("23", "1"), Fraction("13", "1"), Fraction("-4459483456787745585781", "1"), Fraction("12", "1"), Fraction("6", "1"), Fraction("-9", "1")},
 {Fraction("-2", "1"), Fraction("12", "1"), Fraction("21", "1"), Fraction("19", "1"), Fraction("-7", "1"), Fraction("4", "1")}};
//     double mat[N][N+1] = {{0, 0, 0, 0, 0, 0, 0, 0, 1, 5},
//  {1, 1, 1, 1, 1, 1, 1, 1, 1, 9},
//  {256, 128, 64, 32, 16, 8, 4, 2, 1, 13},
//  {6561, 2187, 729, 243, 81, 27, 9, 3, 1, 17},
//  {65536, 16384, 4096, 1024, 256, 64, 16, 4, 1, 21},
//  {390625, 78125, 15625, 3125, 625, 125, 25, 5, 1, 25},
//  {1679616, 279936, 46656, 7776, 1296, 216, 36, 6, 1, 29},
//  {5764801, 823543, 117646798768999, 16807, 2401, 343, 49, 7, 1, 33},
//  {16777216, 2097152, 262144, 32762098498, 4096, 512, 64, 8, 1, 37}};
 
    gaussianElimination(mat);
 
    return 0;
}