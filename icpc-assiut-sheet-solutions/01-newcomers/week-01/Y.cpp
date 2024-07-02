#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    long x1, x2, x3, x4;
    long result;
    cin >> x1 >> x2 >> x3 >> x4;

    result = ( ((x1 % 100) * (x2 % 100) )%100* ((x3 % 100) * (x4 % 100))%100 ) % 100;

    if (result < 10) {
        cout << 0;
    }
    cout << result << endl;
    return 0;
}