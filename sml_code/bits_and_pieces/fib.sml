fun nextfib(prev, curr :int) = (curr, prev+curr);

fun fibpair(n) = 
  if n=1 then (0,1) else nextfib(fibpair(n-1));

fun itfib (n, prev, curr) : int =
  if n=1 then curr
  else itfib (n-1, curr, prev+curr);
