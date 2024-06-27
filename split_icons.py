from PIL import Image
import os

# Ensure the path to the combined image is correct
combined_image_path = 'combined_icons.png'

# Load the combined image
img = Image.open(combined_image_path)
img_width, img_height = img.size

# Number of icons in the combined image
num_icons = 5  # Adjust this if the number of icons is different

# Calculate icon size dynamically
icon_width = img_width // num_icons
icon_height = img_height  # Assuming all icons are in a single row

# Create the icons directory if it doesn't exist
if not os.path.exists('icons'):
    os.makedirs('icons')

# Define coordinates for each icon dynamically
icons = {
    'btrfs': (0, 0, icon_width, icon_height),
    'zfs': (icon_width, 0, icon_width * 2, icon_height),
    'ext4': (icon_width * 2, 0, icon_width * 3, icon_height),
    'xfs': (icon_width * 3, 0, icon_width * 4, icon_height),
    'f2fs': (icon_width * 4, 0, icon_width * 5, icon_height)
}

# Save each icon as a separate file
for name, coords in icons.items():
    icon = img.crop(coords)
    icon.save(f'icons/{name}.png')
