def is_ancestor(heir, ancestor):
    if ancestor == heir or ancestor in pedigree[heir]:
        return 'Yes'
    else:
        for parent in pedigree[heir]:
            global way_for_search
            way_for_search.add(parent)
        for parent in way_for_search:
            is_ancestor(parent, ancestor)


def add_pedigree(family):
    if ':' in family:
        son, ancestors = family.split(' : ')
        son = son.strip()
        ancestors = ancestors.strip()
        pedigree[son] = ancestors

        for ancestor in ancestors:
            if ancestor not in pedigree.keys():
                pedigree[ancestor] = ''
    else:
        pedigree[family] = ''


way_for_search = set()
pedigree = {}

lst_mro = [  # список введённых строк
    'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    # а теперь другая ветка наследования
    'X',
    'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    'Z : X',
    'V : Z Y',
    'W : V',
]

lst_q = [  # список введённых запросов
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
]

for i in lst_mro:
    add_pedigree(i)

for i in lst_q:
    father, son = i.split()
    ans = is_ancestor(son, father)
    if ans == 'Yes':
        print('Yes')
    else:
        print('No')
'''
n = int(input())
for _ in range(n):
    family = input()
    add_pedigree(family)

n = int(input())
for _ in range(n):
    father, son = input().split()
    ans = is_ancestor(son, father)
    if ans != 'Yes':
        print('No')
    else:
        print('Yes')
'''