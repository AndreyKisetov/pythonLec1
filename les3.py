# def f(x):
#     return x**2
# g = f
# print(type(f))
# print(type(g))
# print(f(4))
# print(g(4))


# def calc1(x):
#     return x+10
# # print(calc1(10))
# def calc2(x):
#     return x*10
# # print(calc2(10))
# def math(op, x):
#     print(op(x))
# math(calc2, 10)
# math(calc1, 10)


# def sum(x, y):
#     return x+y
# f = lambda x, y: x+y+2
# def mult(x, y):
#     return x*y
# def calc(op, a, b):
#     print(op(a, b))
    # return op(a, b)
# calc(f, 6, 5)
# calc(lambda x, y: x+y+2, 4, 5)


# list = []
# for i in  range(1, 101):
#     if(i%2 == 0):
#         list.append(i)
# print(list)


# def f(x):
#     return x**2
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)


# a = [1, 2, 3, 5, 8, 15, 23, 38]
# def f(x):
#     return x**2
# list = [(i, f(i)) for i in a if i % 2 == 0]
# print(list)


# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3  5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x:(x, x**2), res)
# print(res)


# li = [x for x in range(1,20)]
# li = list(map(lambda x:x+10, li))
# print(li)


# data = list(map(input().split()))
# print(data)
