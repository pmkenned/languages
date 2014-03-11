fun ins (n, []) = [n]
  | ins (n, ns as h::t) = if (n<h) then n::ns else h::(ins (n, t))
val insertionSort = List.foldr ins []
