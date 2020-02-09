monstres = '''
skeleton
ghost
jack
vampire
witch
mummy
zombie
werewolf
frankenstein
'''


def halloween_monsters(spell: str)-> int:

    def look_monster(monster: str, lst: list):

        ln_monster = len(monster)
        copy_list = lst[:]
        word = []
        ans = ''
        for i in range(ln_monster):
            if monster[i] in copy_list:
                num = copy_list.index(monster[i])
                word.append(copy_list.pop(num))
        for x in word:
            ans += x
        if monster == ans:
            nonlocal count, cp_spell
            count += 1
            cp_spell = copy_list[:]
            return True
        else:
            return False


    MONSTERS = monstres.rsplit()
    cp_spell = list(spell)
    count = 0

    for monster in MONSTERS:
        condition = look_monster(monster, cp_spell)
        while condition:
            condition = look_monster(monster, cp_spell)

    return count


if __name__ == '__main__':
    assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
    print("Your spell seem to be okay. It's time to check.")