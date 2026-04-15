import pygame
import datetime
import math


class MickeyClock:
    def __init__(self, center_x, center_y, background_path):
        self.center_x = center_x
        self.center_y = center_y

        self.background = pygame.image.load(background_path).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        self.minute_hand_length = 90
        self.second_hand_length = 110

    def get_time(self):
        now = datetime.datetime.now()
        return now.minute, now.second

    def get_hand_end(self, angle_deg, length):
        angle_rad = math.radians(angle_deg)

        end_x = self.center_x + length * math.sin(angle_rad)
        end_y = self.center_y - length * math.cos(angle_rad)

        return end_x, end_y

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        minutes, seconds = self.get_time()

        minute_angle = minutes * 6
        second_angle = seconds * 6

        minute_end = self.get_hand_end(minute_angle, self.minute_hand_length)
        second_end = self.get_hand_end(second_angle, self.second_hand_length)

        minute_start = (self.center_x - 5, self.center_y - 5)
        second_start = (self.center_x - 5, self.center_y - 5)

        pygame.draw.line(screen, (0, 0, 0), minute_start, minute_end, 6)
        pygame.draw.line(screen, (255, 0, 0), second_start, second_end, 4)

        pygame.draw.circle(screen, (0, 0, 0), (self.center_x, self.center_y), 5)