#include <sstream>
#include <iostream>

#include "LinkedList.hpp"

void foo(LinkedList<int> const & ll) {
    int x = ll[0];
    std::cout << x << std::endl;
}

int main(int argc, char * argv[]) {

    std::cout << "arguments:" << std::endl;

    for(int i=0; i<argc; i++) {
        std::cout << argv[i] << std::endl;
    }

    LinkedList<int> ll;

    std::string myString;

    std::cout << "Enter a number: ";

    std::getline(std::cin,myString);
    std::stringstream convert(myString);

    int x;
    convert >> x;
    ll.push_back(x);

    foo(ll);
}
