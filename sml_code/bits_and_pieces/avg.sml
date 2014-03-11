fun length [] = 0
  | length (x::xs) = 1 + length xs

fun sum [] = 0
  | sum (x::xs) = x + sum xs

fun avg [] = 0
  | avg xs = sum(xs) div length(xs)

val xs = [1, 5, 3, 7, 8];
print (Int.toString(length(xs)) ^ "\n");
print (Int.toString(sum(xs)) ^ "\n");
print (Int.toString(avg(xs)) ^ "\n");
