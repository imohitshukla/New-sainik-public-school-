import os
import re
from bs4 import BeautifulSoup

def audit_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    filename = os.path.basename(filepath)
    print(f"\n--- Auditing {filename} ---")
    
    # Check Title
    title = soup.find('title')
    if not title or not title.text.strip():
        print("[FLAW] Missing or empty <title> tag.")
        
    # Check Meta Description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if not meta_desc or not meta_desc.get('content', '').strip():
        print("[FLAW] Missing or empty <meta name=\"description\"> tag.")
        
    # Check Links
    ids = set([tag.get('id') for tag in soup.find_all(id=True)])
    links = soup.find_all('a')
    for a in links:
        href = a.get('href', '')
        if href == '#':
            print(f"[FLAW] Empty anchor link: <a href=\"#\">{a.text.strip()}</a>")
        elif href.startswith('#') and len(href) > 1:
            target_id = href[1:]
            if target_id not in ids:
                print(f"[FLAW] Broken internal link: <a href=\"{href}\">{a.text.strip()}</a> (ID '{target_id}' not found in {filename})")
        elif href and not href.startswith('http') and not href.startswith('mailto:') and not href.startswith('tel:'):
            # Internal page link
            target_file = href.split('#')[0]
            if target_file and not os.path.exists(os.path.join(os.path.dirname(filepath), target_file)):
                print(f"[FLAW] Broken page link: <a href=\"{href}\">{a.text.strip()}</a> (File '{target_file}' not found)")

    # Check Images
    imgs = soup.find_all('img')
    for img in imgs:
        src = img.get('src', '')
        if src and not src.startswith('http') and not src.startswith('data:'):
            if not os.path.exists(os.path.join(os.path.dirname(filepath), src)):
                print(f"[FLAW] Broken image link: <img src=\"{src}\"> (File not found)")
        if not img.get('alt'):
            print(f"[FLAW] Missing alt attribute on image: <img src=\"{src}\">")

def main():
    frontend_dir = 'frontend'
    for root, _, files in os.walk(frontend_dir):
        for file in files:
            if file.endswith('.html'):
                audit_html_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
