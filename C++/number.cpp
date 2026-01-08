#include <iostream>
using namespace std;
int main()
{
    int a=-5;
    if(a>0)
    {
        cout<<"Positive Number"<<endl;
        if(a%2==0)
        {
            cout<<"Even Number";
        }
        else
        {
            cout<<"Odd Number";
        }
    
    }
    else
    {
        cout<<"Negative Number";
    }
}