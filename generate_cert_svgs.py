import os

cert_dir = r"d:\github\github-profile-kit\assets\certifications"
os.makedirs(cert_dir, exist_ok=True)

# Clean out old unearned recommendation SVGs if any
for fname in os.listdir(cert_dir):
    if fname.endswith(".svg"):
        os.remove(os.path.join(cert_dir, fname))

certs = [
    # 1. Microsoft AI Skills Fest
    {
        "id": "microsoft-ai-skills-fest-2026",
        "title": "AI Skills Fest 2026",
        "issuer": "Microsoft • Credly Verified",
        "badge_type": "Official Credential • Jun 2026",
        "category": "Artificial Intelligence & Generative AI",
        "desc": "Mastery of advanced Generative AI architectures, multi-agent systems, prompt design, and enterprise AI transformation.",
        "tags": ["Generative AI", "AI Agents", "Microsoft", "Credly Verified"],
        "color1": "#8B5CF6",
        "color2": "#38BDF8",
        "accent": "#00A4EF"
    },
    # 2. Google Cloud Engineer AI Agents
    {
        "id": "google-cloud-engineer-ai-agents",
        "title": "Engineer AI Agents with ADK",
        "issuer": "Google Cloud • Skills Boost & Credly",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Artificial Intelligence",
        "desc": "Autonomous agent design, Agent Development Kit (ADK), multi-step tool calling, context chaining, and prompt orchestration.",
        "tags": ["AI Agents", "Agent Dev Kit", "Gemini", "Cloud AI"],
        "color1": "#38BDF8",
        "color2": "#10B981",
        "accent": "#4285F4"
    },
    # 3. Google Cloud Load Balancing
    {
        "id": "google-cloud-load-balancing",
        "title": "Cloud Load Balancing for Compute Engine",
        "issuer": "Google Cloud • Skills Boost & Credly",
        "badge_type": "Skill Badge • Infrastructure Modernization",
        "category": "Cloud Infrastructure",
        "desc": "Deploying global HTTP(S) load balancers, auto-healing managed instance groups, SSL termination, and resilient traffic routing.",
        "tags": ["Compute Engine", "Load Balancing", "High Availability", "DevOps"],
        "color1": "#6366F1",
        "color2": "#38BDF8",
        "accent": "#4285F4"
    },
    # 4. Google Cloud Feedback Agent
    {
        "id": "google-cloud-feedback-agent",
        "title": "Personal Feedback Agent: AI Boost Bites",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Completion Badge • May 2026",
        "category": "Artificial Intelligence",
        "desc": "Engineering adaptive feedback agents with contextual memory, automated prompt refinement, and iterative model evaluation.",
        "tags": ["Feedback Agents", "AI Automation", "Prompt Eng", "Evaluation"],
        "color1": "#F59E0B",
        "color2": "#EC4899",
        "accent": "#EA4335"
    },
    # 5. AWS Solutions Architecture
    {
        "id": "aws-solutions-architecture-forage",
        "title": "AWS Solutions Architecture Simulation",
        "issuer": "AWS • Forage Certified",
        "badge_type": "Job Simulation • Jan 2026",
        "category": "Cloud Architecture & AWS",
        "desc": "Designing scalable, fault-tolerant AWS architectures, multi-tier VPC configurations, serverless components, and cost optimization.",
        "tags": ["AWS Architecture", "Solutions Design", "VPC & EC2", "ID: pBdoefEGGx..."],
        "color1": "#FF9900",
        "color2": "#38BDF8",
        "accent": "#FF9900"
    },
    # 6. Forage Data Labeling
    {
        "id": "forage-data-labeling-simulation",
        "title": "Data Labeling Job Simulation",
        "issuer": "Forage Academy Certified",
        "badge_type": "Job Simulation • Jan 2026",
        "category": "AI Data Engineering & ML Quality",
        "desc": "Data annotation pipelines, segmentation workflows, bounding box precision verification, and dataset curation for ML models.",
        "tags": ["Data Labeling", "ML Datasets", "Annotation", "ID: px874ydEdX..."],
        "color1": "#0084FF",
        "color2": "#8B5CF6",
        "accent": "#0084FF"
    },
    # 7. TATA Crucible Quiz
    {
        "id": "tata-crucible-campus-quiz-2025",
        "title": "TATA Crucible Campus Quiz 2025",
        "issuer": "TATA & Unstop Verified",
        "badge_type": "Certificate of Participation • Nov 2025",
        "category": "Competitive Honors",
        "desc": "Participated in India's prestigious national business and technology quizzing championship organized by TATA and Unstop.",
        "tags": ["TATA Crucible", "Unstop", "Tech Strategy", "ID: d3fc9eec-4f..."],
        "color1": "#006699",
        "color2": "#38BDF8",
        "accent": "#006699"
    }
]

