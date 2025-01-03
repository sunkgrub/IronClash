from PIL import Image

# Open your sprite image
sprite = Image.open("Assets/Characters/Foot_guy/footGuy.png")  # Replace with your file path

# Upscale using nearest-neighbor interpolation
upscaled_sprite = sprite.resize((200, 300), Image.NEAREST)

# Save the upscaled image
upscaled_sprite.save("Assets/Characters/Foot_guy/sprite_upscaled.png")
