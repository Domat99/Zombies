import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Get the screen dimensions
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Set up the screen in fullscreen mode
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Menu App")

# Create fonts
font = pygame.font.Font(None, 36)

# Load images
image1 = pygame.image.load("Image1.png")  # Replace with your image file
image2 = pygame.image.load("Image2.png")  # Replace with your image file
image3 = pygame.image.load("Image3.png")  # Replace with your image file

# Resize images
image1 = pygame.transform.scale(image1, (100, 100))
image2 = pygame.transform.scale(image2, (100, 100))
image3 = pygame.transform.scale(image3, (100, 100))

# Calculate the position to center images vertically
images_vertical_position = screen_height // 2 - (3 * 100 + 2 * 10) // 2

# Define the main menu
def main_menu():
    screen.fill(RED)

    # Draw images in the middle on top of each other
    screen.blit(image1, (screen_width // 2 - 50, images_vertical_position))
    screen.blit(image2, (screen_width // 2 - 50, images_vertical_position + 110))
    screen.blit(image3, (screen_width // 2 - 50, images_vertical_position + 220))

    # Draw buttons on the top right (Open Submenu) and top left (Exit Game)
    pygame.draw.rect(screen, BLUE, (screen_width - 150, 20, 100, 50))
    button_text = font.render("Open Submenu", True, WHITE)
    screen.blit(button_text, (screen_width - 140, 30))

    pygame.draw.rect(screen, BLUE, (20, 20, 100, 50))
    exit_button_text = font.render("Exit Game", True, WHITE)
    screen.blit(exit_button_text, (30, 30))

def white_submenu():
    screen.fill(WHITE)

    # Draw back button
    pygame.draw.rect(screen, RED, (20, 20, 100, 50))
    back_button_text = font.render("Back", True, WHITE)
    screen.blit(back_button_text, (30, 30))

def yellow_submenu():
    screen.fill(YELLOW)

    # Draw back button
    pygame.draw.rect(screen, RED, (20, 20, 100, 50))
    back_button_text = font.render("Back", True, WHITE)
    screen.blit(back_button_text, (30, 30))

def purple_submenu():
    screen.fill(PURPLE)

    # Draw back button
    pygame.draw.rect(screen, RED, (20, 20, 100, 50))
    back_button_text = font.render("Back", True, WHITE)
    screen.blit(back_button_text, (30, 30))

# Initial state
current_menu = main_menu

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if current_menu == main_menu:
                if screen_width // 2 - 50 < x < screen_width // 2 + 50 and \
                   images_vertical_position < y < images_vertical_position + 100:
                    current_menu = white_submenu
                elif screen_width // 2 - 50 < x < screen_width // 2 + 50 and \
                     images_vertical_position + 110 < y < images_vertical_position + 210:
                    current_menu = yellow_submenu
                elif screen_width // 2 - 50 < x < screen_width // 2 + 50 and \
                     images_vertical_position + 220 < y < images_vertical_position + 320:
                    current_menu = purple_submenu
                elif screen_width - 150 < x < screen_width - 50 and 20 < y < 70:
                    current_menu = submenu
                elif 20 < x < 120 and 20 < y < 70:
                    pygame.quit()
                    sys.exit()
            elif current_menu in [white_submenu, yellow_submenu, purple_submenu]:
                if 20 < x < 120 and 20 < y < 70:
                    current_menu = main_menu

    # Render the current menu
    current_menu()

    # Update the display
    pygame.display.flip()
