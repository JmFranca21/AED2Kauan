import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configuração da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Controle de Fluxo")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)

# Fonte personalizada
font = pygame.font.Font("minha_fonte.ttf", 30)

# Botão
class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Entrada de texto
class TextInput:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 80)
        self.text = ""
        self.active = False
        self.font_size = 36  # Tamanho inicial da fonte

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                return self.text
            else:
                self.text += event.unicode
        return None

    def draw(self, screen):
        # Calcula o tamanho da fonte baseado no comprimento do texto
        max_font_size = 36  # Tamanho máximo da fonte
        min_font_size = 20  # Tamanho mínimo da fonte

        text_length = len(self.text)
        # Ajusta o tamanho da fonte baseado no comprimento do texto
        if text_length == 0:
            self.font_size = max_font_size
        else:
            # Calcula o novo tamanho da fonte
            self.font_size = max(min_font_size, max_font_size - (text_length * 2))

        # Define a fonte com o novo tamanho
        font = pygame.font.Font(None, self.font_size)
        
        # Desenha o campo de texto
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        
        # Centraliza o texto dentro do campo de entrada
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
        pygame.draw.rect(screen, BLUE if self.active else BLACK, self.rect, 2)

class TextInput:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 80)
        self.text = ""
        self.active = False
        self.font_size = 36  # Tamanho inicial da fonte

        # Carrega a fonte customizada (minha-fonte.ttf)
        self.font_path = "minha_fonte.ttf"  # Caminho da fonte customizada
        self.font = pygame.font.Font(self.font_path, self.font_size)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                return self.text
            else:
                self.text += event.unicode
        return None

    def draw(self, screen):
        # Calcula o tamanho da fonte baseado no comprimento do texto
        max_font_size = 36  # Tamanho máximo da fonte
        min_font_size = 18  # Tamanho mínimo da fonte

        text_length = len(self.text)
        # Ajusta o tamanho da fonte baseado no comprimento do texto
        if text_length == 0:
            self.font_size = max_font_size
        else:
            # Calcula o novo tamanho da fonte
            self.font_size = max(min_font_size, max_font_size - (text_length * 2))

        # Atualiza a fonte com o novo tamanho
        self.font = pygame.font.Font(self.font_path, self.font_size)

        # Desenha o campo de texto
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)

        # Centraliza o texto dentro do campo de entrada
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, BLUE if self.active else BLACK, self.rect, 2)

class ArrayInput:
    def __init__(self):
        self.numbers = []
        self.text_input = TextInput(200, 250)

    def add_number(self, number):
        if number.isdigit():
            self.numbers.append(int(number))

    def display_numbers(self, screen):
        square_size = 80  # Tamanho do quadrado
        padding = 20      # Espaço entre os quadrados
        x_position = 50   # Posição inicial no eixo X

        for num in self.numbers:
            # Desenha o quadrado
            pygame.draw.rect(screen, BLUE, (x_position, 350, square_size, square_size))

            # Renderiza o número com a fonte fixa
            number_text = font.render(str(num), True, WHITE)

            # Centraliza o texto dentro do quadrado
            text_rect = number_text.get_rect(center=(x_position + square_size // 2, 350 + square_size // 2))
            screen.blit(number_text, text_rect)

            # Move para o próximo quadrado
            x_position += square_size + padding

    def handle_events(self, event):
        number = self.text_input.handle_event(event)
        if number is not None:
            self.add_number(number)
            self.text_input.text = ""




# Telas específicas
def selection_screen(screen):
    running = True
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    array_input = ArrayInput()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.is_clicked(event.pos):
                return "menu_screen"
            array_input.handle_events(event)

        screen.fill(WHITE)
        back_button.draw_button(screen)
        array_input.text_input.draw(screen)
        array_input.display_numbers(screen)
        pygame.display.flip()

def heap_screen(screen):
    running = True
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    array_input = ArrayInput()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.is_clicked(event.pos):
                return "menu_screen"
            array_input.handle_events(event)

        screen.fill(WHITE)
        back_button.draw_button(screen)
        array_input.text_input.draw(screen)
        array_input.display_numbers(screen)
        pygame.display.flip()

def radix_screen(screen):
    running = True
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    array_input = ArrayInput()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.is_clicked(event.pos):
                return "menu_screen"
            array_input.handle_events(event)

        screen.fill(WHITE)
        back_button.draw_button(screen)
        array_input.text_input.draw(screen)
        array_input.display_numbers(screen)
        pygame.display.flip()

# Menu principal
def menu_screen(screen):
    running = True
    selection_button = Button(300, 100, 200, 50, "Selection Sort", BLUE, WHITE)
    heap_button = Button(300, 200, 200, 50, "Heap Sort", BLUE, WHITE)
    radix_button = Button(300, 300, 200, 50, "Radix Sort", BLUE, WHITE)
    exit_button = Button(300, 400, 200, 50, "Exit", BLACK, WHITE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if selection_button.is_clicked(event.pos):
                    return "selection_screen"
                elif heap_button.is_clicked(event.pos):
                    return "heap_screen"
                elif radix_button.is_clicked(event.pos):
                    return "radix_screen"
                elif exit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        selection_button.draw_button(screen)
        heap_button.draw_button(screen)
        radix_button.draw_button(screen)
        exit_button.draw_button(screen)
        pygame.display.flip()

# Controlador principal
def main_controller():
    screens = {
        "menu_screen": menu_screen,
        "selection_screen": selection_screen,
        "heap_screen": heap_screen,
        "radix_screen": radix_screen,
    }
    current_screen = "menu_screen"
    while True:
        next_screen = screens[current_screen](screen)
        if next_screen:
            current_screen = next_screen

# Executa o programa
if __name__ == "__main__":
    main_controller()
