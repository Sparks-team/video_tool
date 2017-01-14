from PIL import Image, ImageDraw, ImageFont
import extract

def get_logo_frame(id):
	extract.get_logo(id)
	logo = Image.open(id + '/wittylogo.png')
	MAX_W, MAX_H = 1280, 480
	im = Image.new('RGB', (MAX_W, MAX_H), "white")
	draw = ImageDraw.Draw(im)
	im.paste(logo,(180,80))
	im.show()
	im.save(id + "/logo.png")