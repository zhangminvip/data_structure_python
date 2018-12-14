class GameEntry:
    '''Represents one entry of a list of high scores'''

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({},{})'.format(self._name, self._score)  # e.g. '(Bob, 98)'

class Scoreboard:
    '''Fixed-length sequence of high scores in nondecreasing order'''

    def __init__(self, capacity=10):
        '''Initialize scoreboard with given maximum capacity

        All entries are initially None
        '''

        self._board = [None] * capacity          # reserve space for future socres
        self._n = 0                              # number of actual entries

    def __getitem__(self, k):
        '''Return entry at index k'''
        return self._board[k]

    def __str__(self):
        '''Return string representation of the high score list'''
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        '''Consider adding entry to high scores'''
        score = entry.get_score()

        
