import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Menu")

# Load background image
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (width, height))

# Load images
image1 = pygame.image.load("images.jpg")
image2 = pygame.image.load("images.jpg")
image3 = pygame.image.load("images.jpg")

# Load settings icon
settings_icon = pygame.image.load("setting.jpg")
settings_icon = pygame.transform.scale(settings_icon, (30, 30))  # Adjust the size as needed

# Load quit button icon
quit_icon = pygame.image.load("exit.png")
quit_icon = pygame.transform.scale(quit_icon, (50, 50))  # Adjust the size as needed

# Font settings
font = pygame.font.Font(None, 36)

def draw_menu():
    # Display background image
    screen.blit(background_image, (0, 0))

    # Display images as buttons
    button1_rect = pygame.Rect(100, 100, image1.get_width(), image1.get_height())
    button2_rect = pygame.Rect(300, 100, image2.get_width(), image2.get_height())
    button3_rect = pygame.Rect(500, 100, image3.get_width(), image3.get_height())

    pygame.draw.rect(screen, (150, 150, 150), button1_rect)
    pygame.draw.rect(screen, (150, 150, 150), button2_rect)
    pygame.draw.rect(screen, (150, 150, 150), button3_rect)

    screen.blit(image1, button1_rect.topleft)
    screen.blit(image2, button2_rect.topleft)
    screen.blit(image3, button3_rect.topleft)

    # Draw settings button in the top right corner
    settings_rect = pygame.Rect(width - 80, 10, 30, 30)
    pygame.draw.rect(screen, (150, 150, 150), settings_rect)
    screen.blit(settings_icon, settings_rect.topleft)

    # Draw quit button in the top right corner
    quit_rect = pygame.Rect(width - 50, 10, 30, 30)
    pygame.draw.rect(screen, (150, 150, 150), quit_rect)
    screen.blit(quit_icon, quit_rect.topleft)

    pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Check if the settings button is clicked
            if settings_rect.collidepoint(x, y):
                print("Settings button clicked!")
            # Check if the quit button is clicked
            elif quit_rect.collidepoint(x, y):
                running = False
            # Check if any image button is clicked
            elif button1_rect.collidepoint(x, y):
                print("Button 1 clicked!")
            elif button2_rect.collidepoint(x, y):
                print("Button 2 clicked!")
            elif button3_rect.collidepoint(x, y):
                print("Button 3 clicked!")

    draw_menu()

# Quit Pygame
pygame.quit()
sys.exit()
