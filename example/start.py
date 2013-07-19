import sys
import pantograph
import random

class BouncingBall(pantograph.PantographHandler):
    def setup(self):
        self.x = 100
        self.y = 100
        self.xvel = random.randint(1, 5)
        self.yvel = random.randint(1, 5)

    def update(self):
        if self.x <= 0 or self.x >= self.width:
            self.xvel *= -1
        if self.y <= 0 or self.y >= self.height:
            self.yvel *= -1

        self.x += self.xvel
        self.y += self.yvel

        self.clear_rect(0, 0, self.width, self.height)
        self.draw_image("baseball.jpg", self.x, self.y, 20, 20)


if __name__ == '__main__':
    app = pantograph.SimplePantographApplication(BouncingBall)
    app.run()
