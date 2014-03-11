module Main where

main = print (take 5 (iter (2*) 10))

iter :: (a->a) -> a -> [a]

iter f x = x : iter f (f x)
