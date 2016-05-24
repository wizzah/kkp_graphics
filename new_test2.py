import pyglet
from random import randint
import os

batch = pyglet.graphics.Batch()
test = pyglet.image.load_animation('fatcate.gif')

pyglet.resource.path = ['../splash']

window = pyglet.window.Window(fullscreen=True)
total_width = window.width
total_height = window.height

fps_display = pyglet.clock.ClockDisplay()

#if random is too slow, make a list of set points inside the bounding box

#randomly generate coordinates in the screen boundary
sprites = [pyglet.sprite.Sprite(test, batch=batch, x=randint(0, total_width), y=randint(0, total_height)),
           pyglet.sprite.Sprite(pyglet.image.load_animation('../splash/1.gif'), batch=batch, x=randint(0, total_width), y=randint(0, total_height))]

# height = int(test.get_max_height())
# width = int(test.get_max_width())
# print type(height), width

# window = pyglet.window.Window(height=400, width=400)
window.set_caption("hi")
# set bg color
# pyglet.clock.schedule_interval(self.update, 1.0/FPS)

@window.event
def on_draw():
    # window.clear()
    # window.draw()
    # sprites.draw()
    pyglet.gl.glClearColor(0,0,0,0)
    window.clear()
    fps_display.draw()
    batch.draw()


pyglet.app.run()