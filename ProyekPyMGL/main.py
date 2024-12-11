import pygame as pg
import moderngl as mgl
import sys
from model import *  # Make sure this imports the segitiga class
from camera import kamera

class GraphicsEngine:
    def __init__(self, win_size=(800,600)):
        # Memasukkan modul library Pygame
        pg.init()
        # Set window size (ubah ukuran di bagian fungsi)
        self.WIN_SIZE = win_size
        # Set OpenGL attribute
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # Mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(True)
        # Membuat OpenGL context
        pg.display.set_mode(self.WIN_SIZE, pg.OPENGL | pg.DOUBLEBUF)
        # Mendeteksi dan menggunakan OpenGL context yang tersedia
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw' # Ket. cw = clockwise, fungsi ini digunakan untuk melihat interior program
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # Create an object to help track the time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # Kamera
        self.camera = kamera(self)
        # Scene object
        self.scene = kubus(self)
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()
    
    def render(self):
        # Clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))  # RGB Set value
        # Render scene
        self.scene.render()
        # Swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
    
    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            # self.clock.tick(60)  # Set frame rate per detik
            self.delta_time = self.clock.tick(60)

if __name__ == "__main__":
    app = GraphicsEngine()
    app.run()