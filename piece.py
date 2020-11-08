class Piece:
    def __init__(self, team, pos):
        self.team = team
        self.name = f'team{team}{pos}'
        self._pos_zero = f'b{pos}'
        self._pos = f'b{pos}'

    def _get_pos(self):
        return self._pos

    def _set_pos(self, pos):
        try:
            self._pos = pos
            return True
        except:
            return False
    
    def move(self, pos):
        p0 = self._get_pos()
        return self._set_pos(pos), p0

    def hit(self):
        self._set_pos(self._pos_zero)


        


