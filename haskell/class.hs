module Main where

main = do print $ f (5 :: Integer)
          print $ g (5 :: Integer)
          print $ h 'c'
          print $ h (5 :: Integer)

-- Foo is a subclass of Num. It thus inherits the Num operators.
class (Num a) => (Foo a) where
  f  :: a -> a
  g  :: a -> a
  g x = 3*x      -- default

instance Foo Integer where
  f x = 2*x

-- Bar class

class Bar a where
  h :: a -> [a]
  h x = x : [x]  -- default

instance Bar Char
instance Bar Int
instance Bar Integer where
  h x = [x,x,x]

-- Ham class

class Ham a
