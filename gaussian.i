/* File: gaussian.i */
%module gaussian

// inline inserts into wrapper *and* SWIG wraps it.
%inline %{
#include <chrono>
#include "fraction.cpp"
#include "gaussian_constants.h"
#include <time.h>
extern int forwardElim(Fraction mat[N][N+1]);
extern Fraction * backSub(Fraction mat[N][N+1]);
extern Fraction * gaussianElimination(Fraction mat[N][N+1]);
void swap_row(Fraction mat[N][N+1], int i, int j);
%}