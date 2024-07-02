#include <iostream>
#include<iomanip>

using namespace std;

int main() {
    int fnum = 0, lnum = 0;
    char op;
    cin >> fnum >> op >> lnum;
    (op == '+')?cout<<fnum+lnum:(op=='-')?cout<<fnum-lnum:(op=='*')?cout<<fnum*lnum:cout<<fnum/lnum;
    return 0;
}
