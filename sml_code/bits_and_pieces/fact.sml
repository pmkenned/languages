fun fact n : IntInf.int =
  if n=0 then 1 else n * fact(n-1)


fun fact_tail n : IntInf.int = let
  fun lp (0,acc) = acc
    | lp (m,acc) = lp (m-1,acc*m)
  in
    lp (n,1)
  end;

val () =
  print (IntInf.toString(fact_tail (500)) ^ "\n");

val () =
  print (IntInf.toString(fact 120) ^ "\n");
