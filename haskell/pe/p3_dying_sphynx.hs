module Main where

main :: IO ()
main = print (head (factorize 600851475143 []))

mind x = head [y | y <- [2..], x `mod` y == 0]
factorize 1 l = l
factorize p l = factorize (p `div` (mind p)) l++[mind p]
