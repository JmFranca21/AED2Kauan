import pygame
import sys

# Inicializa o Pygame
pygame.init()

#cores do jogo
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Configuração da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Controle de Fluxo")
font = pygame.font.Font(None, 36)

# Define a classe do Botão
class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font # Fonte do texto

    def draw_button(self, screen):
        # Desenha o retângulo do botão
        pygame.draw.rect(screen, self.color, self.rect)
        
        # Renderiza e desenha o texto centralizado no botão
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_clicked(self, mouse_pos):
        # Verifica se o botão foi clicado
        return self.rect.collidepoint(mouse_pos)

#para inserir textos na tela
class Text:
    def __init__(self, text, x, y, font_size=36, color = BLACK):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font_size = font_size
        self.font = font
        self.text_surface = self.font.render(self.text, True, self.color)
    
    def set_text(self, new_text):
        """Altera o texto exibido."""
        self.text = new_text
        self.update_surface()

    def set_color(self, new_color):
        """Altera a cor do texto."""
        self.color = new_color
        self.update_surface()

    def set_position(self, x, y):
        """Define uma nova posição para o texto."""
        self.x = x
        self.y = y

    def update_surface(self):
        """Atualiza a superfície de texto após mudanças."""
        self.text_surface = self.font.render(self.text, True, self.color)

    def write(self, screen):
        """Desenha o texto na tela."""
        screen.blit(self.text_surface, (self.x, self.y))

class Array:
    def __init__(self):
        self.array = []
    
    def input_array(self, screen):
        pass
        
# Função da tela inicial (menu)
def menu_screen(screen):
    #define botões do menu
    running = True
    selection_button = Button(300, 100, 200, 50, "Selection Sort", BLUE, WHITE)
    heap_button = Button(300, 200, 200, 50, "Heap Sort", BLUE, WHITE)
    radix_button = Button(300, 300, 200, 50, "Radix Sort", BLUE, WHITE)
    exit_button = Button(300, 400, 200, 50, "Exit", BLACK, WHITE)
    next_screen = None

    #enquanto o menu estiver rodando
    while running:
        for event in pygame.event.get():
            #se usuário dá quit, saia
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #se clicou em start, vá para a tela game_screen
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if selection_button.is_clicked(event.pos):  #se o botão clicado foi Selection Sort, vá para essa tela
                    next_screen = "selection_screen"
                    running = False #sai do loop running
                    
                elif heap_button.is_clicked(event.pos):     #se o botão clicado foi Heap Sort, vá para essa tela
                    next_screen = "heap_screen"
                    running = False #sai do loop running
                
                elif radix_button.is_clicked(event.pos):    #se o botão clicado foi Radix Sort, vá para essa tela
                    next_screen = "radix_screen"
                    running = False #sai do loop running
                    
                    #se clicou em Exit, dá quit no jogo
                elif exit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()

        #preenche a tela de menu com os elementos
        screen.fill(WHITE)
        selection_button.draw_button(screen)
        heap_button.draw_button(screen)
        radix_button.draw_button(screen)
        exit_button.draw_button(screen)
        pygame.display.flip()
        
    #vai para outra tela após sair do loop running
    return next_screen

# Função da tela do Selection Sort
def selection_screen(screen):
    running = True
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    next_screen = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    next_screen = "menu_screen"
                    running = False
                    
        #desenha os elementos na tela de game
        screen.fill(WHITE)
        back_button.draw_button(screen)
        pygame.display.flip()

    return next_screen

# Função da tela do Radix Sort
def radix_screen(screen):
    running = True
    text_over = Text("esse é o radix sort",300, 100)
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    next_screen = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    next_screen = "menu_screen"
                    running = False
                    
        #desenha os elementos na tela de game
        screen.fill(WHITE)
        back_button.draw_button(screen)
        text_over.write(screen)
        pygame.display.flip()

    return next_screen

# Função da tela do Heap Sort
def heap_screen(screen):
    running = True
    back_button = Button(300, 500, 200, 50, "Back to Menu", BLACK, WHITE)
    next_screen = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    next_screen = "menu_screen"
                    running = False
                    
        #desenha os elementos na tela de game
        screen.fill(WHITE)
        back_button.draw_button(screen)
        pygame.display.flip()

    return next_screen

# Função principal para controlar o fluxo
def main_controller():
    screen_mapping = {
        "menu_screen": menu_screen,           #tela de menu (inicial)
        "selection_screen": selection_screen, #tela de Selection Sort
        "heap_screen": heap_screen,           #tela de Heap Sort
        "radix_screen": radix_screen         #tela de Radix Sort
    }
    current_screen = "menu_screen" #tela atual

    #essa função permite passar para a proxima tela, pegando screen (global) para desenhar a tela
    while True:
        next_screen = screen_mapping[current_screen](screen)
        if next_screen:
            current_screen = next_screen

# Executa o jogo
if __name__ == "__main__":
    main_controller()