class tic_tac_toe():
    '''TicTacToe playing class, contains board information, and will play against human
       player, will actively try to lose the game, this challenge is difficult, and will
       require understanding object oriented programming in python.
    '''
    def __init__(self):
        '''Constructor, will establish board state, and will determine whether the player
           plays as X or O.
        '''
        self.board = [[" "," "," "],
                      [" "," "," "],
                      [" "," "," "]]
        self.player_choice = int(raw_input("would you like to go first? (0,1)"))
        if self.player_choice == 0:
            self.play = "O"
            self.AI = "X"
        else:
            self.play = "X"
            self.AI = "O"
            
    def draw_board(self):
        '''Draws board state to standard output, used by other prompts.
        '''
        print "|--|--|--|"
        for line in self.board:
            print "|"+" |".join(line)+" |"
            print "|--|--|--|"
        return

    def player(self):
        '''Displays board state, and then asks player to make a move, delivers errors
           if player requests an impossible position, and updates board when valid position
           given.
        '''
        while True:
            self.draw_board()
            print "Specify where you want to place your piece (you are "+self.play+"):"
            xcoord = int(raw_input("xccord (0-2)?"))
            if not 0<= int(xcoord) <=2:
                print "out of bounds"
                continue
            ycoord = int(raw_input("yccord (0-2)?"))
            if not 0<=int(ycoord)<=2:
                print "out of bounds"
                continue
            if self.board[xcoord][ycoord] != " ":
                print "postion already in use"
                continue
            else:
                self.board[xcoord][ycoord] = self.play
                break
        return

    def score_position(self, x, y):
        '''Scores positions by attractiveness, used by AI to determine worst possible
           place to play.
        '''
        score = -5
        AIbias = 15
        playbias = 10
        for i in xrange(3):
            if self.board[(x+i)%3][y] == self.AI:
                score -= AIbias
            if self.board[(x+i)%3][y] == self.play:
                score += playbias
            if self.board[x][(y+i)%3] == self.AI:
                score -= AIbias
            if self.board[x][(y+i)%3] == self.play:
                score += playbias
        if (x == 0 or x == 3) and (y == 0 or y == 3):
            for i in xrange(3):
                if self.board[(x+i)%3][(y+i)%3] == self.AI:
                    score -= AIbias
                if self.board[(x+i)%3][(y+i)%3] == self.play:
                    score += playbias
        if x == 1 and y == 1:
            score -= 50
        return abs(score)

    def play_AI(self):
        '''Determines worst possible place for the AI to play and then plays it.
        '''
        score_list = []
        for xval in xrange(3):
            for yval in xrange(3):
                if self.board[xval][yval] == " ":
                    score_list.append((xval, yval, self.score_position(xval, yval)))
        score_list = sorted(score_list, key=lambda i: i[2])
        top_score = score_list[0]
        self.board[top_score[0]][top_score[1]] = self.AI
        return

    def win_condition(self):
        '''Determines whether or not a player has won, prints winning message to standard
           output and returns boolean for main game engine.
        '''
        for val in xrange(3):
            if (self.board[val].count("X") == 3 or
                [line[val] for line in self.board].count("X") == 3):
                print "X wins!"
                return False
            if (self.board[val].count("O") == 3 or
                [line[val] for line in self.board].count("O") == 3):
                print "O wins!"
                return False
        if ([self.board[v][v] for v in xrange(3)].count("X") == 3 or
            [self.board[-(v+1)][v] for v in xrange(3)].count("X") == 3):
            print "X wins!"
            return False
        if ([self.board[v][v] for v in xrange(3)].count("O") == 3 or
            [self.board[-(v+1)][v] for v in xrange(3)].count("O") == 3):
            print "O wins!"
            return False
        return True

    def play_game(self):
        '''Plays the game!, uses move updaters for player and AI until either a win condition
           or a draw condition is reached.
        '''
        counter = 0
        if self.AI == "X":
            self.play_AI()
            counter += 1
        while self.win_condition() and counter < 10:
            self.player()
            counter += 1
            if not self.win_condition():
                break
            self.play_AI()
            counter += 1
        if self.win_condition():
            print "Game ended in a draw"
        return
            
tic_tac_toe().play_game()
