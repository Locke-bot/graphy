/* File: graphene.i */
%module graphene
%include "std_vector.i"
%include "std_string.i"
%{ 
    #include <sstream>
    #include <string>
    #include "gaussian.cpp"
%}

%template(Vector) std::vector<Fraction>;
%template(NestedVector) std::vector<std::vector<Fraction>>;
%include "gaussian.cpp"
class Fraction{
public:
    mpz_class numerator, denominator, temp;
    Fraction(const char*num = "0", const char*det = "1");
    static std::string remove_zero(std::string e);
    Fraction operator + (Fraction const &obj);
    Fraction operator + (int const &obj);
    Fraction operator - (int const &obj);
    explicit operator bool() const;
    bool operator == (int const &obj);
    bool operator == (Fraction const &obj);
    bool operator != (Fraction const &obj);
    bool operator != (int const &obj);
    bool operator < (int const &obj);
    bool operator > (int const &obj);
    bool operator < (Fraction const &obj);
    Fraction operator -= (int const &obj);
    bool operator > (Fraction const &obj);
    Fraction operator += (int const &obj);
    Fraction operator - (Fraction const &obj);
    Fraction operator * (Fraction const &obj);
    Fraction operator * (int const &obj);
    Fraction operator += (Fraction const &obj);
    Fraction operator -= (Fraction const &obj);
    Fraction operator / (Fraction const &obj);
    Fraction abso();
    std::string get_num();
    std::string get_den();
    int toInt();
    void reduce_fraction(Fraction &obj);
    %extend {
        std::string __str__() {
            stringstream ss;
            ss << $self->numerator.get_str() << "/" << $self->denominator.get_str();
            return ss.str();
        }
    }
};