module Main where

main = move 5 5 1

move 1 m d = do { putStr (take m spaces) ;
                  putStr "moving disc of size ";
                  putStr (show m);
                  case (d) of
                    0 -> putStrLn " left"
                    1 -> putStrLn " right" 
                }

move n m d = do { move (n-1) (n-1) ((d+1) `mod` 2);
                  move 1 n d ;
                  move (n-1) (n-1) ((d+1) `mod` 2) }

spaces = ' ' : spaces
