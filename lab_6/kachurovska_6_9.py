strit = input()
op = "+/-*%**//"
k = strit.count("**")
l = strit.count("*")
m = strit.count("//")
n = strit.count("/")
l -= k
n -= m
summ_op = l + n + strit.count("+") + strit.count("-") + strit.count("%")
print(summ_op)