# U1551284 by Yeji Kim

from graphics import *
from Dice import Dice


class Horse:
    def __init__(self, speed, y_pos, image, window):
        self.x_pos = 50
        self.y_pos = y_pos
        self.image = image
        self.dice = Dice(speed)
        self.window = window

    def move(self):
        roll_value = self.dice.roll()
        self.x_pos += roll_value
        self.image.move(roll_value, 0)  

    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, finish_x):
        return self.x_pos >= finish_x


def main():
    # Set up the window
    win = GraphWin("Horse Race", 700, 350)
    win.setBackground("white")

    # Load horse images (Ensure files exist in the directory)
    try:
        knight_image = Image(Point(50, 100), "Knight.gif")
        wizard_image = Image(Point(50, 200), "Wizard.gif")
    except Exception as e:
        print("Error loading images:", e)
        win.close()
        return

    # Create Horse objects
    horse1 = Horse(10, 100, knight_image, win)
    horse2 = Horse(12, 200, wizard_image, win)

    # Draw horses and finish line
    horse1.draw()
    horse2.draw()
    finish_line = Line(Point(600, 50), Point(600, 300))
    finish_line.setWidth(3)
    finish_line.setFill("red")
    finish_line.draw(win)

    # Wait for user click to start
    win.getMouse()

    # Start the race loop
    while not horse1.crossed_finish_line(600) and not horse2.crossed_finish_line(600):
        time.sleep(0.5)
        horse1.move()
        horse2.move()
        win.update()

    # Determine the winner
    if horse1.crossed_finish_line(600) and horse2.crossed_finish_line(600):
        print("Tie")
    elif horse1.crossed_finish_line(600):
        print("Knight is the winner!")
    else:
        print("Wizard is the winner!")

    # Wait for final click before closing
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
