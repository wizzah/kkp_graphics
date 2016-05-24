import pyglet
from random import randint
import os

batch = pyglet.graphics.Batch()
test = pyglet.image.load_animation('fatcate.gif')
other_test = pyglet.image.load_animation('../splash/1.gif')

pyglet.resource.path = ['../splash']

window = pyglet.window.Window(fullscreen=True)
total_width = window.width
total_height = window.height

fps_display = pyglet.clock.ClockDisplay()

def gen_coords(coord, img):
	if coord == "x":
		print img.frames[0].image.width
		return randint(0, (total_width - img.frames[0].image.width))
		# return randint(0, total_width)
	else:
		print (total_height - img.frames[0].image.height)
		return randint(0, (total_height - img.frames[0].image.height))
gen_coords("x", test)

#if random is too slow, make a list of set points inside the bounding box


#randomly generate coordinates in the screen boundary
sprites = [
	pyglet.sprite.Sprite(test, batch=batch, x=gen_coords("x", test), y=gen_coords("y", test)),
	pyglet.sprite.Sprite(other_test, batch=batch, x=gen_coords("x", other_test), y=gen_coords("y", other_test)),
	pyglet.sprite.Sprite(test, batch=batch, x=gen_coords("x", test), y=gen_coords("y", test)),
	pyglet.sprite.Sprite(other_test, batch=batch, x=gen_coords("x", other_test), y=gen_coords("y", other_test))
]

# height = int(test.get_max_height())
# width = int(test.get_max_width())
# print type(height), width

# window = pyglet.window.Window(height=400, width=400)
window.set_caption("hi")
# set bg color
# pyglet.clock.schedule_interval(self.update, 1.0/FPS)
pyglet.gl.glClearColor(0,0,0,0)

@window.event
def on_draw():
    # window.clear()
    # window.draw()
    # sprites.draw()
    window.clear()
    fps_display.draw()
    batch.draw()


pyglet.app.run()