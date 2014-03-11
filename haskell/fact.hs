module Main where

main :: IO ()
main = print (factorial 5)

-- Type annotation (optional)
factorial :: Integer -> Integer

-- Using recursion
factorial 0 = 1
factorial n | n > 0 = n * factorial (n - 1)
