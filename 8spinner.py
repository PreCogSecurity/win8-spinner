from PIL import Image, ImageDraw, ImageSequence
import images2gif as i2g
import math

FILENAME = "spinner.gif"
frames = 32 # no of frames
total_duration = 1000 # no of miliseconds
radius = 30 # outer circle radius
no_dots = 8  # must divide into number of frames evenly or weird shit
no_empty = 4 # no of empty positions
dot_radius = 2 # small 
padding = 10

images = []

angles = [math.pi*(1+math.cos(math.pi*float(x)/frames))-math.pi/2 for x in range(frames)]

size = (radius*2+dot_radius*2+padding*2, radius*2+dot_radius*2+padding*2)

x = [-radius*math.cos(t)+size[0]/2 for t in angles]
y = [radius*math.sin(t)+size[1]/2 for t in angles]

indices = []
for j in xrange(no_dots):
    indices.append(int((math.cos(float(j)/no_dots*math.pi) + 1) / 2 * frames)-1)

print indices

for i in xrange(frames):
    img = Image.new("L",size,255)
    draw = ImageDraw.Draw(img);
    for n in xrange(len(indices)):
        if n+no_empty+1 == no_dots:
            break
        j = indices[n]
        bbox = (x[j] - dot_radius, y[j] - dot_radius,
                x[j] + dot_radius, y[j] + dot_radius)
        draw.ellipse(bbox, fill=0)
    images.append(img)
    indices = [(z + 1) % frames for z in indices]

i2g.writeGif(FILENAME, images, duration=total_duration/frames/1000.0)
