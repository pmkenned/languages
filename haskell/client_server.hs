module Main where

main = print $ take 10 reqs

reqs                        = client myInit resps
resps                       = server reqs

client myInit ~(resp:resps) = myInit : client (next resp) resps
server      (req:reqs)      = process req : server reqs

myInit                      = 0
next resp                   = resp
process req                 = req+1
