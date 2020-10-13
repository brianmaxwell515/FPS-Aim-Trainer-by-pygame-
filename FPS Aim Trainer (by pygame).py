import sys
import time
import random
import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT

# Windows Setting
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
IMAGEWIDTH = 40
IMAGEHEIGHT = 40


# random X, Y setting
def get_random_position(widow_width, window_height, image_width, image_height):
    random_x = random.randint(image_width, widow_width - image_width)
    random_y = random.randint(image_height, window_height - image_height)
    return random_x, random_y


class Target(pygame.sprite.Sprite):  # Target
    def __init__(self, width, height, random_x, random_y, widow_width, window_height):
        super().__init__()
        self.raw_image = pygame.image.load("target_image.png").convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random_x, random_y)
        self.width = width
        self.height = height
        self.widow_width = widow_width
        self.window_height = window_height


def main():
    pygame.init()

    # Create Windows
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("FPS Aim Trainer")
    random_x, random_y = get_random_position(
        WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEWIDTH)

    # Create Target
    target = Target(IMAGEWIDTH, IMAGEHEIGHT, random_x,
                    random_y, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Reload game event
    reload_Target_event = USEREVENT + 1

    # Game Setting
    points = 0
    my_font = pygame.font.SysFont(None, 30)  # ("Fonts", Fonts size)
    my_hit_font = pygame.font.SysFont(None, 40)
    hit_text_surface = None
    main_clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            # Check game running
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Check mouse click
            elif event.type == MOUSEBUTTONDOWN:
                if random_x < pygame.mouse.get_pos()[0] < random_x+IMAGEWIDTH and random_y < pygame.mouse.get_pos()[1] < random_y + IMAGEHEIGHT:
                    target.kill()
                    random_x, random_y = get_random_position(
                        WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEWIDTH)
                    target = Target(IMAGEWIDTH, IMAGEHEIGHT, random_x,
                                    random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
                    # hit_text_surface = my_hit_font.render(
                    #     'Hit!!', True, (0, 0, 0))
                    points += 1

        # UI Rendering
        window_surface.fill(WHITE)
        text_surface = my_font.render(f'Point: {points}', True, (0, 0, 0))
        window_surface.blit(target.image, target.rect)
        window_surface.blit(text_surface, (10, 0))

        # Hit text
        # if hit_text_surface:
        #     window_surface.blit(
        #         hit_text_surface, (random_x - 20, random_y - 20))
        #     hit_text_surface = None

        # Game update
        pygame.display.update()
        main_clock.tick(60)


if __name__ == '__main__':
    main()
