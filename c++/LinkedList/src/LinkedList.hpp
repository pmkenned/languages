#ifndef _LINKEDLIST_HPP_
#define _LINKEDLIST_HPP_

template <class T>
class LinkedList {

    template <class U>
    struct LinkedListNode {
        U data;
        LinkedListNode * nextNode;
    };

    LinkedListNode<T> * head, * tail;

    public:
        LinkedList();
        void push_back(T x);
        T& operator[](const size_t index);
  const T& operator[](const size_t index) const;

};

template <class T>
LinkedList<T>::LinkedList() : head(0), tail(0) {
}

template <class T>
void LinkedList<T>::push_back(T x) {
    if(tail == 0) {
        head = new LinkedListNode<T>;
        tail = head;
    }
    else {
        tail->nextNode = new LinkedListNode<T>;
        tail = tail->nextNode;
    }
    tail->nextNode = 0;
    tail->data = x;
}

template <class T>
const T& LinkedList<T>::operator[](const size_t index) const {
    LinkedListNode<T> const * node = head;
    size_t i=0;
    while((i < index) && (node->nextNode != 0))
        node = node->nextNode;
    return node->data;
}

template <class T>
T& LinkedList<T>::operator[](const size_t index) {
    LinkedListNode<T>& node = const_cast<LinkedListNode<T> &>
        ( static_cast<const LinkedList &>(*this)[index] );
    return node.data;
}

#endif
