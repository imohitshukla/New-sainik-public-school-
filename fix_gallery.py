import os
from bs4 import BeautifulSoup

filepath = '/Users/mohitshukla/new sanik public school website/frontend/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Remove the globe photo (classroom_new_3.jpeg)
img_to_remove = soup.find('img', src='assets/images/classroom_new_3.jpeg')
if img_to_remove:
    gallery_item = img_to_remove.find_parent('div', class_='gallery-item')
    if gallery_item:
        gallery_item.decompose()

# 2. Change the description of the ear model photo (classroom_new_4.jpeg)
img_to_update = soup.find('img', src='assets/images/classroom_new_4.jpeg')
if img_to_update:
    gallery_item = img_to_update.find_parent('div', class_='gallery-item')
    if gallery_item:
        gallery_item['onclick'] = "openLightbox('assets/images/classroom_new_4.jpeg', 'Ear Lesson')"

# 3. Restore lightbox-caption visibility
lightbox_caption = soup.find('div', id='lightbox-caption')
if lightbox_caption:
    lightbox_caption['style'] = "position: absolute; bottom: 30px; color: white; font-size: 1.2rem; text-align: center; width: 100%;"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Gallery fixed!")
