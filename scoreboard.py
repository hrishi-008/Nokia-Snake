from turtle import Turtle

HIGHSCORE = 0
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.default_score = 0
        self.highScore = HIGHSCORE
        self.up()
        self.goto(0, 310)
        self.write(f'Score ={self.default_score} , HighScore = {self.highScore}', False, 'Center', font=('Arial', 18, 'bold'))

    def increment(self):
        self.default_score += 1

    def update(self):
        self.clear()
        self.up()
        self.goto(0, 310)
        self.write(f'Score = {self.default_score}, HighScore = {self.highScore}', False, 'Center', font=('Arial', 18, 'bold'))


    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='Center', font=('Arial', 18, 'bold'))
