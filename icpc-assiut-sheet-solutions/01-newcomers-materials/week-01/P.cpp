#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    char number;
    cin >> number;
    (number%2)?cout<<"ODD":cout<<"EVEN";
    return 0;
}
