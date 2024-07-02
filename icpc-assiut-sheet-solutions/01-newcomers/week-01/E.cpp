#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    const float pi = 3.141592653;
    float r;
    cin >> r;
    
    cout << fixed << setprecision(9) << endl;
    cout << (r * r) * pi << endl;
    return 0;
}
