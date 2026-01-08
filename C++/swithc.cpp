#include <iostream>
using namespace std;
int main()
{
    char a = 'C';
    switch(a)
    {

        case 'A':case 'E':case 'I':case 'O':case 'U':
        case 'a':case 'e':case 'i':case 'o':case 'u':
            cout<<"Vowel"<<endl;
            break;
  
        default:
        cout<<"Alphabet"<<endl;

    }

}