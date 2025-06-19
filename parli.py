from PIL import Image
import matplotlib.pyplot as plt

print("✅ Running updated skinn.py")  

captions = {
    "ar.jpg": "AR shows. AI knows",
    "peoplegov.jpg": "Old Walls. New Realities",
    "parlibuilding.jpg": "India’s Parliament in View. India’s Policies in AR"
}

def show_image_with_caption(image_filename):
    caption = captions.get(image_filename, "No caption available")
    try:
        img = Image.open(image_filename)
        plt.imshow(img)
        plt.axis("off")
        plt.title("Caption: " + caption)
        plt.show()
    except FileNotFoundError:
        print(f"❌ Error: {image_filename} not found. Please check the filename or path.")

show_image_with_caption("ar.jpg")
show_image_with_caption("peoplegov.jpg")
show_image_with_caption("parlibuilding.jpg")
