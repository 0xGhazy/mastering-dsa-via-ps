#include <iostream>
#include<iomanip>
#include <cmath>

using namespace std;

int main() {
    double x1, x2, x3, x4;

    cin>>x1>>x2>>x3>>x4;
    if (x2 == x4) {
        (x1 > x3)?cout<<"YES"<<endl:cout<<"NO"<<endl;
        return 0;
    }

    
    if ( ((x2) * log(x1)) > ((x4) * log(x3))) {
        cout<<"YES"<<endl;
        return 0;
    }
    cout<<"NO"<<endl;
    return 0;
}