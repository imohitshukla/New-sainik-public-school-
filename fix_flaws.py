import os
from bs4 import BeautifulSoup

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace footer Gallery link
    content = content.replace('<li><a href="#">Gallery</a></li>', '<li><a href="index.html#gallery">Gallery</a></li>')
    
    if os.path.basename(filepath) == 'index.html':
        # Remove Facebook link
        content = content.replace('<a href="#">Facebook</a>', '')
        
        # Change notice board links to divs
        content = content.replace('<a href="#" class="notice-item">', '<div class="notice-item">')
        
        # We also need to change the closing </a> for those notice items. 
        # A simpler way since we know the HTML structure is string replacement for the specific text.
        # But wait, replacing </a> with </div> blindly is dangerous.
        # Let's use BeautifulSoup for index.html
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all a.notice-item
        for a in soup.find_all('a', class_='notice-item'):
            a.name = 'div'
            if 'href' in a.attrs:
                del a['href']
                
        # Fix lightbox img alt
        img = soup.find('img', id='lightbox-img')
        if img and not img.get('alt'):
            img['alt'] = 'Enlarged school image'
            
        content = str(soup)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

frontend_dir = '/Users/mohitshukla/new sanik public school website/frontend'
for f in os.listdir(frontend_dir):
    if f.endswith('.html'):
        process_file(os.path.join(frontend_dir, f))

print("Flaws fixed!")
