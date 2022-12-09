class Game:
    def __init__(self):
        """initializes empty field and players"""
        self.field = Field()
        self.player1 = Player()
        self.player2 = Player()
        self.renderer = Renderer()
        self.is_running = True

    def start(self):
        """and starts a game and holds all logic for that game"""
        while self.is_running:
            self.renderer.render(self.field)
            # make turn
            # check win condition

        # handling result of game


class Player:
    def make_turn(self):
        pass


class Field:
    """Holds a state of a game"""
    def put_value(self, point):
        """puts a value to a filed """
        pass


class Renderer:
    """Renders a filed to a console"""
    def render(self, field):
        pass

#
# class Turn:
#     pass


game = Game()
game.start()