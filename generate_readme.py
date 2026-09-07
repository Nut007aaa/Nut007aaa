import os

readme_path = r"d:\github\github-profile-kit\README.md"

def get_badge(name, logo, color="0B1120"):
    return f'<img src="https://img.shields.io/badge/{name}-{color}?style=for-the-badge&logo={logo}&logoColor=white" />'

def generate_projects_section():
    projects = [
        {"id": "ai-health", "title": "AI Health Doctor Assistant"},
        {"id": "ai-matrimony", "title": "AI Matrimony Platform"},
        {"id": "portfolio", "title": "Animated Portfolio"},
        {"id": "rizzglam", "title": "RizzGlam"},
        {"id": "90-days", "title": "90 Days Coding Challenge"}
    ]
    html = '<div align="center">\n<table border="0">\n<tr>\n'
    for i, p in enumerate(projects):
        if i > 0 and i % 2 == 0:
            html += '</tr>\n<tr>\n'
        html += f'''
<td align="center" width="50%">
  <a href="https://github.com/Nut007aaa/{p['id']}">
    <img src="assets/projects/{p['id']}.svg" alt="{p['title']}" width="100%" />
  </a>
</td>
'''
    html += '</tr>\n</table>\n</div>\n'
    return html

def generate_certifications_section():
    certs = [
        {"id": "microsoft-ai-skills-fest-2026", "title": "AI Skills Fest 2026 - Microsoft Credly Verified"},
        {"id": "google-cloud-engineer-ai-agents", "title": "Engineer AI Agents with ADK - Google Cloud"},
        {"id": "google-cloud-load-balancing", "title": "Cloud Load Balancing for Compute Engine - Google Cloud"},
        {"id": "google-cloud-feedback-agent", "title": "Personal Feedback Agent: AI Boost Bites - Google Cloud"}
    ]
    html = '<div align="center">\n<table border="0">\n<tr>\n'
    for i, c in enumerate(certs):
        if i > 0 and i % 2 == 0:
            html += '</tr>\n<tr>\n'
        html += f'''
<td align="center" width="50%">
  <img src="assets/certifications/{c['id']}.svg" alt="{c['title']}" width="100%" />
</td>
'''
    html += '</tr>\n</table>\n</div>\n'
    return html

def generate_credly_skills():
    skills = [
        ("AI Agents", "credly", "FF6B00"),
        ("Artificial Intelligence", "credly", "FF6B00"),
        ("AI Ethics", "credly", "FF6B00"),
        ("AI Applications", "credly", "FF6B00"),
        ("Build Automation", "credly", "FF6B00"),
        ("Cloud Computing", "credly", "FF6B00"),
        ("Compute Engine", "credly", "FF6B00"),
        ("Cloud Load Balancing", "google-cloud", "4285F4"),
        ("Agent Dev Kit (ADK)", "google-cloud", "4285F4")
    ]
    html = '<div align="center">\n'
    for name, logo, color in skills:
        html += f'  <img src="https://img.shields.io/badge/{name.replace(" ", "%20")}-Verified-{color}?style=for-the-badge&logo={logo}&logoColor=white" />\n'
    html += '</div>\n'
    return html

def generate_tech_stack():
    stack_data = {
        "AI & Agents": [
            ("AI Agents", "openai"),
            ("Agent Dev Kit (ADK)", "google-cloud"),
            ("PyTorch", "pytorch"),
            ("TensorFlow", "tensorflow"),
            ("FastAPI", "fastapi")
        ],
        "Cloud & Infrastructure": [
            ("Google Cloud", "google-cloud"),
            ("Compute Engine", "google-cloud"),
            ("Load Balancing", "google-cloud"),
            ("Docker", "docker"),
            ("GitHub Actions", "githubactions")
        ],
        "Frontend": [
            ("React", "react"),
            ("Next.js", "next.js"),
            ("TypeScript", "typescript"),
            ("Tailwind", "tailwindcss"),
            ("Framer Motion", "framer")
        ],
        "Backend & DB": [
            ("Node.js", "node.js"),
            ("Python", "python"),
            ("PostgreSQL", "postgresql"),
            ("MongoDB", "mongodb"),
            ("GraphQL", "graphql")
        ]
    }
    
    html = '<table align="center" border="0">\n'
    for category, techs in stack_data.items():
        html += f'  <tr>\n    <td align="right" width="22%"><b>{category}</b></td>\n    <td width="78%">\n'
        for name, logo in techs:
            html += f'      {get_badge(name, logo)} '
        html += '\n    </td>\n  </tr>\n'
    html += '</table>\n'
    return html

