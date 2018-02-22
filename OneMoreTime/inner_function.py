def marker(N):
    def action(X, N=N):
        print(X ** N)
    return action

f = marker(2)
# f(8)

# def marker(x):
#     action = (lambda n: x ** n)
#     return action
#
# f = marker(2)