cert_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="600" height="240">
  <defs>
    <linearGradient id="bg-grad-{id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.14" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.04" />
    </linearGradient>
    <linearGradient id="border-grad-{id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.6" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.15" />
    </linearGradient>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&amp;display=swap');
      .title {{ font-family: 'Inter', sans-serif; font-weight: 800; font-size: 20px; fill: #F8FAFC; }}
      .issuer {{ font-family: 'Inter', sans-serif; font-weight: 700; font-size: 11px; fill: {color1}; letter-spacing: 1.2px; text-transform: uppercase; }}
      .category {{ font-family: 'Inter', sans-serif; font-weight: 600; font-size: 11px; fill: #94A3B8; }}
      .desc {{ font-family: 'Inter', sans-serif; font-weight: 400; font-size: 13px; fill: #94A3B8; line-height: 1.4; }}
      .tag-text {{ font-family: 'Inter', sans-serif; font-weight: 600; font-size: 11px; fill: #E2E8F0; }}
      .badge-type {{ font-family: 'Inter', sans-serif; font-weight: 700; font-size: 11px; fill: {color2}; }}
    </style>
  </defs>

  <!-- Card Background -->
  <rect width="600" height="240" rx="16" fill="#0B1120" />
  <rect width="600" height="240" rx="16" fill="url(#bg-grad-{id})" stroke="url(#border-grad-{id})" stroke-width="1.5" />

  <!-- Top Issuer Header -->
  <g transform="translate(25, 20)">
    <circle cx="6" cy="6" r="5" fill="{accent}" />
    <text x="18" y="10" class="issuer">{issuer}</text>
    <text x="550" y="10" text-anchor="end" class="badge-type">{badge_type}</text>
  </g>

  <!-- Icon Emblem -->
  <g transform="translate(25, 42)">
    <rect width="44" height="44" rx="12" fill="{color1}" fill-opacity="0.15" stroke="{color1}" stroke-opacity="0.4" stroke-width="1" />
    <circle cx="22" cy="22" r="11" fill="{color2}" fill-opacity="0.8" />
    <circle cx="22" cy="22" r="5" fill="#FFF" />
  </g>

  <!-- Title & Category -->
  <text x="82" y="62" class="title">{title}</text>
  <text x="82" y="80" class="category">📂 {category}</text>

  <!-- Description -->
  <foreignObject x="25" y="98" width="550" height="52">
    <div xmlns="http://www.w3.org/1999/xhtml" class="desc">
      {desc}
    </div>
  </foreignObject>

  <!-- Skill Tags -->
  <g transform="translate(25, 158)">
    <rect x="0" y="0" width="135" height="24" rx="6" fill="#1E293B" fill-opacity="0.8" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="67" y="16" text-anchor="middle" class="tag-text">{tag1}</text>

    <rect x="145" y="0" width="135" height="24" rx="6" fill="#1E293B" fill-opacity="0.8" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="212" y="16" text-anchor="middle" class="tag-text">{tag2}</text>

    <rect x="290" y="0" width="130" height="24" rx="6" fill="#1E293B" fill-opacity="0.8" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="355" y="16" text-anchor="middle" class="tag-text">{tag3}</text>

    <rect x="430" y="0" width="140" height="24" rx="6" fill="#1E293B" fill-opacity="0.8" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="500" y="16" text-anchor="middle" class="tag-text">{tag4}</text>
  </g>

  <!-- Verification Footer -->
  <g transform="translate(25, 198)">
    <rect x="0" y="0" width="150" height="24" rx="12" fill="#F8FAFC" />
    <text x="75" y="16" text-anchor="middle" font-family="Inter" font-weight="700" font-size="10" fill="#050816">VERIFIED BADGE ✓</text>
    
    <text x="550" y="16" text-anchor="end" font-family="Inter" font-weight="600" font-size="12" fill="#38BDF8">Official License &amp; Credential</text>
  </g>
</svg>"""

for c in certs:
    svg_data = cert_template.format(
        id=c["id"],
        title=c["title"],
        issuer=c["issuer"],
        badge_type=c["badge_type"],
        category=c["category"],
        desc=c["desc"],
        tag1=c["tags"][0],
        tag2=c["tags"][1],
        tag3=c["tags"][2],
        tag4=c["tags"][3],
        color1=c["color1"],
        color2=c["color2"],
        accent=c["accent"]
    )
    with open(os.path.join(cert_dir, f'{c["id"]}.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_data)

print(f"Generated {len(certs)} authentic certification SVGs in {cert_dir}")
