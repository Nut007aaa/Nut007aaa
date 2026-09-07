import os

cert_dir = r"d:\github\github-profile-kit\assets\certifications"
os.makedirs(cert_dir, exist_ok=True)

certs = [
    {
        "id": "microsoft-ai-skills-fest-2026",
        "title": "AI Skills Fest 2026",
        "issuer": "Microsoft • Credly Verified",
        "date": "Issued Jun 19, 2026",
        "badge_type": "Official Microsoft Credential",
        "desc": "Mastery of cutting-edge Generative AI, intelligent multi-agent systems, and enterprise AI transformation.",
        "tags": ["Artificial Intelligence", "Generative AI", "AI Agents", "Microsoft"],
        "color1": "#8B5CF6",
        "color2": "#38BDF8",
        "accent": "#00A4EF",
        "icon_type": "microsoft"
    },
    {
        "id": "google-cloud-engineer-ai-agents",
        "title": "Engineer AI Agents with ADK",
        "issuer": "Google Cloud • Skills Boost & Credly",
        "date": "Issued May 19, 2026",
        "badge_type": "Skill Badge • Intermediate",
        "desc": "Architecting autonomous agents, tool orchestration, semantic reasoning, and Agent Development Kit (ADK).",
        "tags": ["AI Agents", "Agent Development Kit", "Google Cloud", "LLM Pipelines"],
        "color1": "#38BDF8",
        "color2": "#10B981",
        "accent": "#4285F4",
        "icon_type": "google"
    },
    {
        "id": "google-cloud-load-balancing",
        "title": "Cloud Load Balancing for Compute Engine",
        "issuer": "Google Cloud • Skills Boost & Credly",
        "date": "Issued Jun 3, 2026",
        "badge_type": "Skill Badge • Infrastructure Modernization",
        "desc": "High-availability global traffic distribution, autoscaling compute instances, SSL offloading, and VPC networking.",
        "tags": ["Compute Engine", "Load Balancing", "Cloud Infrastructure", "DevOps"],
        "color1": "#6366F1",
        "color2": "#38BDF8",
        "accent": "#34A853",
        "icon_type": "google"
    },
    {
        "id": "google-cloud-feedback-agent",
        "title": "Personal Feedback Agent: AI Boost Bites",
        "issuer": "Google Cloud • Skills Boost",
        "date": "Earned May 31, 2026",
        "badge_type": "Completion Badge • Artificial Intelligence",
        "desc": "Building adaptive feedback agents with contextual memory, prompt refinement, and automated evaluation.",
        "tags": ["Feedback Agents", "AI Automation", "Prompt Engineering", "Evaluation"],
        "color1": "#F59E0B",
        "color2": "#EC4899",
        "accent": "#EA4335",
        "icon_type": "google"
    }
]

cert_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 280" width="600" height="280">
  <defs>
    <linearGradient id="bg-grad-{id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.12" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.04" />
    </linearGradient>
    <linearGradient id="border-grad-{id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.6" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.15" />
    </linearGradient>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&amp;display=swap');
      .title {{ font-family: 'Inter', sans-serif; font-weight: 800; font-size: 22px; fill: #F8FAFC; }}
      .issuer {{ font-family: 'Inter', sans-serif; font-weight: 700; font-size: 11px; fill: {color1}; letter-spacing: 1.5px; text-transform: uppercase; }}
      .desc {{ font-family: 'Inter', sans-serif; font-weight: 400; font-size: 14px; fill: #94A3B8; line-height: 1.4; }}
      .tag-text {{ font-family: 'Inter', sans-serif; font-weight: 600; font-size: 11px; fill: #E2E8F0; }}
      .date-text {{ font-family: 'Inter', sans-serif; font-weight: 600; font-size: 12px; fill: #64748B; }}
      .badge-type {{ font-family: 'Inter', sans-serif; font-weight: 600; font-size: 11px; fill: {color2}; }}
    </style>
  </defs>

  <!-- Card Background -->
  <rect width="600" height="280" rx="18" fill="#0B1120" />
  <rect width="600" height="280" rx="18" fill="url(#bg-grad-{id})" stroke="url(#border-grad-{id})" stroke-width="1.5" />

  <!-- Top Issuer Header -->
  <g transform="translate(30, 24)">
    <circle cx="8" cy="8" r="5" fill="{accent}" />
    <text x="22" y="12" class="issuer">{issuer}</text>
    <text x="540" y="12" text-anchor="end" class="badge-type">{badge_type}</text>
  </g>

  <!-- Icon Emblem -->
  <g transform="translate(30, 52)">
    <rect width="56" height="56" rx="14" fill="{color1}" fill-opacity="0.15" stroke="{color1}" stroke-opacity="0.4" stroke-width="1" />
    <circle cx="28" cy="28" r="14" fill="{color2}" fill-opacity="0.8" />
    <circle cx="28" cy="28" r="6" fill="#FFF" />
  </g>

  <!-- Title & Date -->
  <text x="102" y="78" class="title">{title}</text>
  <text x="102" y="100" class="date-text">📅 {date}</text>

  <!-- Description -->
  <foreignObject x="30" y="125" width="540" height="60">
    <div xmlns="http://www.w3.org/1999/xhtml" class="desc">
      {desc}
    </div>
  </foreignObject>

  <!-- Skill Tags -->
  <g transform="translate(30, 195)">
    <rect x="0" y="0" width="130" height="26" rx="7" fill="#1E293B" fill-opacity="0.7" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="65" y="17" text-anchor="middle" class="tag-text">{tag1}</text>

    <rect x="140" y="0" width="145" height="26" rx="7" fill="#1E293B" fill-opacity="0.7" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="212" y="17" text-anchor="middle" class="tag-text">{tag2}</text>

    <rect x="295" y="0" width="120" height="26" rx="7" fill="#1E293B" fill-opacity="0.7" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="355" y="17" text-anchor="middle" class="tag-text">{tag3}</text>

    <rect x="425" y="0" width="135" height="26" rx="7" fill="#1E293B" fill-opacity="0.7" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="492" y="17" text-anchor="middle" class="tag-text">{tag4}</text>
  </g>

  <!-- Verification Footer -->
  <g transform="translate(30, 240)">
    <rect x="0" y="0" width="160" height="26" rx="13" fill="#F8FAFC" />
    <text x="80" y="17" text-anchor="middle" font-family="Inter" font-weight="700" font-size="11" fill="#050816">VERIFIED CREDENTIAL ✓</text>
    
    <text x="540" y="18" text-anchor="end" font-family="Inter" font-weight="600" font-size="12" fill="#38BDF8">Credly &amp; Google Cloud Verified</text>
  </g>
</svg>"""

for c in certs:
    svg_data = cert_template.format(
        id=c["id"],
        title=c["title"],
        issuer=c["issuer"],
        date=c["date"],
        badge_type=c["badge_type"],
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

print(f"Generated {len(certs)} certification SVGs in {cert_dir}")
