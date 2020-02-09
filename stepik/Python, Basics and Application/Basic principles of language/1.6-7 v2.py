"""def is_ancestor(heir, ancestor):
    if ancestor == heir:
        print('Yes')
        return 0
    elif ancestor in pedigree[heir]:
        print('Yes')
        return 0
    else:
        for parent in pedigree[heir]:
            is_ancestor(parent, ancestor)
        return 1"""


def is_ancestor(heir, ancestor):
    if ancestor == heir or ancestor in pedigree[heir]:
        return 'Stop'
    else:
        return 'Continue'


def find_way(heir, ancestor):
    if is_ancestor(heir, ancestor) == 'Continue':
        for parent in pedigree[heir]:
            if is_ancestor(parent, ancestor) == 'Stop':
                break
            else:
                find_way(parent, ancestor)
        print('No')
    else:
        print('Yes')


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


pedigree = {}
n = int(input())
for _ in range(n):
    family = input()
    add_pedigree(family)

n = int(input())
for _ in range(n):
    father, son = input().split()
    find_way(son, father)
