#include<vector>
#include<iostream>
#include<bits/stdc++.h>
#include "fraction.cxx"
// C++ program to demonstrate working of Guassian Elimination
// method
//#include<bits/stdc++.h>
using namespace std;
 
// #define N 20        // Number of unknowns
int N;
// function to reduce matrix to r.e.f.  Returns a value to
// indicate whether matrix is singular or not
int forwardElim(std::vector<std::vector<Fraction>> &mat);
 
// function to calculate the values of the unknowns
std::vector<Fraction> backSub(std::vector<std::vector<Fraction>> &mat);
 
// function to get matrix content
std::vector<Fraction> gaussianElimination(std::vector<std::vector<Fraction>> &mat)
{
    /* reduction into r.e.f. */
    N = mat.size();
    // cout << singular_flag << "cout singular" << endl;
    cout << "cout singular" << endl;
    int singular_flag = forwardElim(mat);
    cout << "miami bitches" << endl;
    /* if matrix is singular */
    if (singular_flag != -1)
    {
        /* if the RHS of equation corresponding to
           zero row is 0, * system has infinitely
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
void swap_row(std::vector<std::vector<Fraction>> &mat, int i, int j)
{
    //printf("Swapped rows %d and %d\n", i, j);
    for (int k=0; k<=N; k++)
    {
        Fraction temp = mat[i][k];
        mat[i][k] = mat[j][k];
        mat[j][k] = temp;
    }
}
 
// function to print matrix content at any stage
 
// function to reduce matrix to r.e.f.
int forwardElim(std::vector<std::vector<Fraction>> &mat)
{
    for (int k=0; k<N; k++)
    {
        // Initialize maximum value and index for pivot
        int i_max = k;
        Fraction v_max = Fraction(std::to_string(mat[i_max][k].toInt()).c_str());;
        /* find greater amplitude for pivot if any */
        for (int i = k+1; i < N; i++){
            if (mat[i][k].abso() > v_max){
                v_max = mat[i][k], i_max = i;
            }
        }
        /* if a prinicipal diagonal element  is zero,
         * it denotes that matrix is singular, and
         * will lead to a division-by-zero later. */
        // cout << "I did it " << mat[k][i_max] << " " << !mat[k][i_max] << endl;
        if (!mat[k][i_max]){
            cout << "I am singular" << endl;
            return k; // Matrix is singular
        }
        /* Swap the greatest value row with current row */
        if (i_max != k){
            swap_row(mat, k, i_max);
        }
        for (int y=0; y<N; y++){
            for (int q=0; q<N+1; q++){
                cout << mat[y][q] << "  ";
            }
            cout << endl;
        }
        for (int i=k+1; i<N; i++)
        {
            /* factor f to set current row kth element to 0,
             * and subsequently remaining kth column to 0 */
            Fraction f = mat[i][k]/mat[k][k];
            // cout << f << " " << mat[i][k] << " " << mat[k][k] << endl;
            /* subtract fth multiple of corresponding kth
               row element*/
            for (int j=k+1; j<=N; j++){
                mat[i][j] -= mat[k][j]*f;
            }
            /* filling lower triangular matrix with zeros*/
            mat[i][k] = Fraction("0");
        }
 
        //print(mat);        //for matrix state
    }
    //print(mat);            //for matrix state
    return -1;
}
 
