from random import randrange

class TicTacToe:
    win_combinations=['012','036','048','258','678','246','147','345']
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def aimove(self,aitoken):
        move=999
        for i in self.win_combinations:
                #Check For AI Win Opportunities
                #Check For Player Win Opportunities
            for univ_token in [self.usrtoken,aitoken]:
                if self.board[int(i[0])]==univ_token:
                    if self.board[int(i[1])]==univ_token and self.board[int(i[2])]==' ':
                        move=int(i[2])
                        break
                    elif self.board[int(i[2])]==univ_token and self.board[int(i[1])]==' ':
                        move=int(i[1])
                        break
                elif self.board[int(i[1])]==univ_token:
                    if self.board[int(i[2])]==univ_token and self.board[int(i[0])]==' ':
                        move=int(i[0])
                        break
                    elif self.board[int(i[0])]==univ_token and self.board[int(i[2])]==' ':
                        move=int(i[2])
                        break
                elif self.board[int(i[2])]==univ_token:
                    if self.board[int(i[1])]==univ_token and self.board[int(i[0])]==' ':
                        move=int(i[0])
                        break
                    elif self.board[int(i[0])]==univ_token and self.board[int(i[1])]==' ':
                        move=int(i[1])
                        break
        if move==999:
            move=randrange(0,9)
            while self.board[move]!=' ':
                move=randrange
        return move

    def check_win(self):
        for i in self.win_combinations:
            if self.board[int(i[1])]!=' ' and self.board[int(i[0])]==self.board[int(i[1])] and self.board[int(i[1])]==self.board[int(i[2])]:
                return True
        return False


    def printboard(self):
        print(
        '''
        {}|{}|{}
        {}|{}|{}
        {}|{}|{}
        '''.format(self.board[0],self.board[1],self.board[2],self.board[3],self.board[4],self.board[5],self.board[6],self.board[7],self.board[8]))

    def __init__(self):
        print("Are you 'X' or 'O'?(X/O): ")
        while True:
            self.usrtoken=input()
            if self.usrtoken=='X' or self.usrtoken=='x':
                self.usrtoken='X'; aitoken='O'
            elif self.usrtoken=='O' or self.usrtoken=='o':
                self.usrtoken='O'; aitoken='X'
            else:
                print("Invalid character selected!")
                continue
            break
        while True:
            print("Your Move! [1-9]:")
            self.printboard()
            while True:
                try:
                    usrinput=int(input("> "))-1
                except:
                    print("Disallowed Move!")
                    continue
                if usrinput<0 or usrinput>8 or self.board[usrinput]!=' ':
                    print("Disallowed Move!")
                else:
                    break
            self.board[usrinput]=self.usrtoken
            if self.check_win():
                self.printboard()
                print("Congratulations, You Won!")
                break
            if ' ' not in self.board:
                self.printboard()
                print("It's a Draw!")
                break
            self.board[self.aimove(aitoken)]=aitoken
            if self.check_win():
                self.printboard()
                print("You Lost!")
                break
if __name__ == '__main__':
    TicTacToe()