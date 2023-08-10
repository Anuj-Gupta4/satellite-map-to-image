# satellite-map-to-image
This app can generate map images like that in google maps using the images taken from the satellites. It utilizes Generative adversial network model to translate the images from satellite map to google map images.

# Run project
- upload model named `model_010960.h5` on root of repository
- run on terminal: `pip install -r requirements.txt`
- run on terminal: `python manage.py makemigrations`
- run on terminal: `python manage.py migrate`
- run on terminal: `python manage.py runserver`
- All Done