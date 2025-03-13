from graphics import GraphWin, Image, Line, Point  # graphics 모듈에서 필요한 요소 가져오기
from Dice import Dice
import time

class Horse:
    def __init__(self, speed, y_pos, image_path, window):
        self.x_pos = 50  # 출발 지점 x 좌표
        self.y_pos = y_pos
        self.window = window
        self.dice = Dice(speed)
        
        try:
            self.image = Image(Point(self.x_pos, self.y_pos), image_path)
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
    # 그래픽 창 설정
    win = GraphWin("Horse Race", 700, 350)
    win.setBackground("white")
    
    # 말 이미지 로드
    horse1_image = "Knight.gif"
    horse2_image = "Wizard.gif"
    
    # Horse 객체 생성
    horse1 = Horse(10, 100, horse1_image, win)
    horse2 = Horse(12, 200, horse2_image, win)
    
    # 경주마 그리기
    horse1.draw()
    horse2.draw()
    
    # 결승선 그리기
    finish_line = Line(Point(600, 50), Point(600, 300))
    finish_line.setWidth(3)
    finish_line.setFill("red")
    finish_line.draw(win)
    
    # 시작 대기 (사용자 클릭 대기)
    win.getMouse()
    
    # 경주 시작
    while not horse1.crossed_finish_line(600) and not horse2.crossed_finish_line(600):
        time.sleep(0.5)
        horse1.move()
        horse2.move()
        
    # 우승자 판별
    if horse1.crossed_finish_line(600) and horse2.crossed_finish_line(600):
        print("Tie")
    elif horse1.crossed_finish_line(600):
        print("Knight is the winner!")
    else:
        print("Wizard is the winner!")
    
    # 종료 대기
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
