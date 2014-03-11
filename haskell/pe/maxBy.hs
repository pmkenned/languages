-- should probably be updated to use Ord class
-- should probably use a compare function which
--  returns -1,0,1 instead of a Bool

main = print $ maximumBy (>) [1,2,3,0]

maximumBy :: (a -> a -> Bool) -> [a] -> a
maximumBy f (x:xs) = maximumBy' f x xs

maximumBy' :: (a -> a -> Bool) -> a -> [a] -> a
maximumBy' f m [] = m
maximumBy' f m (x:xs) = if (f m x) then maximumBy' f m xs else maximumBy' f x xs
