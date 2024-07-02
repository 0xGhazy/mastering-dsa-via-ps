#include <iostream>
#include<iomanip>
#include <unistd.h>
 
using namespace std;
 
int main() {
    long x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    if (x1 < x2) {
        swap(x1, x2);
        swap(y1, y2);
    }
 
    if (x1 <= y2) {
        cout << x1 << " " << min(y1, y2) <<endl;
        return 0;
    }
 
    cout << -1 <<endl;
    return 0;
}