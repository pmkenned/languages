module Main where

main = print $ take 5 fib

fib@(1:tfib) = 1 : 1 : [ a+b | (a,b) <- zip fib tfib ]
