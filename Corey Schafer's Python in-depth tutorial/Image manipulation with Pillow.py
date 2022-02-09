from PIL import Image
import os

# image1 = Image.open(r'C:\Users\USER\Pictures\bangla_movie_recommendation_banner.jpg')
# image1.show('BM.png')

size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))


image1 = Image.open(r'C:\Users\USER\Pictures\bangla_movie_recommendation_banner.jpg')
image1.convert(mode='L').save('black_and_white.jpg')
image1.rotate(90).save('rotated.jpg')