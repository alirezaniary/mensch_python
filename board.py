class Board:
    def __init__(self):
        self._pos = [f'{x:02}' for x in range(40)]
        self._team_start_pos = {'A': 0, 'B': 10, 'C': 20, 'D': 30}
        self._base_team = {team: [f'{team}b{x}' for x in range(4)] for team in 'ABCD'}
        self._target_team = {team: [f'{team}t{x}' for x in range(4)] for team in 'ABCD'}

        self._positions = {}
        for t in 'ABCD':
            for x in self.get_track(t):
                self._positions[x] = None

    def get_track(self, team):
        return self._base_team[team] + \
               self._pos[self._team_start_pos[team]:] + \
               self._pos[:self._team_start_pos[team]] + \
               self._target_team[team]

    def set_pos(self, piece, pos):
        self._positions[pos] = piece

    def is_empty(self, pos):
        if self._positions[pos] == None:
            return True
        else:
            return False


if __name__ == '__main__':
    B = Board()
    print(B._positions)
