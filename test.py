from stack import InfixToSuffix, compute, infix, infix_to_suffix, stack, compute_suffix
s = '1+(2×4-5)÷5+sqrt(2)'
q = '1+2+3×sqrt(1)'
t = '1+2×sqrt(3+5)'
w = '1+2^3'
e = '1+2^3×sqrt(3+4)^3'
# # 测试初始栈运算
# s = InfixToSuffix(s)
# print(s)
# s = compute(s)
# print(s)

# # 测试改进后栈运算
# a = stack()
# a = infix(s)
# print(a.listarray)
# b = stack()
# b = infix_to_suffix(a)
# print(b.listarray)
# c = compute_suffix(b)
# print(c)

# # 测试str转化为float
# a = '3.1414'
# b = float(a)
# b = b*2
# print(b)

# # 测试sqrt和pow函数
# import math
# a = float(2.13)
# b = math.sqrt(a)
# c = pow(b, 2)
# print(b)
# print(c)

# # 测试sqrt存入中缀栈操作
# a = infix(q)
# print(a.listarray)
# # 测试sqrt转入后缀栈操作
# b = infix_to_suffix(a)
# print(b.listarray)
# # 测试添入sqrt的运算
# c = compute_suffix(b)
# print(c)

# # 测试运算符'^'
# a = infix(e)
# print(a.listarray)
# b = infix_to_suffix(a)
# print(b.listarray)
# c = compute_suffix(b)
# print(c)

# cccc = '+++++++3'
# cccc = '3+++++++3'
cccc = '2.1-2.2'
# cccc = '6+sqrt(9)'
a = infix(cccc)
print(a.listarray)
b = infix_to_suffix(a)
print(b.listarray)
c = compute_suffix(b)
print(c)
