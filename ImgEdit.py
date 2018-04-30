from PIL import Image, ImageDraw, ImageFont

def img_txt(Texte):
	img = Image.open('Test.png')

	x1:int = 72
	y1:int = 60
	x2:int = 275
	y2:int = 408

	txt = Image.new('RGB', (x2-x1, y2-y1), color = (255, 255, 255))
	fnt = ImageFont.truetype('/usr/share/fonts/truetype/lohit-devanagari/Lohit-Devanagari.ttf', 21)
	d = ImageDraw.Draw(txt)
	d.text((0,0), Texte ,font=fnt , fill=(0,0,0))

	box = (x1,y1,x2,y2)

	img.paste(txt,(x1,y1))
	return(img)
 