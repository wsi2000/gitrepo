/*
 * bmii.cxx
 * 
110-1301, USA.
 * 
 * 
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	float masa = 0;
    float wzrost = 0;
    float BMI = 0;
    cout << "Podaj mase" << endl;
    cin >> masa;
    cout << "Podaj wzrost" << endl;
    cin >> wzrost;
    BMI= masa/(wzrost*wzrost);
    cout <<"Twoje BMI wynosi:" << BMI << endl;   
        if (BMI<18.5)
            cout << "niedowaga" << endl;
        else (BMI <18.5 && BMI >24.9)
            cout << "norma" << endl;
        if (BMI>=25) 
            cout << "nadwaga" << endl;
        if (BMI >=30)
            cout << "otyłość" << endl;
            
	return 0;
}

