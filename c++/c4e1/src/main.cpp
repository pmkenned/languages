#include <iostream>
#include <limits>

void print_limits() {

    std::cout << "hello, world" << std::endl;

    std::cout << "float max: " << std::numeric_limits<float>::max() << std::endl;
    std::cout << "float min: " << std::numeric_limits<float>::min() << std::endl;

    std::cout << "(signed) int max: " << std::numeric_limits<int>::max() << std::endl;
    std::cout << "(signed) int min: " << std::numeric_limits<int>::min() << std::endl;

    std::cout << "unsigned int max: " << std::numeric_limits<unsigned int>::max() << std::endl;
    std::cout << "unsigned int min: " << std::numeric_limits<unsigned int>::min() << std::endl;

    std::cout << "(signed) long (int) max: " << std::numeric_limits<long>::max() << std::endl;
    std::cout << "(signed) long (int) min: " << std::numeric_limits<long>::min() << std::endl;

    std::cout << "unsigned long (int) max: " << std::numeric_limits<unsigned long>::max() << std::endl;
    std::cout << "unsigned long (int) min: " << std::numeric_limits<unsigned long>::min() << std::endl;

    std::cout << "(signed) short (int) max: " << std::numeric_limits<short>::max() << std::endl;
    std::cout << "(signed) short (int) min: " << std::numeric_limits<short>::min() << std::endl;

    std::cout << "unsigned short (int) max: " << std::numeric_limits<unsigned short>::max() << std::endl;
    std::cout << "unsigned short (int) min: " << std::numeric_limits<unsigned short>::min() << std::endl;

    std::cout << "char max: " << (int) std::numeric_limits<char>::max() << std::endl;
    std::cout << "char min: " << (int) std::numeric_limits<char>::min() << std::endl;

    std::cout << "signed char max: " << (int) std::numeric_limits<signed char>::max() << std::endl;
    std::cout << "signed char min: " << (int) std::numeric_limits<signed char>::min() << std::endl;

    std::cout << "unsigned char max: " << (int) std::numeric_limits<unsigned char>::max() << std::endl;
    std::cout << "unsigned char min: " << (int) std::numeric_limits<unsigned char>::min() << std::endl;



}

int increment(const int & x) {
    return x + 1;
}

int times2(const int x) {
    return x*2;
}

int main() {

    print_limits();

    int x = 4;
    const int y[] = {0,1,2};
    const int & z = x;

    std::cout << times2(x) << std::endl;
    std::cout << times2(y[1]) << std::endl;
    std::cout << times2(z) << std::endl;

    x = increment(1);
    std::cout << x << std::endl;

}
