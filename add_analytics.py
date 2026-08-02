import os

frontend_dir = '/Users/mohitshukla/new sanik public school website/frontend'

analytics_script = """
    <!-- Vercel Analytics & Speed Insights -->
    <script>
      window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
      window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/insights/script.js"></script>
    <script defer src="/_vercel/speed-insights/script.js"></script>
"""

for root, _, files in os.walk(frontend_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it's already added to avoid duplicates
            if 'window.va =' not in content:
                content = content.replace('</head>', analytics_script + '</head>')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Analytics scripts added successfully!")
