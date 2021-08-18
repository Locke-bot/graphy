//Gauss Elimination
#include<iostream>
#include <iterator>
#include <algorithm>
#include <vector>
#include "fraction.cxx"
using namespace std;
int i,j;

std::vector<Fraction> GaussianElimination(std::vector<std::vector<Fraction>> &a)
{
    int n = a.size();
    vector<Fraction> x(n);        //declare an array to store the elements of augmented-matrix    

    for (int i=0;i<n;i++)                    //Pivotisation
        for (int k=i+1;k<n;k++)
            if (a[i][i].abso()<a[k][i].abso())
                for (j=0;j<=n;j++)
                {
                    Fraction temp=a[i][j];
                    a[i][j]=a[k][j];
                    a[k][j]=temp;
                }
    
    for (int i=0;i<n-1;i++){            //loop to perform the gauss elimination
        Fraction aii=a[i][i];
        for (int k=i+1;k<n;k++)
            {
                Fraction t=a[k][i]/aii;
                for (j=0;j<=n;j++)
                    a[k][j]-=t*a[i][j];    //make the elements below the pivot elements equal to zero or eliminate the variables
            }
    }
    
    for (i=n-1;i>=0;i--)                //back-substitution
    {                        //x is an array whose values correspond to the values of x,y,z..
        x[i]=a[i][n];                //make the variable to be calculated equal to the rhs of the last equation
        for (j=i+1;j<n;j++)
            if (j!=i)            //then subtract all the lhs values except the coefficient of the variable whose value                                   is being calculated
                x[i]-=a[i][j]*x[j];
        x[i]=x[i]/a[i][i];            //now finally divide the rhs by the coefficient of the variable to be calculated
    }
    return x;
}
int main(){
    vector
    GaussianElimination()
}