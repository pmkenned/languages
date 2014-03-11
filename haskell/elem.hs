module Main where

main = print $ 5 `element` [2, 3, 7, 5, 10]

x `element` []     = False
x `element` ys     = any1 (x==) (ys)

any1 f []     = False
any1 f (x:xs) = (f x) || (any1 f xs)
