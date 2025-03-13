#A2: A Horse Race by Yeji Kim U1551284

from graphics import GraphWin, Image, Line, Point  # Import necessary elements from the graphics module
from Dice import Dice
import time

# Create the class for Horse
class Horse:
    def __init__(self, speed, y_pos, image_path, window):
        self.x_pos = 0  # Initial horizontal position of the horse
        self.y_pos = y_pos  # Vertical position of the horse
        self.window = window  # Graphical window where the horse will move
        self.dice = Dice(speed)  # Create a Dice object to determine the horse's movement

        try:
            self.image = Image(Point(self.x_pos, self.y_pos), image_path)  # Load the horse's image
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")  # Print error message if image loading fails
            self.image = None  # Set the image to None if loading fails

    # Method to move the horse based on the dice roll
    def move(self):
        roll_value = self.dice.roll()  # Roll the dice to get the movement value
        self.x_pos += roll_value  # Update the horse's position based on the roll value
        if self.image:
            self.image.move(roll_value, 0)  # Move the horse's image on the screen

    # Method to draw the horse on the window
    def draw(self):
        if self.image:
            self.image.draw(self.window)  # Draw the image on the graphical window

    # Method to check if the horse has crossed the finish line
    def crossed_finish_line(self, finish_x):
        return self.x_pos >= finish_x  # Returns True if the horse has crossed the finish line

def main():
    # Create the graphical window for the race
    win = GraphWin("Horse Race", 700, 350)
    win.setBackground("white")  # Set the background color of the window

    # Load the images for the horses
    horse1_image = "Knight.gif"
    horse2_image = "Wizard.gif"

    # Create Horse objects with different speeds and positions
    horse1 = Horse(10, 100, horse1_image, win)
    horse2 = Horse(12, 200, horse2_image, win)

    # Draw the horses on the screen
    horse1.draw()
    horse2.draw()

    # Draw the finish line on the screen
    finish_line = Line(Point(600, 50), Point(600, 300))
    finish_line.setWidth(3)  # Set the width of the finish line
    finish_line.setFill("red")  # Set the color of the finish line to red
    finish_line.draw(win)  # Draw the finish line on the window

    # Wait for the user to click to start the race
    win.getMouse()

    # Start the race loop
    while not horse1.crossed_finish_line(600) and not horse2.crossed_finish_line(600):
        time.sleep(0.01)  # Add a small delay to control the speed of the race
        horse1.move()  # Move horse1
        horse2.move()  # Move horse2

    # Determine the winner based on which horse crosses the finish line first
    if horse1.crossed_finish_line(600) and horse2.crossed_finish_line(600):
        print("Tie")  # If both horses cross the finish line at the same time, it's a tie
    elif horse1.crossed_finish_line(600):
        print("Knight is the winner!")  # If horse1 crosses the finish line first, it wins
    else:
        print("Wizard is the winner!")  # If horse2 crosses the finish line first, it wins

    # Wait for the user to click before closing the window
    win.getMouse()
    win.close()  # Close the graphical window

if __name__ == "__main__":
    main()  # Start the main function if the script is run directly
