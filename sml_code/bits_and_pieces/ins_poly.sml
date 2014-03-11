(* Note: << is nothing special; it's a name for the ordering operator *)
(* Could have used, say, 'lt' *)

fun ins' << (num, nums) = let
  fun i (n, []) = [n]
    | i (n, ns as h::t) = if << (n,h) then n::ns else h::i(n,t)
in
  i (num, nums)
end
fun insertionSort' << = List.foldr (ins' <<) []
