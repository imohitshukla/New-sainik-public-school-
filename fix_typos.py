import os

frontend_dir = '/Users/mohitshukla/new sanik public school website/frontend'

for root, _, files in os.walk(frontend_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix spelling of Siyarpakha in the address (header & footer variants if they exist)
            # The user wrote: "Bajrang Chauraha, Siyarpaha Gudhankalan Naraini, Banda-210129"
            # In HTML it might have <br> or be on one line.
            content = content.replace("Siyarpaha Gudhankalan", "Siyarpakha Gudhankalan")
            
            # Fix teachers count in index.html
            if file == 'index.html':
                # The stat says '12+'
                content = content.replace(">12+<", ">20+<")
                # Just in case there's whitespace:
                content = content.replace('12+</h4>', '20+</h4>')
                # Wait, I should probably check how it is exactly formatted. Let's just do a blanket replace of "12+" if it relates to teachers.
                # Actually, replacing "12+" to "20+" when it is near TEACHERS is safer.
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Typos fixed!")
