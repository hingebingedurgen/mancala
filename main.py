from __future__ import annotations

class Pocket:
    def __init__(self, is_mancala: bool, whose_pocket: int, next: Pocket, adjacent: Pocket) -> None:
        self.is_mancala = is_mancala
        self.num_stones = 0
        self.whose_pocket = whose_pocket
        self.next = next
        self.adjacent = adjacent
    
class Board:
    def __init__(self) -> None:
        self.pockets = self._initialize_pockets()
        self.whose_turn = 0
    
    def _initialize_pockets(self):
        pockets = []
        for i in range(14):
            if i % 7 == 0:
                if i < 7:
                    pocket = Pocket(is_mancala=True, whose_pocket=0, next=None, adjacent=None)
                else:
                    pocket = Pocket(is_mancala=True, whose_pocket=1, next=None, adjacent=None)
            else:
                if i < 7:
                    pocket = Pocket(is_mancala=False, whose_pocket=0, next=None, adjacent=None)
                else:
                    pocket = Pocket(is_mancala=False, whose_pocket=1, next=None, adjacent=None)
            pockets.append(pocket)
        
        for i in range(1, len(pockets)):
            pockets[i-1].next = pockets[i]
            pockets[i].adjacent = pockets[len(pockets)-i]
            pockets[len(pockets)-i].adjacent = pockets[i]
        pockets[len(pockets)-1].next = pockets[0]

        return pockets



if __name__ == '__main__':
    board = Board()
    for i in range(len(board.pockets)):
        print(i)
        print(board.pockets[i].is_mancala)
        print(board.pockets[i].whose_pocket)
        print()
        