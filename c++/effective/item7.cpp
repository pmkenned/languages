#include <iostream>

using namespace std;

class Base {
public:
    virtual ~Base() { cout << "Base destructor" << endl; }
};

class Derived : public Base {
public:
    ~Derived() { cout << "Derived destructor" << endl; }
};

class AbstractBase {
    public:
        virtual ~AbstractBase() = 0; // pure virtual because this is an abstract base class
};

AbstractBase::~AbstractBase() {}

class DerivedFromAbstractBase : public AbstractBase {
    public:
        ~DerivedFromAbstractBase() {
            std::cout << "DerivedFromAbstractBase destructor" << std::endl;
        }
};

int main(int argc, char * argv[]) {

    Base * b = new Derived();

    delete b; // will invoke derived destructor and then the base destructor

    DerivedFromAbstractBase * dfab = new DerivedFromAbstractBase();
    delete dfab;
}
