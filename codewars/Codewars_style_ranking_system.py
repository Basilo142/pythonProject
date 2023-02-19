# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python

class User:

    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.rank_dict = {
            -8: 0,
            -7: 1,
            -6: 2,
            -5: 3,
            -4: 4,
            -3: 5,
            -2: 6,
            -1: 7,
            1: 8,
            2: 9,
            3: 10,
            4: 11,
            5: 12,
            6: 13,
            7: 14,
            8: 15
        }

    def inc_progress(self, set_rank):

        delta = self.rank_dict[set_rank] - self.rank_dict[self.rank]

        if delta == -1:
            self.progress += 1
        if delta == 0:
            self.progress += 3
        if delta > 0:
            self.progress += 10 * delta ** 2

        delta_rank = self.progress // 100
        value_rank = self.rank_dict[self.rank] + delta_rank
        print('value_rank = {}'.format(value_rank))
        if value_rank not in self.rank_dict.values():
            self.rank = 8
        else:
            for k in self.rank_dict:
                if self.rank_dict[k] == value_rank:
                    self.rank = k

        if self.rank == 8:
            self.progress = 0
        else:
            self.progress -= delta_rank * 100


if __name__ == '__main__':
    user = User()