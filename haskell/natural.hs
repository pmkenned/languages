main = print $ take 5 list

list = 0: [x+1 | x <- list ]
