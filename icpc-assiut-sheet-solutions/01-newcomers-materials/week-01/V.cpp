#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    short a, b;
    char op;
    cin >> a >> op >> b;
    if (op == '>' && a > b) {
        cout << "Right" << endl;
    } else if (op == '<' && a < b) {
        cout << "Right" << endl;
    } else if (op == '=' && a == b) {
        cout << "Right" << endl;
    } else {
        cout << "Wrong" << endl;
    }
    return 0;
}