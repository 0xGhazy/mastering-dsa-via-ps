#include <iostream>
#include<iomanip>

using namespace std;

bool is_multiplay(int a, int b);

int main() {
    int a, b;
    cin >> a >> b;
    if (is_multiplay(a, b))
        cout <<"Multiples" << endl;
    else
        cout << "No Multiples" << endl;
    return 0;
}

bool is_multiplay(int a, int b) {
    return a % b == 0 || b % a == 0;
}