/*
 * tabele.cpp
 */

#include <iostream>

using namespace std;

void pobierzliczby(int tab[], int ile){
    int i=0;
    for (i = 0; i < ile; i++) {
        cout << "Podaj liczbę: ";
        cin >> tab[i];
    }
}

void sumujliczby (int tab[], int ile){
    int i = 0 ;
    int suma = 0;
     for (i = 0; i < ile; i++) {
        suma += tab[i];
         }
         cout << "Suma liczb: " << suma << endl; 
}

void najmniejsza(int tab[], int ile){
    int min = tab[0];
    int i = 0;
    for (i = 1 ; i < ile ; i++ ) {
        if (min > tab[i])
        min = tab[i];
        } 
        cout << "Najmniejsza: " << min << endl;
        
    } // funkcja znajduje i drukuje najmniejsza liczbe z tabeli
    
void ile5(int tab[], int ile){
    int i = 0;
    for (i = 0 ; i < ile ; i++){
        if (tab[i] %5  ==0)
            licznik5++;
            
        if (tab[i] % 2 == 0 )
            parzyste++;
        
        }
        
        
    cout << "Liczby podzielne przez 5: " << licznik5 << endl;
    cout << "Parzystych: " << parzyste << endl;
    
    }

int main(int argc, char **argv)
{
    int rozmiar = 0;
    cout << "Ile liczb podasz: " ;
    cin >> rozmiar;
    
	int liczby[rozmiar];
    
    pobierzliczby(liczby, rozmiar);
    sumujliczby(liczby,rozmiar);
    najmniejsza(liczby,rozmiar);
    ile5(liczby,rozmiar);

	return 0;
}

