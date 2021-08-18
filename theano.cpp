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
    int singular_flag = forwardElim(mat);
    /* if matrix is singular */
    if (singular_flag != -1)
    {
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
        if (!mat[k][i_max]){
            return k; // Matrix is singular
        }
        /* Swap the greatest value row with current row */
        if (i_max != k){
            swap_row(mat, k, i_max);
        }
        for (int i=k+1; i<N; i++)
        {
            /* factor f to set current row kth element to 0,
             * and subsequently remaining kth column to 0 */
            Fraction f = mat[i][k]/mat[k][k];
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
    return x;
}