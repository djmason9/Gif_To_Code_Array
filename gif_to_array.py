from PIL import Image

imageObject = Image.open("[YOUR_GIF_PATH_HERE]")

# Get the dimensions of the resized frame (320x170)
frame_width, frame_height = [YOUR_WIDTH], [YOUR_HEIGHT]

# Calculate the size of each frame's data array
frame_size = frame_width * frame_height

print(imageObject.is_animated)
print(imageObject.n_frames)
frames_data = []
# Display individual frames from the loaded animated GIF file
for frame in range(0, imageObject.n_frames):
    imageObject.seek(frame)
    rgb_pixels = list(imageObject.convert("RGB").getdata())

    frame_data = [((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3) for r, g, b in rgb_pixels]
    frames_data.append(frame_data)

# Save the array to a file named "output_array.txt"
output_filename = "[YOUR_FILE_NAME_HERE]"

with open(output_filename, "w") as output_file:
    output_file.write(f"#define PROGMEM\n\nint framesNumber = {len(frames_data)}; int aniWidth = {frame_width}; int aniHeight = {frame_height};\n\n")
    output_file.write("const unsigned short logo2[][{}] PROGMEM = {{\n".format(frame_size))
    for idx, frame_data in enumerate(frames_data):
        comma = "," if idx < len(frames_data) - 1 else ""
        output_file.write("    {" + ",".join([f"0x{val:04X}" for val in frame_data]) + f"}}{comma}\n")
    output_file.write("};\n")

print(f"Array representation of GIF frames saved to {output_filename}.")
