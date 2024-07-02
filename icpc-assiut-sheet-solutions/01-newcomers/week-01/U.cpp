#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    double number, intPart, fractPart = 0.000;
    cin >> number;
    intPart = int(number);
    fractPart = number - intPart;
    if (fractPart == 0) {
        cout << "int " << intPart << endl;
    }  else {
        cout << "float " << intPart << " " << fractPart << endl;
    }

    return 0;
}