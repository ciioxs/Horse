from graphics import *
from Dice import Dice
import time   


class Horse:
    def __init__(self, speed, y_pos, image_path, window):
        self.x_pos = 50
        self.y_pos = y_pos
        self.window = window
        self.dice = Dice(speed)

        try:
            self.image = Image(Point(50, y_pos), image_path)
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            self.image = None  

    def move(self):
        roll_value = self.dice.roll()
        self.x_pos += roll_value
        if self.image:
            self.image.move(roll_value, 0)

    def draw(self):
        if self.image:
            self.image.draw(self.window)

    def crossed_finish_line(self, finish_x):
        return self.x_pos >= finish_x


def main():
    # Set up the window
    win = GraphWin("Horse Race", 700, 350)
    win.setBackground("white")

    # Create Horse objects
    horse1 = Horse(10, 100, "Knight.gif", win)
    horse2 = Horse(12, 200, "Wizard.gif", win)

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
    while True:
        time.sleep(0.5)
        horse1.move()
        horse2.move()

        if horse1.crossed_finish_line(600) or horse2.crossed_finish_line(600):
            break   

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