// function to calculate the values of the unknowns
std::vector<Fraction> backSub(std::vector<std::vector<Fraction>> &mat)
{
    std::vector<Fraction> x(N);  // An array to store solution
 
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
    cout << "SOLUTION READY" <<endl;
    for (int i=0; i<x.size(); i++){
        cout << x[i] << endl;
    }
    return x;
}
// Driver program
int main()
{
    /* input matrix */
    auto begin = std::chrono::high_resolution_clock::now();
    //time_t begin, end;
    //time(&begin);
    vector<vector<Fraction>> mat  {{Fraction("10000000000", "1"), Fraction("1000000000", "1"), Fraction("100000000", "1"), Fraction("10000000", "1"), Fraction("1000000", "1"), Fraction("100000", "1"), Fraction("10000", "1"), Fraction("1000", "1"), Fraction("100", "1"), Fraction("10", "1"), Fraction("1", "1"), Fraction("240045", "1")},
 {Fraction("3486784401", "1"), Fraction("387420489", "1"), Fraction("43046721", "1"), Fraction("4782969", "1"), Fraction("531441", "1"), Fraction("59049", "1"), Fraction("6561", "1"), Fraction("729", "1"), Fraction("81", "1"), Fraction("9", "1"), Fraction("1", "1"), Fraction("157505", "1")},
 {Fraction("1073741824", "1"), Fraction("134217728", "1"), Fraction("16777216", "1"), Fraction("2097152", "1"), Fraction("262144", "1"), Fraction("32768", "1"), Fraction("4096", "1"), Fraction("512", "1"), Fraction("64", "1"), Fraction("8", "1"), Fraction("1", "1"), Fraction("98341", "1")},
 {Fraction("282475249", "1"), Fraction("40353607", "1"), Fraction("5764801", "1"), Fraction("823543", "1"), Fraction("117649", "1"), Fraction("16807", "1"), Fraction("2401", "1"), Fraction("343", "1"), Fraction("49", "1"), Fraction("7", "1"), Fraction("1", "1"), Fraction("57657", "1")},
 {Fraction("60466176", "1"), Fraction("10077696", "1"), Fraction("1679616", "1"), Fraction("279936", "1"), Fraction("46656", "1"), Fraction("7776", "1"), Fraction("1296", "1"), Fraction("216", "1"), Fraction("36", "1"), Fraction("6", "1"), Fraction("1", "1"), Fraction("31133", "1")},
 {Fraction("9765625", "1"), Fraction("1953125", "1"), Fraction("390625", "1"), Fraction("78125", "1"), Fraction("15625", "1"), Fraction("3125", "1"), Fraction("625", "1"), Fraction("125", "1"), Fraction("25", "1"), Fraction("5", "1"), Fraction("1", "1"), Fraction("15025", "1")},
 {Fraction("1048576", "1"), Fraction("262144", "1"), Fraction("65536", "1"), Fraction("16384", "1"), Fraction("4096", "1"), Fraction("1024", "1"), Fraction("256", "1"), Fraction("64", "1"), Fraction("16", "1"), Fraction("4", "1"), Fraction("1", "1"), Fraction("6165", "1")},
 {Fraction("59049", "1"), Fraction("19683", "1"), Fraction("6561", "1"), Fraction("2187", "1"), Fraction("729", "1"), Fraction("243", "1"), Fraction("81", "1"), Fraction("27", "1"), Fraction("9", "1"), Fraction("3", "1"), Fraction("1", "1"), Fraction("1961", "1")},
 {Fraction("1024", "1"), Fraction("512", "1"), Fraction("256", "1"), Fraction("128", "1"), Fraction("64", "1"), Fraction("32", "1"), Fraction("16", "1"), Fraction("8", "1"), Fraction("4", "1"), Fraction("2", "1"), Fraction("1", "1"), Fraction("397", "1")},
 {Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("33", "1")},
 {Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("1", "1"), Fraction("5", "1")}};

    
//     Fraction mat[N][N+1] = {{Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("1", "1"), Fraction("5", "1")},
//  {Fraction("1", "1"), Fraction("1", "1"), Fraction ("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("33", "1")},
//  {Fraction("1024", "1"), Fraction("512", "1"), Fraction("256", "1"), Fraction("128", "1"), Fraction("64", "1"), Fraction("32", "1"), Fraction("16", "1"), Fraction("8", "1"), Fraction("4", "1"), Fraction("2", "1"), Fraction("1", "1"), Fraction("397", "1")},
//  {Fraction("59049", "1"), Fraction("19683", "1"), Fraction("6561", "1"), Fraction("2187", "1"), Fraction("729", "1"), Fraction("243", "1"), Fraction("81", "1"), Fraction("27", "1"), Fraction("9", "1"), Fraction("3", "1"), Fraction("1", "1"), Fraction("1961", "1")},
//  {Fraction("1048576", "1"), Fraction("262144", "1"), Fraction("65536", "1"), Fraction("16384", "1"), Fraction("4096", "1"), Fraction("1024", "1"), Fraction("256", "1"), Fraction("64", "1"), Fraction("16", "1"), Fraction("4", "1"), Fraction("1", "1"), Fraction("6165", "1")},
//  {Fraction("9765625", "1"), Fraction("1953125", "1"), Fraction("390625", "1"), Fraction("78125", "1"), Fraction("15625", "1"), Fraction("3125", "1"), Fraction("625", "1"), Fraction("125", "1"), Fraction("25", "1"), Fraction("5", "1"), Fraction("1", "1"), Fraction("15025", "1")},
//  {Fraction("60466176", "1"), Fraction("10077696", "1"), Fraction("1679616", "1"), Fraction("279936", "1"), Fraction("46656", "1"), Fraction("7776", "1"), Fraction("1296", "1"), Fraction("216", "1"), Fraction("36", "1"), Fraction("6", "1"), Fraction("1", "1"), Fraction("31133", "1")},
//  {Fraction("282475249", "1"), Fraction("40353607", "1"), Fraction("5764801", "1"), Fraction("823543", "1"), Fraction("117649", "1"), Fraction("16807", "1"), Fraction("2401", "1"), Fraction("343", "1"), Fraction("49", "1"), Fraction("7", "1"), Fraction("1", "1"), Fraction("57657", "1")},
//  {Fraction("1073741824", "1"), Fraction("134217728", "1"), Fraction("16777216", "1"), Fraction("2097152", "1"), Fraction("262144", "1"), Fraction("32768", "1"), Fraction("4096", "1"), Fraction("512", "1"), Fraction("64", "1"), Fraction("8", "1"), Fraction("1", "1"), Fraction("98341", "1")},
//  {Fraction("3486784401", "1"), Fraction("387420489", "1"), Fraction("43046721", "1"), Fraction("4782969", "1"), Fraction("531441", "1"), Fraction("59049", "1"), Fraction("6561", "1"), Fraction("729", "1"), Fraction("81", "1"), Fraction("9", "1"), Fraction("1", "1"), Fraction("157505", "1")},
//  {Fraction("10000000000", "1"), Fraction("1000000000", "1"), Fraction("100000000", "1"), Fraction("10000000", "1"), Fraction("1000000", "1"), Fraction("100000", "1"), Fraction("10000", "1"), Fraction("1000", "1"), Fraction("100", "1"), Fraction("10", "1"), Fraction("1", "1"), Fraction("240045", "1")}};
    // Fraction mat[N][N+1] = {{Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("0", "1"), Fraction("1", "1"), Fraction("5", "1")},
    //                         {Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("1", "1"), Fraction("54", "1")},
    //                         {Fraction("256", "1"), Fraction("128", "1"), Fraction("64", "1"), Fraction("32", "1"), Fraction("16", "1"), Fraction("8", "1"), Fraction("4", "1"), Fraction("2", "1"), Fraction("1", "1"), Fraction("1453", "1")},
    //                         {Fraction("6561", "1"), Fraction("2187", "1"), Fraction("729", "1"), Fraction("243", "1"), Fraction("81", "1"), Fraction("27", "1"), Fraction("9", "1"), Fraction("3", "1"), Fraction("1", "1"), Fraction("10952", "1")},
    //                         {Fraction("65536", "1"), Fraction("16384", "1"), Fraction("4096", "1"), Fraction("1024", "1"), Fraction("256", "1"), Fraction("64", "1"), Fraction("16", "1"), Fraction("4", "1"), Fraction("1", "1"), Fraction("46101", "1")},
    //                         {Fraction("390625", "1"), Fraction("78125", "1"), Fraction("15625", "1"), Fraction("3125", "1"), Fraction("625", "1"), Fraction("125", "1"), Fraction("25", "1"), Fraction("5", "1"), Fraction("1", "1"), Fraction("140650", "1")},
    //                         {Fraction("1679616", "1"), Fraction("279936", "1"), Fraction("46656", "1"), Fraction("7776", "1"), Fraction("1296", "1"), Fraction("216", "1"), Fraction("36", "1"), Fraction("6", "1"), Fraction("1", "1"), Fraction("349949", "1")},
    //                         {Fraction("5764801", "1"), Fraction("823543", "1"), Fraction("117649", "1"), Fraction("16807", "1"), Fraction("2401", "1"), Fraction("343", "1"), Fraction("49", "1"), Fraction("7", "1"), Fraction("1", "1"), Fraction("756348", "1")},
    //                         {Fraction("16777216", "1"), Fraction("2097152", "1"), Fraction("262144", "1"), Fraction("32768", "1"), Fraction("4096", "1"), Fraction("512", "1"), Fraction("64", "1"), Fraction("8", "1"), Fraction("1", "1"), Fraction("1474597", "1")}};
    gaussianElimination(mat);
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %.3f seconds.\n", elapsed.count() * 1e-9);
    //time(&end);
    //time_t elapsed = end - begin;
    //printf("Time measured: %ld seconds.\n", elapsed);
    return 0;
}