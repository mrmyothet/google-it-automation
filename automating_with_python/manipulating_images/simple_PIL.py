from PIL import Image

img = Image.open("example.jpg")
new_img = img.resize((640, 480))
new_img.save("example_resized.jpg")

new_img = img.rotate(90)
new_img.save("example_rotated.jpg")

new_img = img.rotate(180).resize((640, 480)).save("flipped_and_resized.jpg")
