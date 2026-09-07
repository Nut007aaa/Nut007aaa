import os

cert_dir = r"d:\github\github-profile-kit\assets\certifications"
os.makedirs(cert_dir, exist_ok=True)

certs = [
    # --- AI & Multi-Agent Systems ---
    {
        "id": "microsoft-ai-skills-fest-2026",
        "title": "AI Skills Fest 2026",
        "issuer": "Microsoft • Credly Verified",
        "badge_type": "Official Microsoft Credential",
        "category": "Artificial Intelligence & Generative AI",
        "desc": "Mastery of advanced Generative AI architectures, multi-agent reasoning systems, and enterprise AI transformation.",
        "tags": ["Generative AI", "AI Agents", "Microsoft", "Copilot"],
        "color1": "#8B5CF6",
        "color2": "#38BDF8",
        "accent": "#00A4EF"
    },
    {
        "id": "google-cloud-engineer-ai-agents",
        "title": "Engineer AI Agents with ADK",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Artificial Intelligence",
        "desc": "Autonomous agent design, Agent Development Kit (ADK), tool calling, context chaining, and prompt orchestration.",
        "tags": ["AI Agents", "ADK", "Gemini", "Cloud AI"],
        "color1": "#38BDF8",
        "color2": "#10B981",
        "accent": "#4285F4"
    },
    {
        "id": "google-cloud-gemini-enterprise",
        "title": "Create First Gemini Enterprise App",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Foundational",
        "category": "Artificial Intelligence",
        "desc": "Developing enterprise-grade multimodal AI applications utilizing the Gemini API, Vertex AI, and vector retrieval.",
        "tags": ["Gemini AI", "Enterprise AI", "Vertex AI", "Multimodal"],
        "color1": "#4285F4",
        "color2": "#8B5CF6",
        "accent": "#4285F4"
    },
    {
        "id": "google-cloud-feedback-agent",
        "title": "Personal Feedback Agent (AI Boost Bites)",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Completion Badge",
        "category": "Artificial Intelligence",
        "desc": "Engineering automated feedback agents with contextual adaptive memory, prompt evaluation, and feedback loops.",
        "tags": ["Feedback Agents", "AI Automation", "Prompt Eng", "Evaluation"],
        "color1": "#F59E0B",
        "color2": "#EC4899",
        "accent": "#EA4335"
    },
    {
        "id": "google-cloud-prepare-data-ml-apis",
        "title": "Prepare Data for ML APIs",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Foundational",
        "category": "Smart Analytics & ML",
        "desc": "Preprocessing, feature extraction, dataset curation, and seamless pipeline integration for Google Cloud ML APIs.",
        "tags": ["Machine Learning", "Data Prep", "Vision API", "BigQuery ML"],
        "color1": "#10B981",
        "color2": "#38BDF8",
        "accent": "#34A853"
    },

    # --- Cloud Infrastructure, Kubernetes & Terraform ---
    {
        "id": "google-cloud-manage-kubernetes",
        "title": "Manage Kubernetes in Google Cloud",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Hybrid & Multi-Cloud",
        "desc": "Container orchestration with GKE: multi-node clusters, deployments, auto-scaling, rolling updates, and monitoring.",
        "tags": ["Kubernetes", "GKE", "Containers", "DevOps"],
        "color1": "#326CE5",
        "color2": "#38BDF8",
        "accent": "#326CE5"
    },
    {
        "id": "google-cloud-terraform-infrastructure",
        "title": "Build Infrastructure with Terraform",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Infrastructure Modernization",
        "desc": "Declarative Infrastructure-as-Code (IaC), state management, reusable modules, and automated cloud provisioning.",
        "tags": ["Terraform", "IaC", "Automation", "GCP Resources"],
        "color1": "#844FBA",
        "color2": "#38BDF8",
        "accent": "#844FBA"
    },
    {
        "id": "google-cloud-load-balancing",
        "title": "Cloud Load Balancing for Compute Engine",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Infrastructure Modernization",
        "desc": "Deploying global HTTP(S) load balancers, auto-healing managed instance groups, and resilient traffic management.",
        "tags": ["Compute Engine", "Load Balancing", "High Availability", "DevOps"],
        "color1": "#6366F1",
        "color2": "#38BDF8",
        "accent": "#4285F4"
    },
    {
        "id": "google-cloud-app-dev-environment",
        "title": "Set Up an App Dev Environment",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Foundational",
        "category": "Infrastructure Modernization",
        "desc": "Configuring development environments, IAM service accounts, Cloud Shell, Cloud Storage, and Compute VMs.",
        "tags": ["Cloud SDK", "IAM Accounts", "Cloud Shell", "App Engine"],
        "color1": "#0EA5E9",
        "color2": "#10B981",
        "accent": "#34A853"
    },

    # --- Cloud Networking & Security ---
    {
        "id": "google-cloud-develop-network",
        "title": "Develop Your Google Cloud Network",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Infrastructure Modernization",
        "desc": "Architecting Virtual Private Clouds (VPC), custom subnets, multi-region routing, bastion hosts, and Cloud DNS.",
        "tags": ["VPC Networks", "Cloud DNS", "Subnets", "Routing"],
        "color1": "#2563EB",
        "color2": "#38BDF8",
        "accent": "#4285F4"
    },
    {
        "id": "google-cloud-build-secure-network",
        "title": "Build a Secure Google Cloud Network",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Cloud Security",
        "desc": "Hardening cloud perimeters with Cloud Armor, strict firewall policies, private Google Access, and VPC Service Controls.",
        "tags": ["Cloud Armor", "Firewall Rules", "VPC Security", "Perimeter"],
        "color1": "#DC2626",
        "color2": "#F59E0B",
        "accent": "#EA4335"
    },
    {
        "id": "google-cloud-security-fundamentals",
        "title": "Implement Cloud Security Fundamentals",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Cloud Security",
        "desc": "Implementing least privilege with Cloud IAM, audit logging, Cloud KMS cryptographic keys, and security benchmarks.",
        "tags": ["Cloud IAM", "Cloud KMS", "Audit Logs", "Compliance"],
        "color1": "#EF4444",
        "color2": "#8B5CF6",
        "accent": "#EA4335"
    },

    # --- Data Warehousing & Cloud Storage ---
    {
        "id": "google-cloud-bigquery-data-warehouse",
        "title": "Build a Data Warehouse with BigQuery",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Intermediate",
        "category": "Smart Analytics",
        "desc": "Designing high-performance analytical data warehouses, optimized SQL partitioning, clustering, and BI ingestion.",
        "tags": ["BigQuery", "SQL Analytics", "Data Warehouse", "ETL"],
        "color1": "#0284C7",
        "color2": "#38BDF8",
        "accent": "#4285F4"
    },
    {
        "id": "google-cloud-storage-data-protection",
        "title": "Cloud Storage & Data Protection",
        "issuer": "Google Cloud • Skills Boost",
        "badge_type": "Skill Badge • Foundational",
        "category": "Data Management",
        "desc": "Object lifecycle management, Cloud Storage access control, object versioning, and retention protection policies.",
        "tags": ["Cloud Storage", "Data Protection", "Object Locking", "Disaster Recovery"],
        "color1": "#14B8A6",
        "color2": "#38BDF8",
        "accent": "#34A853"
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
    <rect x="0" y="0" width="130" height="24" rx="6" fill="#1E293B" fill-opacity="0.8" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="65" y="16" text-anchor="middle" class="tag-text">{tag1}</text>

    <rect x="140" y="0" width="135" height="24" rx="6" fill="#1E293B" fill-opacity="0.8" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="207" y="16" text-anchor="middle" class="tag-text">{tag2}</text>

    <rect x="285" y="0" width="130" height="24" rx="6" fill="#1E293B" fill-opacity="0.8" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="350" y="16" text-anchor="middle" class="tag-text">{tag3}</text>

    <rect x="425" y="0" width="145" height="24" rx="6" fill="#1E293B" fill-opacity="0.8" stroke="{color1}" stroke-opacity="0.3" stroke-width="1"/>
    <text x="497" y="16" text-anchor="middle" class="tag-text">{tag4}</text>
  </g>

  <!-- Verification Footer -->
  <g transform="translate(25, 198)">
    <rect x="0" y="0" width="150" height="24" rx="12" fill="#F8FAFC" />
    <text x="75" y="16" text-anchor="middle" font-family="Inter" font-weight="700" font-size="10" fill="#050816">VERIFIED BADGE ✓</text>
    
    <text x="550" y="16" text-anchor="end" font-family="Inter" font-weight="600" font-size="12" fill="#38BDF8">Google Cloud &amp; Microsoft Skills Boost</text>
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

print(f"Generated {len(certs)} certification SVGs in {cert_dir}")
