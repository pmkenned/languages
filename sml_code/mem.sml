infix mem;
fun (x mem []) = false
  | (x mem (y::l)) = (x=y) orelse (x mem l);

fun newmem(x,xs) = if x mem xs then xs else x::xs;

fun union([],ys) = ys
  | union(x::xs,ys) = newmem(x, union(xs,ys));

fun union_node([]) = []
  | union_node( (x:int * int list)::xs) = union(#2 x, union_node(xs));

(* union_node_n( 1,[ (1,[2,3]), (1,[1,3]), (3,[1,2])] ); *)

fun listByRemovingElement([], element) = [] 
    | listByRemovingElement(headElement :: tailElements, element) =
          if (element = headElement) then
              listByRemovingElement(tailElements, element)
          else
              headElement :: listByRemovingElement(tailElements, element);
  
fun listByRemovingElements(l, nil) = l
  | listByRemovingElements(l, headElement :: tailElements) =
    listByRemovingElement(listByRemovingElements(l, tailElements), headElement)
  
fun removeDuplicatesFromList([]) = []
  | removeDuplicatesFromList(headElement :: tailElements) = (headElement :: (removeDuplicatesFromList(listByRemovingElement(tailElements, headElement))));

fun nth_item([],n) : int = 0
  | nth_item(x::xs,n) : int = if(n=0) then x else nth_item(xs,n-1);

(*fun merge_node(n : int, xs : int list, G: int * int list) : int * int list = *)


val l = [1,2,3];
val n : int = nth_item(l,1);

merge_node(n,listByRemovingElement(l,n),G);
