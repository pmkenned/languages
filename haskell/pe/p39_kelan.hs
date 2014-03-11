module Main where

main = print answer

triples top =
    [ [v^2-u^2, 2*u*v, u^2+v^2] |
      u <- [1..top],
      v <- [(u+1), (u+3)..top],
      gcd u v == 1 ]

answer =
    head $
    maximumBy (\a b -> compare (length a) (length b) ) $
    group $ -- this function needs to be defined
    quicksort $ -- list of lists?
    concat $
    map (\s -> [s,(2*s)..999]) $
    map sum $
    triples 50

maximumBy :: (a -> a -> Bool) -> [a] -> a
maximumBy f (x:xs) = maximumBy' f x xs

maximumBy' :: (a -> a -> Bool) -> a -> [a] -> a
maximumBy' f m [] = m
maximumBy' f m (x:xs) = if (f m x) then maximumBy' f m xs else maximumBy' f x xs

quicksort (x:xs) = quicksort [y | y <- xs, y<x] ++ [x] ++ [z | z <- xs, z>=x]
