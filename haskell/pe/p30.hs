module Main where

main = print $ sum $ map snd list'

list = zip [2..] (map (sum . map (^5)) (map digits [2..1000000]))
list' = filter (\(x,y) -> x==y) list

digits 0 = []
digits x = (x `mod` 10) : digits (x `div` 10)
