# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

users = ['user1', 'user2', 'user3', 'user4', 'user5']

data = list(enumerate(users))
print(data)
# [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]

# --------------------------------------------------------------------

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)

# [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# ------------------------------------------------------------------

li = [x for x in range(1, 20)]

li = list(map(lambda x: x + 10, li))
print(li)

# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# ----------------------------------------------------------------

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
print(list(res))

# [2, 8, 38]


