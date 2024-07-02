#include <iostream>
#include<iomanip>
#include <cmath>

using namespace std;

int main() {
    long num1, num2, num3;
    cin >> num1 >> num2 >> num3;

    long max_val = max(num1, num2);
    max_val = max(max_val, num3);

    long min_val = min(num1, num2);
    min_val = min(min_val, num3);

    long const mid = (num1 +num2 + num3) - (max_val + min_val);

    cout << min_val << endl;
    cout << mid << endl;
    cout << max_val << endl;
    cout<<endl;
    cout << num1 << endl;
    cout << num2 << endl;
    cout << num3 << endl;

    return 0;
}