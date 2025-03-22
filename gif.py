from PIL import Image, ImageSequence

# Load the base character image
character_path = "/mnt/data/A_cute,_animated_boy_character_in_a_formal_suit,_p.png"
character_img = Image.open(character_path).convert("RGBA")

# Create animation frames
frames = []
num_frames = 30  # Total frames for smooth animation

for i in range(num_frames):
    frame = character_img.copy()

    # Simulate blinking at certain frames
    if i % 15 == 0:  # Blink every 15 frames
        blink_layer = Image.new("RGBA", frame.size, (0, 0, 0, 50))  # Transparent black overlay
        frame.paste(blink_layer, (0, 0), blink_layer)

    # Simulate hand movement (subtle up-down motion)
    y_offset = int(5 * np.sin(2 * np.pi * i / num_frames))  # Smooth waving motion
    new_frame = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    new_frame.paste(frame, (0, y_offset), frame)

    frames.append(new_frame)

# Save as a GIF
gif_path = "/mnt/data/animated_presentation_character.gif"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=100, loop=0)

gif_path
