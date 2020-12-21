import pygame
from random import randint

pygame.init()

display = pygame.display.set_mode((800, 800), 0)

black = (0, 0, 0)
raio = 10
div_vel = 10


class Point:

    def __init__(self, cor, x, y, vel, vel_x, vel_y):
        self.cor = cor
        self.x = x
        self.y = y
        self.vel = vel
        self.vel_x = vel_x
        self.vel_y = vel_y


def create_point(num: int):
    objects = []

    for i in range(num):
        r = randint(10, 255)
        g = randint(10, 255)
        b = randint(10, 255)
        x = randint(10, 790)
        y = randint(10, 790)
        vel_x = randint(-9, 9) / div_vel
        vel_y = randint(-9, 9) / div_vel

        objects.append(Point((r, g, b), x, y, vel_x, vel_y, 0))

    return objects


points = create_point(100)

while True:
    for point in points:
        point.x += point.vel_x
        point.y += point.vel_y

        n = randint(0, 15000)

        if n >= 14998:
            point.vel_x = randint(-9, 9) / div_vel
            point.vel_x = randint(-9, 9) / div_vel
            point.vel_y = randint(-9, 9) / div_vel
            point.vel_y = randint(-9, 9) / div_vel

        if point.x + raio > 800:
            point.vel_x = -point.vel
        if point.x - raio < 0:
            point.vel_x = point.vel
        if point.y + raio > 800:
            point.vel_y = -point.vel
        if point.y - raio < 0:
            point.vel_y = point.vel

    # Pintar
    display.fill(black)
    for p in points:
        pygame.draw.circle(display, p.cor, (int(p.x), int(p.y)), raio, 0)
    pygame.display.update()

    # eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
