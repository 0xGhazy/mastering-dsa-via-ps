#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    long days;
    cin >> days;

    int years = days / 365;
    int rest = days % 365;

    int months = rest / 30;
    rest = rest % 30;

    cout << years << " years" <<endl;
    cout << months << " months" <<endl;
    cout << rest << " days" <<endl;

    return 0;
}
