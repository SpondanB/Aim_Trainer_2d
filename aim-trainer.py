import pygame
import math
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INTERVAL = 400 # ms
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

BG_COLOR = (0, 25, 40)
LIVES = 100

TOP_STAT_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("consolas", 24)


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    
    color = "red"
    col2 = "white"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
    
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
            
    def draw(self, window):
        pygame.draw.circle(window, self.col2, (self.x, self.y), self.size)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size*0.8)
        pygame.draw.circle(window, self.col2, (self.x, self.y), self.size*0.6)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size*0.4)
    
    def collide(self, x, y):
        check_distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return check_distance <= self.size
    
        
    
def draw (win, targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)
    
def formated_time(sec):
    milli = math.floor(int(sec * 1000 % 1000) / 100)
    secs = int(round(sec % 60, 1)) 
    mins = int(sec // 60)
    
    return f"{mins:02d}:{secs:02d}:{milli:02d}"

def draw_stats(win, time, target_pressed, miss):
    pygame.draw.rect(win, "orange", (0, 0, WIDTH, TOP_STAT_HEIGHT))
    
    time_label = LABEL_FONT.render(f"Time: {formated_time(time)}", 1, "black")
    
    speed = round(target_pressed / time, 2)
    speed_label = LABEL_FONT.render(f"Speed: {speed} tar/sec", 1, "black")
    
    hits_label = LABEL_FONT.render(f"Hits: {target_pressed}", 1, "black")
    
    lives_label = LABEL_FONT.render(f"Lives: {LIVES - miss}", 1, "black")
    
    win.blit(time_label, (5, 5))
    win.blit(speed_label, (225, 5))
    win.blit(hits_label, (500, 5))
    win.blit(lives_label, (650, 5))

def end_screen(win, time, target_pressed, clicks):
    win.fill(BG_COLOR)
    time_label = LABEL_FONT.render(f"Time: {formated_time(time)}", 1, "WHITE")
    
    speed = round(target_pressed / time, 2)
    speed_label = LABEL_FONT.render(f"Speed: {speed} tar/sec", 1, "WHITE")
    
    hits_label = LABEL_FONT.render(f"Hits: {target_pressed}", 1, "WHITE")
    
    accuracy_label = LABEL_FONT.render(
        f"Accuracy: {round((target_pressed/clicks)*100,2)}%", 1, "WHITE")
    
    win.blit(time_label, (get_mid(time_label), 100))
    win.blit(speed_label, (get_mid(speed_label), 200))
    win.blit(hits_label, (get_mid(hits_label), 300))
    win.blit(accuracy_label, (get_mid(accuracy_label), 400))
    
    pygame.display.update()
    
        

def get_mid(surf):
    return WIDTH/2 - surf.get_width()/2  

def main():
    running = True
    pause = False
    targets = []
    clock = pygame.time.Clock()
    
    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    pygame.time.set_timer(TARGET_EVENT, TARGET_INTERVAL)
    
    while running:
        clock.tick(60)
        
        click = False
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            '''
            if pause:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()
            '''
            if not pause:
                if event.type == TARGET_EVENT:
                    x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                    y = random.randint(TARGET_PADDING + TOP_STAT_HEIGHT, HEIGHT - TARGET_PADDING)
                    t = Target(x, y)
                    targets.append(t)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    clicks += 1
                
        if not pause:
            elapsed_time = time.time() - start_time
            
            for target in targets:
                target.update()
                if target.size <= 0:
                    targets.remove(target)
                    misses += 1
                if click and target.collide(*mouse_pos):
                    targets.remove(target)
                    target_pressed += 1
            
            draw(WIN, targets)
            draw_stats(WIN, elapsed_time, target_pressed, misses)
            pygame.display.update()
        
        if misses >= LIVES:
            end_screen(WIN, elapsed_time, target_pressed, clicks)
            pause = True

    
    pygame.quit()
    

if __name__ == "__main__":
    main()
