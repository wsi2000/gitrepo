/*
 * imie.cxx
 * 
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	  
    char imie[10];

    cout << "Witaj w C++!" <<endl;
	cout << "Podaj imię: ";
    // cin >> imie;
    cin.getline(imie, 10);  
    cout << " ";
    cout << "Cześć, " << imie << "!" << endl; 
    
    
    int a,b;
    
    char dzialanie;
    cout << "Dzialanie? ";
    cin >> dzialanie;
    cout << "liczba a:"; cin >> a;
    cout << "liczba b:"; cin >> b;
    
    if (dzialanie == '+')
        cout << a+b << endl;
    else if (dzialanie == '-')
        cout << a-b << endl;
    
	return 0;
}

