# Assiut code forces sheet

## Week 01: [Date types contest](https://codeforces.com/group/MWSDmqGsZm/contest/219158)

### Notes:

- `a**b > c**d` can be simplified to **`b log(a) * d log(c)`**.
- `10+20=30` or `10 + 20 = 30` can be taken from user input as the following example:

```cpp
    int num1, num2, result;
    char op, eq;
    cin >> num1 >> op >> num2 >> eq >> result;
```

- The `%` operator can be used and distributed to avoid the overflow as follows:

```cpp
    long x1, x2, x3, x4;
    long result;
    cin >> x1 >> x2 >> x3 >> x4;

    result = ( ((x1 % 100) * (x2 % 100) )%100* ((x3 % 100) * (x4 % 100))%100 ) % 100;
```
