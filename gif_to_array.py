from PIL import Image

# Open the GIF image
gif_image = Image.open('jmww.gif')

# Convert the image to RGB mode
if gif_image.mode != 'RGB':
    gif_image = gif_image.convert('RGB')


# Get the dimensions of the resized frame (320x170)
frame_width, frame_height = 320, 170

# Calculate the size of each frame's data array
frame_size = frame_width * frame_height

# Initialize the list to store the frames
frames_data = []

# Loop through each frame in the GIF
try:
    while True:
        # Resize the frame to the desired resolution (320x170)
        resized_frame = gif_image.resize((frame_width, frame_height), Image.BICUBIC)  # or Image.BICUBIC

        # Convert the pixels to a list of RGB tuples
        rgb_pixels = resized_frame.getdata()

        # Convert the RGB pixels to a list of unsigned short values
        frame_data = [((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3) for r, g, b in rgb_pixels]
        # Append the frame data to the list
        frames_data.append(frame_data)

        # Move to the next frame
        gif_image.seek(len(frames_data))

except EOFError:
    print(f"Error")
    pass

# Save the array to a file named "output_array.txt"
output_filename = "output_array.txt"

with open(output_filename, "w") as output_file:
    output_file.write(f"#define PROGMEM\n\nint framesNumber = {len(frames_data)}; int aniWidth = {frame_width}; int aniHeight = {frame_height};\n\n")
    output_file.write("const unsigned short logo2[][{}] PROGMEM = {{\n".format(frame_size))
    for idx, frame_data in enumerate(frames_data):
        comma = "," if idx < len(frames_data) - 1 else ""
        output_file.write("    {" + ",".join([f"0x{val:04X}" for val in frame_data]) + f"}}{comma}\n")
    output_file.write("};\n")

print(f"Array representation of GIF frames saved to {output_filename}.")