readme_content = f"""<!-- 
======================================================
  PREMIUM GITHUB PROFILE 
  Designed with Apple, Stripe, and Vercel Aesthetics
======================================================
-->

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner/hero.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/banner/hero.svg">
    <img alt="Hero Banner" src="assets/banner/hero.svg" width="100%">
  </picture>
</div>

<br />

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/svg/typing-header.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/svg/typing-header.svg">
    <img alt="Typing Animation" src="assets/svg/typing-header.svg" width="100%">
  </picture>
</div>

<br />

<div align="center">
  <a href="https://nut007aaa.github.io" target="_blank"><img src="https://img.shields.io/badge/Portfolio-050816?style=for-the-badge&logo=vercel&logoColor=white&borderColor=38BDF8" alt="Portfolio" /></a>
  <a href="https://linkedin.com/in/Nut007aaa" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-050816?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://twitter.com/Nut007aaa" target="_blank"><img src="https://img.shields.io/badge/Twitter-050816?style=for-the-badge&logo=x&logoColor=white" alt="Twitter" /></a>
  <a href="mailto:anish.shaiks007@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Email-050816?style=for-the-badge&logo=minutemailer&logoColor=white" alt="Email" /></a>
  <a href="resume.pdf" target="_blank"><img src="https://img.shields.io/badge/Resume-050816?style=for-the-badge&logo=googledocs&logoColor=white" alt="Resume" /></a>
</div>

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## 🌌 The Vision

> **Building real-world products at the intersection of Artificial Intelligence, Cloud Infrastructure, and Premium Design.**

I am **Anish Shaik**, a **Senior Staff Software Engineer** and **Product Designer** with a relentless pursuit of excellence. My work doesn't just function—it performs beautifully. I specialize in crafting autonomous AI agent architectures, resilient cloud infrastructure on Google Cloud & Microsoft ecosystems, and responsive digital products with an uncompromising focus on user experience.

---

## 🏆 Verified Certifications & Badges

<div align="center">
  <p>Recognized by <b>Microsoft</b> and <b>Google Cloud</b> for expertise in Artificial Intelligence, Multi-Agent Systems, and Cloud Infrastructure.</p>
</div>

{generate_certifications_section()}

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## 🎖️ Credly Verified Skills

<div align="center">
  <p><i>Official skill competencies verified by Credly, Google Cloud, and Microsoft.</i></p>
</div>

{generate_credly_skills()}

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## 🛠️ Tech Stack & Skill Matrix

<div align="center">
{generate_tech_stack()}
</div>

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## 🏗️ System Architecture & Design

I architect systems for scale. From edge-deployed serverless functions to heavy GPU-bound ML microservices and load-balanced Compute Engine clusters, my systems are designed with high availability, low latency, and robust observability.

<div align="center">
  <img src="assets/svg/architecture.svg" width="100%" alt="System Architecture">
</div>

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## 🚀 Featured Projects

My portfolio includes projects ranging from autonomous AI agents to complex consumer applications. Each product is built to production standards, complete with CI/CD, analytics, and responsive premium UIs.

{generate_projects_section()}

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## 📈 GitHub Analytics

<div align="center">
  <table border="0">
    <tr>
      <td width="50%">
        <img src="assets/svg/github-stats.svg" alt="GitHub Stats" width="100%" />
      </td>
      <td width="50%">
        <img src="https://streak-stats.demolab.com/?user=Nut007aaa&theme=react&hide_border=true&background=0B1120&ring=38BDF8&fire=8B5CF6&currStreakLabel=F8FAFC" alt="GitHub Streak" width="100%" />
      </td>
    </tr>
  </table>
  <br />
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/svg/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/svg/github-snake.svg">
    <img alt="github contribution grid snake animation" src="assets/svg/github-snake-dark.svg" width="100%">
  </picture>
</div>

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## ⏱️ Coding & Focus Activity

<div align="center">
  <table border="0">
    <tr>
      <td align="center" width="25%">
        <b>🤖 AI Agent Development</b><br/>
        <small>Agent Dev Kit • Multi-Agent Loops</small>
      </td>
      <td align="center" width="25%">
        <b>☁️ Cloud Infrastructure</b><br/>
        <small>Compute Engine • Load Balancing</small>
      </td>
      <td align="center" width="25%">
        <b>⚡ High-Scale Systems</b><br/>
        <small>FastAPI • Node.js • Distributed Systems</small>
      </td>
      <td align="center" width="25%">
        <b>🎨 Premium Design</b><br/>
        <small>React • Next.js • Interactive UIs</small>
      </td>
    </tr>
  </table>
</div>

<!--START_SECTION:waka-->
<!--END_SECTION:waka-->

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## 🎓 Education & Credentials

* **Microsoft Certified: AI Skills Fest 2026** (Credly Verified)
* **Google Cloud Skill Badge**: Engineer AI Agents with Agent Development Kit (ADK)
* **Google Cloud Skill Badge**: Implementing Cloud Load Balancing for Compute Engine
* **Google Cloud Completion Badge**: AI Boost Bites - Personal Feedback Agent
* **M.S. Computer Science** (Specialization in Artificial Intelligence)

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

## 🎵 Currently Listening To

<div align="center">
  <a href="https://spotify.com">
    <img src="https://spotify-github-profile.vercel.app/api/view?uid=Nut007aaa&cover_image=true&theme=novathem&bar_color=38BDF8&bar_color_cover=false" alt="Spotify Listening" />
  </a>
</div>

<div align="center">
  <img src="assets/svg/divider.svg" width="100%" />
</div>

<div align="center">
  <i>"Design is not just what it looks like and feels like. Design is how it works."</i>
  <br>
  <b>— Steve Jobs</b>
</div>

<br>

<div align="center">
  <p><small>Copyright © 2026 Anish Shaik. Handcrafted with precision.</small></p>
</div>
"""

# Let's pad it to ensure clean vertical rhythm
for i in range(25):
    readme_content += "\n<!-- Spacing block for premium vertical rhythm -->\n<br/>"

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_content.strip())

print("README.md generated successfully!")
