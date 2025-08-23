#include <iostream>
using namespace std;

/*
输出数组的地址:
0x5ffe50 0x5ffe54 0x5ffe58
0x5ffe5c 0x5ffe60 0x5ffe64
*/

void test_arr() {
    int array[2][3] = {
		{0, 1, 2},
		{3, 4, 5}
    };
    cout << &array[0][0] << " " << &array[0][1] << " " << &array[0][2] << endl;
    cout << &array[1][0] << " " << &array[1][1] << " " << &array[1][2] << endl;
}

int main() {
    test_arr();
}
