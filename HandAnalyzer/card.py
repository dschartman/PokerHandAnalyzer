from .exceptions import InvalidCardException

class Card(object):
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.rank_value = self._get_rank_value(rank)
        self.suit = suit

    def _get_rank_value(self, rank: str):
        if rank == 'T':
            return 10
        
        if rank == 'J':
            return 11

        if rank == 'Q':
            return 12

        if rank == 'K':
            return 13
        
        if rank == 'A':
            return 14

        try:
            return int(rank)
        except:
            raise InvalidCardException(f'Expected a valid card rank.  Received {rank}!')