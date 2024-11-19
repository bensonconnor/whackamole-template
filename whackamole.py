import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft=((random.randint(0, 19))*32,(random.randint(0, 15))*32))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if mole_rect.collidepoint(event.pos):  # Check if click is on the mole
                        mole_rect.topleft = ((random.randint(0, 19))*32),(random.randint(0, 15))*32
            screen.fill("light green")
            pygame.draw.line(screen, 0, (32, 0), (32, 512))
            pygame.draw.line(screen, 0, (64, 0), (64, 512))
            pygame.draw.line(screen, 0, (96, 0), (96, 512))
            pygame.draw.line(screen, 0, (128, 0), (128, 512))
            pygame.draw.line(screen, 0, (160, 0), (160, 512))
            pygame.draw.line(screen, 0, (192, 0), (192, 512))
            pygame.draw.line(screen, 0, (224, 0), (224, 512))
            pygame.draw.line(screen, 0, (256, 0), (256, 512))
            pygame.draw.line(screen, 0, (288, 0), (288, 512))
            pygame.draw.line(screen, 0, (320, 0), (320, 512))
            pygame.draw.line(screen, 0, (352, 0), (352, 512))
            pygame.draw.line(screen, 0, (384, 0), (384, 512))
            pygame.draw.line(screen, 0, (416, 0), (416, 512))
            pygame.draw.line(screen, 0, (448, 0), (448, 512))
            pygame.draw.line(screen, 0, (480, 0), (480, 512))
            pygame.draw.line(screen, 0, (512, 0), (512, 512))
            pygame.draw.line(screen, 0, (544, 0), (544, 512))
            pygame.draw.line(screen, 0, (576, 0), (576, 512))
            pygame.draw.line(screen, 0, (608, 0), (608, 512))
            pygame.draw.line(screen, 0, (0, 32), (640, 32))
            pygame.draw.line(screen, 0, (0,64), (640,64))
            pygame.draw.line(screen, 0, (0,96), (640,96))
            pygame.draw.line(screen, 0, (0,128), (640,128))
            pygame.draw.line(screen, 0, (0,160), (640,160))
            pygame.draw.line(screen, 0, (0,192), (640,192))
            pygame.draw.line(screen, 0, (0,224), (640,224))
            pygame.draw.line(screen, 0, (0,256), (640,256))
            pygame.draw.line(screen, 0, (0,288), (640,288))
            pygame.draw.line(screen, 0, (0,320), (640,320))
            pygame.draw.line(screen, 0, (0,352), (640,352))
            pygame.draw.line(screen, 0, (0,384), (640,384))
            pygame.draw.line(screen, 0, (0,416), (640,416))
            pygame.draw.line(screen, 0, (0,448), (640,448))
            pygame.draw.line(screen, 0, (0,480), (640,480))
            pygame.draw.line(screen, 0, (0,512), (640,512))
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
