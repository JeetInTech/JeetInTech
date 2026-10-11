import os

os.makedirs('assets/badges', exist_ok=True)

badges = [
    ('sebastian', 'Sebastian'),
    ('neuroviai', 'Neuroviai'),
    ('genesis-jobapp', 'Genesis: Job Application Agent'),
    ('ai-data-analyst', 'AI Data Analyst Engine'),
    ('virtual-therapist', 'Virtual Therapist'),
    ('genesis-video', 'Genesis: Video Pipeline'),
    ('genesis-jobpulse', 'Genesis: JobPulse'),
    ('streak-guardian', 'Daily Coding Streak Guardian'),
    ('mr-memecredible', 'Mr. Memecredible'),
    ('local-cortex', 'Local Cortex'),
    ('molars-nutrition', 'Molars Nutrition'),
    ('offline-image-gen', 'Offline Image Workstation'),
    ('neurovia-careers', 'Neurovia Careers'),
    ('crafting-brain', 'Crafting Brain'),
    ('genesis-central-brain', 'Genesis: Central Brain'),
    ('whatsapp-agent', 'WhatsApp Automation'),
    ('linkedin-outreach', 'LinkedIn Outreach'),
    ('linkedin-publisher', 'LinkedIn Publisher'),
    ('cold-mails', 'Cold Mails Agent'),
]

for slug, title in badges:
    char_len = len(title)
    # Give comfortable width for Segoe UI 12px bold
    width = int(char_len * 8.2 + 38)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="26" viewBox="0 0 {width} 26" fill="none">
  <rect x="0.5" y="0.5" width="{width-1}" height="25" rx="5" fill="#0d1117" stroke="#00FF41" stroke-width="1.2"/>
  <circle cx="13" cy="13" r="3.5" fill="#00FF41"/>
  <text x="24" y="17" fill="#00FF41" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="12" font-weight="700" letter-spacing="0.3">{title}</text>
</svg>'''
    with open(f'assets/badges/{slug}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

print(f"Generated {len(badges)} badges in assets/badges/")
