#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include "gmpxx.h"

using namespace std;

class Fraction {
public:
    mpz_class numerator, denominator, temp;
    Fraction(const char*num = "0", const char*den = "1")  {
        std::string s_num;
        std::string s_den;
        std::stringstream ss;
        ss << num;
        ss >> s_num;
        ss.str("");
        ss.clear();
        ss << den;
        ss >> s_den;
        int num_dot = s_num.find('.');
        int den_dot = s_den.find('.');
        if (!(num_dot != -1 && den_dot != -1) && (num_dot != -1 || den_dot != -1)){ // i.e just one of them has a dot in it (float)
            if (num_dot == -1){
                s_num += ".";
                num_dot = s_num.length()-1;
            }
            else if (den_dot == -1){
                s_den += ".";
                den_dot = s_den.length()-1;
            }

        }
        if (num_dot != -1 && den_dot != -1){
            std::string num_zero(s_num.length()-num_dot, '0');
            std::string den_zero(s_den.length()-den_dot, '0');
            // cout << remove_zero(s_num.substr(0, num_dot) + s_num.substr(num_dot+1)) << " " << (remove_zero(s_den.substr(0, den_dot)) + s_den.substr(den_dot+1)) << endl;
            numerator = mpz_class(remove_zero(s_num.substr(0, num_dot) + s_num.substr(num_dot+1))) * mpz_class('1'+ den_zero);
            denominator = mpz_class(remove_zero(s_den.substr(0, den_dot) + s_den.substr(den_dot+1))) * mpz_class('1'+ num_zero);
            // cout << num_zero << " " << endl;
        }
        else{
            numerator = mpz_class(num);
            denominator = mpz_class(den);
            mpz_gcd(temp.get_mpz_t(), numerator.get_mpz_t(), denominator.get_mpz_t());
        }
        reduce_fraction(*this);
    }
    static std::string remove_zero(std::string e){
        if (e[0] == '-'){
            e = e.substr(1);
            e.erase(0, std::min(e.find_first_not_of('0'), e.size()-1));
            e = '-'+e;
        }
        else{
            e.erase(0, std::min(e.find_first_not_of('0'), e.size()-1));
        }
        return e;
    }

    explicit operator bool() const { return 0 != numerator;}
    // This is automatically called when '+' is used with
    // between two Fraction objects
    //explicit operator int() const{return 2};
    Fraction operator + (Fraction const &obj) {
         Fraction frac;
         frac.numerator = numerator*obj.denominator + denominator*obj.numerator;
         frac.denominator = denominator*obj.denominator;
         reduce_fraction(frac);
         return frac;
    }
    Fraction operator + (int const &obj) {
         Fraction frac;
         frac.numerator = numerator + denominator*obj;
         frac.denominator = denominator;
         reduce_fraction(frac);
         return frac;
    }    
    Fraction operator - (int const &obj) {
         Fraction frac;
         frac.numerator = numerator - denominator*obj;
         frac.denominator = denominator;
         reduce_fraction(frac);
         return frac;
    }
    bool operator == (int const &obj) {
        if (numerator == obj && denominator == 1) {
            return true;
        }
        return false;
    }
    bool operator == (Fraction const &obj) {
        if (numerator == obj.numerator && denominator == obj.denominator) {
            return true;
        }
        return false;
    }
    // bool 
    bool operator != (Fraction const &obj) {
        return !(*this==obj);
    }
    bool operator != (int const &obj) {
        return !(*this==obj);
    }
    bool operator < (int const &obj) {
        return numerator < obj*denominator;
    }
    bool operator > (int const &obj) {
        return numerator > obj*denominator;
    }
    bool operator < (Fraction const &obj) {
        return numerator*obj.denominator < obj.numerator*denominator;
    }
    bool operator > (Fraction const &obj) {
        return numerator*obj.denominator > obj.numerator*denominator;
    }    
    Fraction operator += (int const &obj) {
         *this = *this + obj;
         return *this;
    }
    Fraction operator -= (int const &obj) {
         *this = *this - obj;
         return *this;
    }    
    Fraction operator - (Fraction const &obj) {
         Fraction frac;
         frac.numerator = numerator*obj.denominator - denominator*obj.numerator;
         frac.denominator = denominator*obj.denominator;
         reduce_fraction(frac);
         return frac;
    }
    friend std::ostream& operator<<(std::ostream& out, const Fraction& frac){
        out << frac.numerator << "/" << frac.denominator;
        return out;
    };
    Fraction operator * (Fraction const &obj) {
         Fraction frac;
         frac.numerator =  numerator * obj.numerator;
         frac.denominator = denominator * obj.denominator;
         reduce_fraction(frac);
         return frac;
    }
    Fraction operator * (int const &obj) {
        Fraction frac;
        frac.numerator = numerator*obj;
        frac.denominator = denominator;
        reduce_fraction(frac);
        return frac;
    }
    Fraction operator += (Fraction const &obj) {
        *this = *this + obj;
        return *this;
    }
    Fraction operator ++ (int) {
        *this = *this + 1;
        return *this;
    }

    Fraction operator -= (Fraction const &obj) {
        *this = *this - obj;
        return *this;
    }

    Fraction operator / (Fraction const &obj) {
         Fraction frac;
         frac.numerator = numerator* obj.denominator;
         frac.denominator = denominator * obj.numerator;
         reduce_fraction(frac);
         return frac;
    }


    std::string get_num(){
        return numerator.get_str();
    }

    std::string get_den(){
        return denominator.get_str();
    }

    void reduce_fraction(Fraction &obj){
        mpz_gcd(obj.temp.get_mpz_t(), obj.numerator.get_mpz_t(), obj.denominator.get_mpz_t());
        obj.numerator = obj.numerator/obj.temp;
        obj.denominator = obj.denominator/obj.temp;
        if (obj.denominator < 0)
            obj.numerator *= -1, obj.denominator *= -1;
    }

    Fraction abso() {
        Fraction frac;
        frac.numerator = abs(numerator);
        frac.denominator = abs(denominator);
        return frac;
    }
    
    int toInt() {
        return mpz_class(numerator/denominator).get_si();
    }
    void print() {
        cout << numerator << "/" << denominator << endl;
    }
};

// int main(){
//     Fraction f2("-0.8716330694513772", "3.0");
//     // Fraction f2("-0.00", "3.0");
//     // Fraction f3("-1");
//     f2.print();
//     // mpz_class a;
//     // a = mpz_class("4033");
//     // cout << a;
//     // f1 -= f2*f3;
//     // f1 -= Fraction("2");
//     // bool b;
//     // b = ( = );
//     // cout << "\nAfter Hours" << endl;
//     // cout << f1+1;
//     // cout << "about " << b << "\nabs";
// }