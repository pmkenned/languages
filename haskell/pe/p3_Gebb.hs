module Main where

main :: IO ()
main = print (primeFactors 600851475143)

primes (n:ns) = n : primes (filter ((0/=). flip mod n) ns)

isMultiple t d = (mod t d == 0)

takeFirst _ [] = -1
takeFirst f (x:xs) = if (f x) then x else takeFirst f xs

getFirstPrimeDivisor x = takeFirst (isMultiple x) (primes [2..])

primeFactors 1 = [1]
primeFactors x = d : primeFactors (div x d) where d = getFirstPrimeDivisor x
