from PIL import Image

# Open your sprite image
sprite = Image.open("Assets/Characters/Fist_Guy/fistguyRaw.png")  # Replace with your file path

# Upscale using nearest-neighbor interpolation
upscaled_sprite = sprite.resize((200, 300), Image.NEAREST)

# Save the upscaled image
upscaled_sprite.save("sprite_upscaled.png")
