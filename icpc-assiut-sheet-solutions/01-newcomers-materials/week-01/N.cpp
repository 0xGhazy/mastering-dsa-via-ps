#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    char input;
    cin >> input;
    if (input >= 'a' && input <= 'z') { cout << (char) (input-32) << endl; }
    else { cout << (char) (input+32) << endl; }
    return 0;
}
