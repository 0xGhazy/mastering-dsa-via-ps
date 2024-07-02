#include <iostream>
#include<iomanip>

using namespace std;

int main() {

    // Solution 1
    // long long a, b;
    // cin >> a >> b;
    // cout << (a%10) + (b%10) << endl;

    // solution 2
    string a, b;
    cin >> a >> b;
    cout <<  a[a.size()-1] + b[b.size()-1] -2*'0' << endl;

    return 0;
}
