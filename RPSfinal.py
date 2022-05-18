
import random

moves = ['rock', 'paper', 'scissors']


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Sorry, the option:"{option}" is invalid. Try again')


class Player:

    def learn(self, my_move, their_move):
        pass


class rocky(Player):
    def move(self):
        return 'rock'


class rando(Player):
    def move(self):
        return random.choice(moves)


class human(Player):
    def move(self):
        Inputs.move_selection("move_selection")
        return Inputs.human_move


class reflector(Player):
    movesmade = 0

    def move(self):
        reflector.movesmade += 1
        if reflector.movesmade == 1:
            return 'rock'
        else:
            return reflector.last_round

    def learn(self, my_move, their_move):
        if their_move == 'rock':
            reflector.last_round = 'rock'
        if their_move == 'paper':
            reflector.last_round = 'paper'
        if their_move == 'scissors':
            reflector.last_round = 'scissors'


class cycler(Player):

    move_cycler = 0

    def move(self):
        cycler.move_cycler += 1
        if cycler.move_cycler % 3 == 0:
            return 'rock'
        if cycler.move_cycler % 3 == 1:
            return 'paper'
        if cycler.move_cycler % 3 == 2:
            return 'scissors'


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        humanmove = self.p1.move()
        aimove = self.p2.move()
        print(f"Player 1: {humanmove}  Player 2: {aimove}")
        self.p1.learn(humanmove, aimove)
        self.p2.learn(aimove, humanmove)
        Game_engine.permutations("permutations", humanmove, aimove)

    def play_game(self):
        print("Game start!")
        while Inputs.total_rounds > (Game.p1_score + Game.p2_score):
            self.play_round()
        print("Game over!")


class Game_engine():

    def permutations(self, humanmove, aimove):
        hm = humanmove
        aim = aimove
        print(f"Human plays {hm}")
        print(f"Ai plays {aim}")
        if hm == aim:
            print('draw')
        if (hm+aim) == 'paperrock' or 'rockpaper':
            Game_engine.p_r('p_r', (hm+aim))
        if (hm+aim) == 'paperscissors' or 'scissorspaper':
            Game_engine.s_p('s_p', (hm+aim))
        if (hm+aim) == 'rockscissors' or 'scissorsrock':
            Game_engine.r_s('r_s', (hm+aim))

    def p_r(self, order):
        if order == 'paperrock':
            Game_engine.human_wins('human_wins')
        if order == 'rockpaper':
            Game_engine.ai_wins('ai_wins')

    def s_p(self, order):
        if order == 'scissorspaper':
            Game_engine.human_wins('human_wins')
        if order == 'paperscissors':
            Game_engine.ai_wins('ai_wins')

    def r_s(self, order):
        if order == 'rockscissors':
            Game_engine.human_wins('human_wins')
        if order == 'scissorsrock':
            Game_engine.ai_wins('ai_wins')

    def human_wins(self):
        Game.p1_score += 1
        print("player wins")
        print(f"Human {Game.p1_score} vs AI {Game.p2_score}")

    def ai_wins(self):
        Game.p2_score += 1
        print("AI wins")
        print(f" {Game.p1_score} vs {Game.p2_score}")


class Inputs:
    human = ('yes')
    possible_opponents = ('a.Rock', 'b.Rando', 'c.Reflector', 'd.Cycler')
    total_rounds = 0

    def round_or_match(self):
        print("would you like to play a full match or a singular round")
        print("select A for singular round")
        print("select B for full match")
        choice = valid_input("Select:", ['a', 'b'])
        if choice == 'a':
            Launcher.single_round = 'yes'
        if choice == 'b':
            Launcher.single_round = 'no'
            Inputs.intro_option('intro_option')

    def intro_option(self):
        print("You can play best out of 3,5 or 7 rounds")
        print("a draw is not scored")
        print("select '3', '5', '7'")
        choice = valid_input("Select: ", ['3', '5', '7'])
        if choice == '3':
            Inputs.total_rounds += 3
        elif choice == '5':
            Inputs.total_rounds += 5
        elif choice == '7':
            Inputs.total_rounds += 7

    def player_selection(self):

        print("please select your opponent")
        print(Inputs.possible_opponents)
        choice = valid_input("Select: ", ['a', 'b', 'c', 'd'])
        if choice == 'a':
            Inputs.player_selected = 'Rock'
        if choice == 'b':
            Inputs.player_selected = 'Rando'
        if choice == 'c':
            Inputs.player_selected = 'Reflector'
        if choice == 'd':
            Inputs.player_selected = 'Cycler'

    def move_selection(self):
        print("please select your move")
        print(moves)
        choice = valid_input("Select: ", ['rock', 'paper', 'scissors'])
        if choice == 'rock':
            Inputs.human_move = 'rock'
        elif choice == 'paper':
            Inputs.human_move = 'paper'
        elif choice == 'scissors':
            Inputs.human_move = 'scissors'


class Launcher:

    def launch_game(self):
        Inputs.round_or_match("round_or_match")
        Inputs.player_selection("player_selection")
        if Inputs.player_selected == 'Rock':
            Launcher.launch_rock('launch_rock')
        if Inputs.player_selected == 'Rando':
            Launcher.launch_rando('launch_rando')
        if Inputs.player_selected == 'Reflector':
            Launcher.launch_reflector('launch_reflector')
        if Inputs.player_selected == 'Cycler':
            Launcher.launch_cycler('launch_cycler')

    def launch_rock(self):
        game = Game(human(), rocky())
        if Launcher.single_round == 'no':
            game.play_game()
        if Launcher.single_round == 'yes':
            game.play_round()

    def launch_rando(self):
        game = Game(human(), rando())
        if Launcher.single_round == 'no':
            game.play_game()
        if Launcher.single_round == 'yes':
            game.play_round()

    def launch_reflector(self):
        game = Game(human(), reflector())
        if Launcher.single_round == 'no':
            game.play_game()
        if Launcher.single_round == 'yes':
            game.play_round()

    def launch_cycler(self):
        game = Game(human(), cycler())
        if Launcher.single_round == 'no':
            game.play_game()
        if Launcher.single_round == 'yes':
            game.play_round()


if __name__ == '__main__':
    Launcher.launch_game("launch_game")
