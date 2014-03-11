a = 1
b = 2
c = 3
d = 4

main = let y   = a*b
           f x = (x+y)/y
       in do {print $ f c + f d;
              print $ g 7 9 }

g x y | y>z  = 0
      | y==z = 1
      | y<z  = 2
      where z = x*x
