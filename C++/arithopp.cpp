#include <iostream>
using namespace std;
int main()
{
    int a=10,b=3,c=0;
    cout<<"Addition: "<<(a+b)<<endl;
    cout<<"Subtraction: "<<(a-b)<<endl;
    cout<<"Multiplication: "<<(a*b)<<endl;
    cout<<"Division: "<<(float)a/b<<endl;
    cout<<"Modulus: "<<(a%b)<<endl;
    cout<<"Increment: "<<(a++)<<endl;
    cout<<a<<endl;
    cout<<"Decrement: "<<(b--)<<endl;
    cout<<b<<endl;
    while (c<=5)
    {
        cout<<"Value of c: "<<c<<endl;
        c++;
    }
}

