import pygame
from .config import config


class Canvas:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Canvas, cls).__new__(cls)
        return cls._instance

    def __init__(
        self, width=config.WIDTH, height=config.HEIGHT, caption=config.CAPTION
    ):
        if not hasattr(self, "initialized"):
            # Initialize the pygame
            pygame.init()

            # Set the width and height of the screen [width, height]
            self.width = width
            self.height = height
            self.screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption(caption)

            # Loop until the user clicks the close button.
            self.running = True
            self.clock = pygame.time.Clock()
            self.fps = config.FPS
            self.background_color = config.BACKGROUND_COLOR

            self.initialized = True

    def clear(self):
        self.screen.fill(self.background_color)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                self.running = False

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.fps)
