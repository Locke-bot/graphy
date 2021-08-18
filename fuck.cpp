#include<chrono>
#include "fraction.cxx"
#include<time.h>
// C++ program to demonstrate working of Guassian Elimination
// method
#include<bits/stdc++.h>
using namespace std;
 
#define N 9        // Number of unknowns
// function to reduce matrix to r.e.f.  Returns a value to
// indicate whether matrix is singular or not
int forwardElim(Fraction mat[N][N+1]);
 
// function to calculate the values of the unknowns
Fraction * backSub(Fraction mat[N][N+1]);

// function to get matrix content
Fraction * gaussianElimination(Fraction mat[N][N+1])
{
    /* reduction into r.e.f. */
    int singular_flag = forwardElim(mat);
    // cout << singular_flag << endl;
    /* if matrix is singular */
    if (singular_flag != -1)
    {
        printf("Singular Matrix.\n");
 
        /* if the RHS of equation corresponding to
           zero row  is 0, * system has infinitely
           many solutions, else inconsistent*/
        if (mat[singular_flag][N])
            throw "Inconsistent System.";
        else
            throw "May have infinitely many solutions.";
    }
 
    /* get solution to system and print it using
       backward substitution */
    return backSub(mat);
}

// function for elementary operation of swapping two rows
void swap_row(Fraction mat[N][N+1], int i, int j)
{
    // printf("Swapped rows %d and %d\n", i, j);
    // cout <<  "pre swap1 fuck " << i << " " << j <<endl;
    // for (int y=0; y < N; y++){
    //     for (int z=0; z < N+1; z++){
    //         cout << mat[y][z] << "   ";
    //     }
    //     cout << endl;
    // }    
    for (int k=0; k<=N; k++)
    {
        Fraction temp = mat[i][k];
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
    // cout << "end post" << endl;
}
 
// function to reduce matrix to r.e.f.
int forwardElim(Fraction mat[N][N+1])
{
    for (int k=0; k<N; k++)
    {
        // Initialize maximum value and index for pivot
        int i_max = k;
        // std::string s = std::to_string(mat[i_max][k].toInt());
        // const char* t = s.c_str();
        // t << mat[i_max][k].toInt();
        // cout << t << " SHOUT AM" << endl;
        Fraction v_max = Fraction(std::to_string(mat[i_max][k].toInt()).c_str());
        cout << "I_MAX" << i_max << endl;
        /* find greater amplitude for pivot if any */
        for (int i = k+1; i < N; i++){
            cout << mat[i][k].abso() << "abs" << v_max << " " << (mat[i][k].abso() > v_max) << endl;
            if (mat[i][k].abso() > v_max){
                v_max = mat[i][k], i_max = i;
            }
        }
        /* if a prinicipal diagonal element  is zero,
         * it denotes that matrix is singular, and
         * will lead to a division-by-zero later. */
        if (!mat[k][i_max]){
            return k; // Matrix is singular
        }
        /* Swap the greatest value row with current row */
        // cout <<  "pre swap1" << endl;
        // for (int y=0; y < N; y++){
        //     for (int z=0; z < N+1; z++){
        //         cout << mat[y][z] << "   ";
        //     }
        //     cout << endl;
        // }
        // cout << "end pre_swap" << endl;
        if (i_max != k){
            cout << "swap_row" << k << " k, i_max" << i_max << endl;
            swap_row(mat, k, i_max);
        }
        for (int i=k+1; i<N; i++)
        {
            /* factor f to set current row kth element to 0,
             * and subsequently remaining kth column to 0 */
            cout << "fuck matrcx start" << endl;            
            for (int y=0; y < N; y++){
                for (int z=0; z < N+1; z++){
                    cout << mat[y][z] << "   ";
                }
                cout << endl;
            }                 
            Fraction f = mat[i][k]/mat[k][k];
            cout << i << " " << k << endl;
            cout << mat[i][k] << "__" << mat[k][k] << " "<< f << endl;
            /* subtract fth multiple of corresponding kth
               row element*/
            cout << "fuck curiously" << endl;
            for (int j=k+1; j<=N; j++){
                cout << mat[i][j] << " " << mat[k][j] << " " << f << endl;
                mat[i][j] -= mat[k][j]*f;
                cout << mat[i][j] << endl;
            }
            cout << "fuck ended seroiusly" << endl;                
            /* filling lower triangular matrix with zeros*/
            mat[i][k] = Fraction("0");
            for (int y=0; y < N; y++){
                for (int z=0; z < N+1; z++){
                    cout << mat[y][z] << "   ";
                }
                cout << endl;
            }                 
            cout << "fuck matrcx end" << endl;            
        }
    }
    return -1;
}
 
// function to calculate the values of the unknowns
Fraction * backSub(Fraction mat[N][N+1])
{
    // cout << "visiting" << endl;
    Fraction x[N];  // An array to store solution
 
    /* Start calculating from last equation up to the
       first */
    for (int i = N-1; i >= 0; i--)
    {
        /* start with the RHS of the equation */
        x[i] = mat[i][N];
        // cout << "yftff " << x[i] << endl;
        /* Initialize j to i+1 since matrix is upper
           triangular*/
        for (int j=i+1; j<N; j++)
        {
            /* subtract all the lhs values
             * except the coefficient of the variable
             * whose value is being calculated */
            cout << x[i] << endl;
            x[i] -= mat[i][j]*x[j];
        }
 
        /* divide the RHS by the coefficient of the
           unknown being calculated */
        x[i] = x[i]/mat[i][i];
        // cout << x[i] << endl;
    }
    cout << "solution ready";
    Fraction fracarray[N];
    for (int i=0; i<N; i++){
        cout << x[i] << endl;
        fracarray[i] = x[i];
        //printf("%lf\n", x[i]);
    }
    return fracarray;
}

// Driver program
int main()
{
    /* input matrix */
    auto begin = std::chrono::high_resolution_clock::now();
    //time_t begin, end;
    //time(&begin);
    // Fraction mat[N][N+1] =    {{Fraction("3"), Fraction("2"), Fraction("-4"), Fraction("3"), Fraction("9"), Fraction("76000")},
    //                         {Fraction("2"), Fraction("3"), Fraction("3"), Fraction("15"), Fraction("8000"), Fraction("45")},
    //                         {Fraction("5"), Fraction("-3"), Fraction("1"), Fraction("12"), Fraction("-4"), Fraction("56")},
    //                         {Fraction("23"), Fraction("13"), Fraction("-445941"), Fraction("12"), Fraction("6"), Fraction("-9")},
    //                         {Fraction("-2"), Fraction("12"), Fraction("21"), Fraction("19"), Fraction("-7"), Fraction("4")}};

    Fraction mat[N][N+1] = {{Fraction("3", "6"), Fraction("2"), Fraction("-4"), Fraction("3")},
                          {Fraction("2"), Fraction("3"), Fraction("3"), Fraction("15")},
                          {Fraction("5", "4"), Fraction("-3"), Fraction("1"), Fraction("14")}
                          };
    // Fraction mat[N][N+1] = {{Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("1", "1"), Fraction("5", "1")},
    //                         {Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("54", "1")},
    //                         {Fraction("256", "1"), Fraction("128", "1"), Fraction("64", "1"), Fraction("32", "1"), Fraction("16", "1"), Fraction("8", "1"), Fraction("4", "1"), Fraction("2", "1"), Fraction("1", "1"), Fraction("1453", "1")},
    //                         {Fraction("6561", "1"), Fraction("2187", "1"), Fraction("729", "1"), Fraction("243", "1"), Fraction("81", "1"), Fraction("27", "1"), Fraction("9", "1"), Fraction("3", "1"), Fraction("1", "1"), Fraction("10952", "1")},
    //                         {Fraction("65536", "1"), Fraction("16384", "1"), Fraction("4096", "1"), Fraction("1024", "1"), Fraction("256", "1"), Fraction("64", "1"), Fraction("16", "1"), Fraction("4", "1"), Fraction("1", "1"), Fraction("46101", "1")},
    //                         {Fraction("390625", "1"), Fraction("78125", "1"), Fraction("15625", "1"), Fraction("3125", "1"), Fraction("625", "1"), Fraction("125", "1"), Fraction("25", "1"), Fraction("5", "1"), Fraction("1", "1"), Fraction("140650", "1")},
    //                         {Fraction("1679616", "1"), Fraction("279936", "1"), Fraction("46656", "1"), Fraction("7776", "1"), Fraction("1296", "1"), Fraction("216", "1"), Fraction("36", "1"), Fraction("6", "1"), Fraction("1", "1"), Fraction("349949", "1")},
    //                         {Fraction("5764801", "1"), Fraction("823543", "1"), Fraction("117649", "1"), Fraction("16807", "1"), Fraction("2401", "1"), Fraction("343", "1"), Fraction("49", "1"), Fraction("7", "1"), Fraction("1", "1"), Fraction("756348", "1")},
    //                         {Fraction("16777216", "1"), Fraction("2097152", "1"), Fraction("262144", "1"), Fraction("32768", "1"), Fraction("4096", "1"), Fraction("512", "1"), Fraction("64", "1"), Fraction("8", "1"), Fraction("1", "1"), Fraction("1474597", "1")}};
    cout << gaussianElimination(mat);
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %.3f seconds.\n", elapsed.count() * 1e-9);
    //time(&end);
    //time_t elapsed = end - begin;
    //printf("Time measured: %ld seconds.\n", elapsed);
    return 0;
}