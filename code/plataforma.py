import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, comprimento: int, tile_path: str):
        super().__init__()

        # Carregar o tile
        tile_img = pygame.image.load(tile_path).convert_alpha()
        largura_tile = tile_img.get_width()
        altura_tile = tile_img.get_height()

        # Superfície do tamanho da plataforma
        self.image = pygame.Surface((comprimento * largura_tile, altura_tile), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))

        # Desenhar os tiles lado a lado
        for i in range(comprimento):
            self.image.blit(tile_img, (i * largura_tile, 0))