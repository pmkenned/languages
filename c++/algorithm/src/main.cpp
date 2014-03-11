#include <iostream>
#include <vector>
#include <algorithm>

void for_each_func(int x) {
}

bool find_if_func(int x) {
    return (x % 2 == 0)? true : false;
}

int main(int argc, char * argv[]) {

    std::vector<int> a;

    int x;
    std::cout << "list: ";
    for(int i=0; i<10; i++) {
        x = i%5;
        a.push_back(x);
        std::cout << x << " ";
    }
    std::cout << std::endl;

    std::vector<int>::iterator
        find_it,
        find_if_it,
        find_end_it,
        find_first_of_it;

    int sought = 3;
    int sought_list[] = {2,3,4};
    
                       std::for_each(      a.begin(), a.end(), for_each_func);
    find_it          = std::find(          a.begin(), a.end(), sought);
    find_if_it       = std::find_if(       a.begin(), a.end(), find_if_func);
    find_end_it      = std::find_end(      a.begin(), a.end(), sought_list, sought_list+3);
    find_first_of_it = std::find_first_of( a.begin(), a.end(), sought_list, sought_list+3);

//    std::adjacent_find();
//    std::count();
//    std::count_if();
//    std::mismatch();
//    std::equal();
//    std::search();
//    std::search_n();

    std::cout << "find_it: "          << (find_it          - a.begin()) << std::endl;
    std::cout << "find_if_it: "       << (find_if_it       - a.begin()) << std::endl;
    std::cout << "find_end_it: "      << (find_end_it      - a.begin()) << std::endl;
    std::cout << "find_first_of_it: " << (find_first_of_it - a.begin()) << std::endl;

//
//    std::copy();
//    std::copy_backward();
//    std::swap();
//    std::swap_ranges();
//    std::iter_swap();
//    std::transform();
//    std::replace();
//    std::replace_if();
//    std::replace_copy();
//    std::replace_copy_if();
//    std::fill();
//    std::fill_n();
//    std::generate();
//    std::generate_n();
//    std::remove();
//    std::remove_if();
//    std::remove_copy();
//    std::remove_copy_if();
//    std::unique();
//    std::unique_copy();
//    std::reverse();
//    std::reverse_copy();
//    std::rotate();
//    std::rotate_copy();
//    std::partition();
//    std::stable_partition();
//    std::sort();
//    std::stable_sort();
//    std::partial_sort();
//    std::partial_sort_copy();
//    std::is_sorted();
//    std::is_sorted_until();
//    std::nth_element();
//
//    std::lower_bound();
//    std::upper_bound();
//    std::equal_range();
//    std::binary_search();
//
//    std::merge();
//    std::implace_merge();
//    std::includes();
//    std::set_union();
//    std::set_intersection();
//    std::set_difference();
//    std::set_symmetric_difference();
//
//    std::push_heap();
//    std::pop_heap();
//    std::make_heap();
//    std::sort_heap();
//    std::is_heap();
//    std::is_heap_until();
//    std::min();
//    std::max();
//    std::mix_element();
//    std::max_element();
//    std::lexicographical_compare();
//    std::next_permutation();
//    std::prev_permutation();
//
//    std::accumulate();
//    std::inner_product();
//    std::adjacent_difference();
//    std::partial_sum();

/*
    std::all_of(); // C++11
    std::any_of(); // C++11
    std::none_of(); // C++11
    std::is_permutation(); // C++11
    std::find_if_not(); // C++11
    std::copy_n(); // C++11
    std::copy_if(); // C++11
    std::move(); // C++11
    std::move_backward(); // C++11
    std::shuffle(); // C++11
    std::is_partitioned(); // C++11
    std::partition_copy(); // C++11
    std::partition_point(); // C++11
    std::minmax(); // C++11
    std::minmax_element(); // C++11
    std::iota(); // C++11
*/

}
