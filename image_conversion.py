from PIL import Image

# Open your sprite image
sprite = Image.open("Assets/Characters/GunGuy/gunGuy.png")  # Replace with your file path

# Upscale using nearest-neighbor interpolation
upscaled_sprite = sprite.resize((200, 300), Image.NEAREST)

# Save the upscaled image
upscaled_sprite.save("Assets/Characters/GunGuy/fdasfdsafads.png")
