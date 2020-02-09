'''
Реализуйте программу, которая будет эмулировать работу с пространствами имен.
Необходимо реализовать поддержку создания пространств имен и добавление в них
переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый
идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем
<namespace> внутри пространства <parent>

add <namespace> <var> – добавить в пространство <namespace> переменную <var>

get <namespace> <var> – получить имя пространства, из которого будет взята
переменная <var> при запросе из пространства <namespace>, или None, если такого
 пространства не существует

'''


def create_namespace(name, primary_space):
    if primary_space in dct.keys():
        dct[primary_space][1].append(name)
        dct[name] = [primary_space, []]


def add_variable(variable, space):
    if space in dct.keys():
        dct[space][1].append(variable)


def get_name_of_vars_space(var, space):
    if space == 'None':
        print('None')
        return
    if var in dct[space][1]:
        print(space)
        return
    else:
        up_space = dct[space][0]
        get_name_of_vars_space(var, up_space)


dct = {'global': ['None',[]]}
n = int(input())

for _ in range(n):
    cmd, namespace, var = input().split()

    if cmd == 'create':
        create_namespace(namespace, var)
    elif cmd == 'add':
        add_variable(var, namespace)
    elif cmd == 'get':
        get_name_of_vars_space(var, namespace)