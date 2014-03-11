main = do { putStrLn $ copies 5 'x';
            putStrLn $ take 5 ['a' | x <- [0..]] }

copies 0 x = []
copies 1 x = [x]
copies n x = x : copies (n-1) x
