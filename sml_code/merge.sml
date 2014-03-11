(* local
  fun loop (x::y::zs, xs, ys) = loop (zs, x::xs, y::ys)
    | loop (x::[], xs, ys) = (x::xs, ys)
    | loop ([], xs, ys) = (xs, ys)
in
  fun split ns = loop (List.rev ns, [], [])
end *)

fun split ns = let
  fun loop (x::y::zs, xs, ys) = loop (zs, x::xs, y::ys)
    | loop (x::[], xs, ys) = (x::xs, ys)
    | loop ([], xs, ys) = (xs, ys)
in
  loop (List.rev ns, [], [])
end

(* Merge two ordered lists using the order lt.
 * Pre: the given lists xs and ys must already be ordered per lt.
 * Runs in O(n) time, where n = |xs| + |ys|. *)

(* Note: the xs and ys parameters to merge are distinct from the xs and ys
 * parameters for the loop function inside merge *)
fun merge lt (xs, ys) = let
  fun loop (out, left as x::xs, right as y::ys) =
          if lt (x, y) then loop (x::out, xs, right)
          else loop (y::out, left, ys)
    | loop (out, x::xs, []) = loop (x::out, xs, [])
    | loop (out, [], y::ys) = loop (y::out, [], ys)
    | loop (out, [], []) = List.rev out
  in
    loop ([], xs, ys)
  end

fun mergesort lt xs = let
  val merge' = merge lt
  fun ms [] = []
    | ms [x] = [x]
    | ms xs = let
        val (left, right) = split xs
        in
          merge' (ms left, ms right)
        end
  in
    ms xs
  end
