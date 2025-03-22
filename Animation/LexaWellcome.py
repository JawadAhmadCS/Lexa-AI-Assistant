import pygame
import time

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600

pygame.display.set_caption("Lexa Entry Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (150, 50, 255)

# Fonts
font_large = pygame.font.Font(None, 72)
font_small = pygame.font.Font(None, 36)

# Messages
main_message = "Welcome to Lexa"
sub_message = "Your Intelligent AI Assistant"

# Animation variables
def start_welcome_animation():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    """Starts the welcome animation."""
    text_alpha = 0  # Transparency for fade-in effect
    circle_radius = 0  # Expanding circle effect
    max_circle_radius = WIDTH // 1
    animation_duration = 3  # Duration of animation in seconds

    def draw_expanding_circle_with_text():
        """Draws the expanding circle with text appearing in the middle."""
        nonlocal circle_radius, text_alpha

        # Draw the expanding circle
        pygame.draw.circle(screen, PURPLE, (WIDTH // 2, HEIGHT // 2), circle_radius, 5)

        # Draw text inside the circle
        text = font_large.render(main_message, True, WHITE)
        text.set_alpha(text_alpha)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        screen.blit(text, text_rect)

        sub_text = font_small.render(sub_message, True, WHITE)
        sub_text.set_alpha(text_alpha)
        sub_text_rect = sub_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        screen.blit(sub_text, sub_text_rect)

        # Increase circle radius
        if circle_radius < max_circle_radius:
            circle_radius += 10

        # Gradually fade in the text
        if circle_radius > max_circle_radius // 4 and text_alpha < 255:
            text_alpha += 5

    # Main animation loop
    running = True
    start_time = time.time()
    while running:
        elapsed_time = time.time() - start_time  # Track elapsed time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)  # Clear the screen

        # Draw the expanding circle with the text
        draw_expanding_circle_with_text()

        pygame.display.flip()  # Update the screen
        pygame.time.Clock().tick(30)  # Limit frame rate to 30 FPS

        # Exit after the animation duration
        if elapsed_time >= animation_duration:
            running = False

    pygame.quit()


# Call the animation
#start_welcome_animation()
