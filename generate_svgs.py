import os

projects = [
    {
        "id": "ai-health",
        "title": "AI Health Doctor Assistant",
        "desc": "An intelligent virtual assistant for medical diagnosis and patient care.",
        "tags": ["Python", "TensorFlow", "React", "AWS"],
        "color1": "#38BDF8",
        "color2": "#8B5CF6"
    },
    {
        "id": "ai-matrimony",
        "title": "AI Matrimony Platform",
        "desc": "Next-gen matchmaking leveraging deep learning and semantic matching.",
        "tags": ["Node.js", "MongoDB", "OpenAI", "Next.js"],
        "color1": "#EC4899",
        "color2": "#8B5CF6"
    },
    {
        "id": "portfolio",
        "title": "Animated Portfolio",
        "desc": "A premium, futuristic, and highly interactive developer portfolio.",
        "tags": ["Three.js", "Framer Motion", "React", "GSAP"],
        "color1": "#10B981",
        "color2": "#3B82F6"
    },
    {
        "id": "rizzglam",
        "title": "RizzGlam",
        "desc": "AI-powered fashion and styling recommendation engine.",
        "tags": ["PyTorch", "FastAPI", "Flutter", "GCP"],
        "color1": "#F59E0B",
        "color2": "#EF4444"
    },
    {
        "id": "90-days",
        "title": "90 Days Coding Challenge",
        "desc": "An intense, daily coding curriculum and platform for developers.",
        "tags": ["TypeScript", "Supabase", "Tailwind", "Vercel"],
        "color1": "#6366F1",
        "color2": "#14B8A6"
    }
]

svg_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="600" height="300">
  <defs>
    <linearGradient id="grad-{id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.15" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.05" />
    </linearGradient>
    <linearGradient id="border-grad-{id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.5" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.1" />
    </linearGradient>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&amp;display=swap');
      .title {{ font-family: 'Inter', sans-serif; font-weight: 800; font-size: 28px; fill: #F8FAFC; }}
      .desc {{ font-family: 'Inter', sans-serif; font-weight: 400; font-size: 16px; fill: #94A3B8; }}
      .tag-text {{ font-family: 'Inter', sans-serif; font-weight: 600; font-size: 12px; fill: {color1}; }}
    </style>
  </defs>

  <rect width="600" height="300" rx="20" fill="#0B1120" />
  <rect width="600" height="300" rx="20" fill="url(#grad-{id})" stroke="url(#border-grad-{id})" stroke-width="2" />
  
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="60" height="60" rx="16" fill="{color1}" fill-opacity="0.2" stroke="{color1}" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="30" cy="30" r="12" fill="{color2}" opacity="0.8"/>
    <circle cx="30" cy="30" r="6" fill="#FFF" opacity="0.9"/>
  </g>

  <text x="120" y="80" class="title">{title}</text>
  
  <foreignObject x="120" y="100" width="440" height="80">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Inter', sans-serif; font-size: 16px; color: #94A3B8; line-height: 1.5;">
      {desc}
    </div>
  </foreignObject>

  <!-- Tags -->
  <g transform="translate(120, 180)">
    <rect x="0" y="0" width="80" height="28" rx="8" fill="{color1}" fill-opacity="0.1" stroke="{color1}" stroke-opacity="0.3"/>
    <text x="40" y="18" text-anchor="middle" class="tag-text">{tag1}</text>
    
    <rect x="90" y="0" width="90" height="28" rx="8" fill="{color1}" fill-opacity="0.1" stroke="{color1}" stroke-opacity="0.3"/>
    <text x="135" y="18" text-anchor="middle" class="tag-text">{tag2}</text>
    
    <rect x="190" y="0" width="80" height="28" rx="8" fill="{color1}" fill-opacity="0.1" stroke="{color1}" stroke-opacity="0.3"/>
    <text x="230" y="18" text-anchor="middle" class="tag-text">{tag3}</text>
    
    <rect x="280" y="0" width="80" height="28" rx="8" fill="{color1}" fill-opacity="0.1" stroke="{color1}" stroke-opacity="0.3"/>
    <text x="320" y="18" text-anchor="middle" class="tag-text">{tag4}</text>
  </g>
  
  <!-- Buttons -->
  <g transform="translate(120, 240)">
    <rect x="0" y="0" width="140" height="36" rx="18" fill="#F8FAFC" />
    <text x="70" y="22" text-anchor="middle" font-family="Inter" font-weight="600" font-size="14" fill="#050816">View Project ↗</text>
    
    <rect x="150" y="0" width="120" height="36" rx="18" fill="transparent" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="210" y="22" text-anchor="middle" font-family="Inter" font-weight="600" font-size="14" fill="#F8FAFC">GitHub</text>
  </g>
</svg>"""

out_dir = r"d:\github\github-profile-kit\assets\projects"
os.makedirs(out_dir, exist_ok=True)

for p in projects:
    svg_content = svg_template.format(
        id=p["id"],
        title=p["title"],
        desc=p["desc"],
        color1=p["color1"],
        color2=p["color2"],
        tag1=p["tags"][0],
        tag2=p["tags"][1],
        tag3=p["tags"][2],
        tag4=p["tags"][3]
    )
    with open(os.path.join(out_dir, f'{p["id"]}.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_content)
