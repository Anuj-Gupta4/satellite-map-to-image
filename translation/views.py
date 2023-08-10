import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
import matplotlib
matplotlib.use('Agg')  # Use Agg backend to avoid GUI-related issues
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.utils import img_to_array
from numpy import expand_dims

def generate_image(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        uploaded_file_url = fs.url(filename)

        # Load the model
        model = load_model('model_010960.h5')

        # Generate the image
        src_image = load_image(os.path.join('media', filename))
        gen_image = model.predict(src_image)
        gen_image = (gen_image + 1) / 2.0

        # Save and display the generated image
        gen_filename = f'gen_{filename}'
        plt.imshow(gen_image[0])
        plt.axis('off')
        gen_filepath = os.path.join('media', gen_filename)
        plt.savefig(gen_filepath, bbox_inches='tight', pad_inches=0)
        plt.close()

        gen_file_url = fs.url(gen_filename)
        print(uploaded_file_url)
        print(gen_file_url)
        return render(request, 'result.html', {'uploaded_file_url': uploaded_file_url, 'gen_file_url': gen_file_url})

    return render(request, 'generate_image.html')

def load_image(filename, size=(256, 256)):
    pixels = Image.open(filename)
    pixels = pixels.resize(size)
    pixels = img_to_array(pixels)
    pixels = (pixels - 127.5) / 127.5
    pixels = expand_dims(pixels, 0)
    return pixels
