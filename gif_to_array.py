from PIL import Image

fileName = "[FIILE]"
pathName= "[/PATH/]" + fileName + ".gif"

imageObject = Image.open(pathName)


# Calculate the size of each frame's data array
frame_size = frame_width * frame_height

frames_data = []
# Display individual frames from the loaded animated GIF file
for frame in range(0, imageObject.n_frames):
    imageObject.seek(frame)
    rgb_pixels = list(imageObject.convert("RGB").getdata())
    # print(rgb_pixels)

    frame_data = [((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3) for r, g, b in rgb_pixels]
    frames_data.append(frame_data)

# Save the array to a file named "output_array.txt"
output_filename = fileName + ".h"

with open(output_filename, "w") as output_file:
    output_file.write(f"#define PROGMEM\n\nint {fileName}framesNumber = {len(frames_data)}; int aniWidth = {frame_width}; int aniHeight = {frame_height};\n\n")
    output_file.write(f"const unsigned short {fileName}")
    output_file.write("[][{}] PROGMEM = {{\n".format(frame_size))
    for idx, frame_data in enumerate(frames_data):
        comma = "," if idx < len(frames_data) - 1 else ""
        output_file.write("    {" + ",".join([f"0x{val:04X}" for val in frame_data]) + f"}}{comma}\n")
    output_file.write("};\n")

print(f"Array representation of GIF frames saved to {output_filename}.")
