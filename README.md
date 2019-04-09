
Inspired by a [Numberphile video](https://www.youtube.com/watch?v=Wim9WJeDTHQ) on the topic, I wanted to personally investigate an algorithmic approach to finding numbers with high multiplicative persistence. 

Multiplicative persistence: multiply the digits of the number together. The product is your new number. Example: 77 -> 49 -> 36 -> 18 -> 8. Four steps to reach a fixed point. 

This is sequence [A003001](https://oeis.org/A003001) in the On-Line Encyclopedia of Integer Sequences. 

It is conjectured that there are no numbers of multiplicative persistence > 11. 

The code uses a depth-first search technique (through recursion) looking for numbers which have a prime factorization composed entirely of 2s, 3s, and 7s.
