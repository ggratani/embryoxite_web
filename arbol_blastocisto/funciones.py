from PIL import ImageDraw, ImageFont

def count_cells(data, imagen):
    fontsize = 20
    font = ImageFont.truetype("arial.ttf", fontsize)
    cont = 0
    predictions = data["predictions"]
    size = imagen.size
    for pred in predictions:
        if pred["probability"] > 0.85:
            if pred["tagName"] == "cell":
                x = pred["boundingBox"]["left"] * size[0]
                y = pred["boundingBox"]["top"] * size[1]
                w = pred["boundingBox"]["width"] * size[0]
                h = pred["boundingBox"]["height"] * size[1]
                draw = ImageDraw.Draw(imagen)
                draw.rectangle((x, y, (x+w), (y+h)), outline=(0, 255, 0),width=3)
                cont = cont +1
    draw.text([20,20], "{} celulas".format(cont), font = font, fill="#FFF")
    return cont