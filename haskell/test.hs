module Main where

main = do {print (double_and_inc 5); print (take 5 squares)}

bar = map (\x -> x + 1) [1, 2, 3]

double_and_inc = inc . double

double x = 2*x
inc x = x + 1

numsFrom n = n : numsFrom(n+1)

squares = map (^2) (numsFrom 0)

foo :: [a] -> a
foo (x:xs) = x

data Point a = Pt a a

divisible :: Integer -> Integer -> Bool

divisible x n = (x`mod`n == 0)
