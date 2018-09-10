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
    
    
	return 0;
}

