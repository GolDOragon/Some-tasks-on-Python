'''
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

'''


def is_ancestor(heir, ancestor):
    if ancestor in pedigree[heir] or heir == ancestor:
        print('Yes')
        return False
    return True





def add_pedigree(stroka):
    def add_family(heir, parents=[]):
        pedigree[heir] = parents

    if ':' in stroka:
        cl, parents = stroka.split(':')
        add_family(cl.strip(), parents.split())
    else:
        cl = stroka
        add_family(cl)


pedigree = {}

########################
list_to_input = ['classA : classB classC classD classG classH', 'classB : classC classE classG classH classK classL', 'classC : classE classD classH classK classL', 'classE : classD classF classK classL', 'classD : classG classH', 'classF : classK', 'classG : classF', 'classH : classL', 'classK : classH classL', 'classL']#10
list_to_question=['classK classD', 'classD classA', 'classG classD', 'classH classA', 'classE classE', 'classH classG', 'classE classL', 'classB classD', 'classD classL', 'classD classG', 'classD classE', 'classA classF', 'classA classC', 'classK classA', 'classA classH', 'classK classD', 'classH classB', 'classK classB', 'classD classL', 'classG classG', 'classA classH', 'classK classL', 'classG classE', 'classB classA', 'classC classK', 'classK classL', 'classC classL', 'classG classC', 'classD classD', 'classC classG', 'classE classA', 'classF classK', 'classB classG', 'classH classL', 'classL classF', 'classH classG', 'classD classA', 'classH classL']#38
answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']#38
#########################

#n = int(input())
n = 10
for _ in range(n):
    add_pedigree(list_to_input[_])

n = 38
for _ in range(n):
    ancestor, heir = list_to_question[_].split()
    if is_ancestor(heir, ancestor):
        for parent in pedigree[heir]:
            is_ancestor(parent, ancestor)
        print("No")
