module Main where

main = print $ (5::Integer) `element` ([1, 2, 3, 4, 5] :: [Integer])

element :: (Equality a) => a -> [a] -> Bool

x `element` []     = False
x `element` (y:ys) = x ## y || (x `element` ys)

class Equality a where
 (##), (#$)    :: a -> a -> Bool
 x #$ y        = not (x ## y)     -- default method

instance Equality Integer where
  x ## y       = x == y
