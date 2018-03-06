# My Solution for finding similar number

The problem is to find the count of all possible similar numbers of a given number. A similar number(S) of a given number(N) can be defines as a number which are eqaul in length of N and formed by re-arranging the digits of N.

For example, if N is 121, S can be:
* 121
* 211
* 112

Zeros in the front does not constitute S.

For example, if N is 1200, S can be:
* 1002
* 1020
* 1200
* 2001
* 2010
* 2100

However, in the above case, 0012, 0210, 0120, etc., are not similar to 1200 as there is no value for precedind zeros and the end result will not be an equal digit number.
