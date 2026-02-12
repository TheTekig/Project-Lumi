import pygame
from PIL import Image
import os
class EmotionDisplayService:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1152, 648))
        pygame.display.set_caption("Lumi Emotion Display")
        
        self.clock = pygame.time.Clock()

        self.frames = []
        self.durations = []
        self.current_frame = 0
        self.frame_timer = 0

        self.running = True

    def load_gif(self, gif_path):
        self.frames.clear()
        self.durations.clear()
        self.current_frame = 0
        self.frame_timer = 0

        gif = Image.open(gif_path)

        try:
            while True:
                frame = gif.copy().convert("RGBA")
                duration = gif.info.get("duration", 100)  # Duração padrão de 100ms

                mode = frame.mode
                size = frame.size
                data = frame.tobytes()

                pygame_image = pygame.image.fromstring(data, size, mode)
                self.frames.append(pygame_image)
                self.durations.append(duration)

                gif.seek(gif.tell() + 1)
        except EOFError:
            pass
    
    def set_emotion(self, emotion: str):
        path = f"./src/lumi_robot/Display/emotions/{emotion}.gif"
        if os.path.exists(path):
            self.load_gif(path)
        else:
            print(f"Emotion GIF not found: {path}")

    def run(self):
        while self.running:
            dt = self.clock.tick(30)  # Limita a 30 FPS 
            self.frame_timer += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            if self.frames:
                if self.frame_timer >= self.durations[self.current_frame]:
                    self.frame_timer = 0
                    self.current_frame = (self.current_frame + 1) % len(self.frames)

                    frame = self.frames[self.current_frame]
                    self.screen.blit(frame, (0, 0))
                
            pygame.display.flip()  # Atualiza a tela
        pygame.quit()