#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    char input;
    cin >> input;
    if (input >= '0' && input <= '9') {
        cout << "IS DIGIT" << endl;
    } else if (input >= 'A' && input <= 'Z') {
        cout << "ALPHA" << endl;
        cout << "IS CAPITAL" << endl;
    } else {
        cout << "ALPHA" << endl;
        cout << "IS SMALL" << endl;
    }
    return 0;
}
