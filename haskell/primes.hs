main = print (primes 100)

primes :: Integral a => a -> [a]
primes 2 = [2]
primes n = 2:[i | i<- [3,5..n], all (\k -> (mod i k /= 0)) (primes $ isqrt i)]

isqrt x = truncate $ sqrt $ fromIntegral x
