class Npc:

    def __init__(self):
        # self.name_npc = None
        self.hp = 0

        print('start')

    def add_nam(self, name_npc):

        self.name_npc = name_npc
        print('name_Classs')

    def name(self):
        if self.name_npc:
            print('Name -', self.name_npc.title())
        else:
            print("Upssss")

    def added_hp(self, hp):
        self.hp = self.hp + hp

    def how_hp(self):
        print('hpeshek-'+ str(self.hp))


class Npc_freands(Npc):

    def __init__(self):
        pass
        # super().__init__()


if __name__ == '__main__':


    a = Npc()
    a.add_nam('ss')
    a.added_hp(456)
    a.how_hp()

    b = Npc_freands()
    b.add_nam('asas')
    b.name()
    b.name()
    print(a.hp)


