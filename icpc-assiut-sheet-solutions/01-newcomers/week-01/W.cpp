#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    int a, b, result;
    char op, _;
    int internal_result = 0;
    cin >> a >> op >> b >> _ >> result;
    switch (op) {
        case '+':
            internal_result = a + b;
            break;
        case '-':
            internal_result = a - b;
            break;
        case '*':
            internal_result = a * b;
            break;
        default:
            internal_result = 0;
    }

    if (internal_result == result) {
        cout << "Yes" << endl;
    } else {
        cout << internal_result << endl;
    }

    return 0;
}