# Repeating the same process for the newly uploaded image
# Load the newly uploaded image
new_img = Image.open("logo-white.png")

# Calculate padding
new_width, new_height = new_img.size
new_left = new_right = new_width * 0.22
new_top = new_bottom = new_height * 0.22

# Add padding around the image
final_new_width = new_width + new_left + new_right
final_new_height = new_height + new_top + new_bottom
result_new = Image.new(new_img.mode, (int(final_new_width), int(final_new_height)), "black")
result_new.paste(new_img, (int(new_left), int(new_top)))

# Save the modified image
output_new_path = "logo_with_new_padding.png"
result_new.save(output_new_path)

output_new_path
