import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Shih-Yu (Fiona) Wu - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean, minimal design
st.markdown("""
<style>
    body {
        font-family: 'Inter', sans-serif;
        background-color: #ffffff;
        color: #333333;
    }
    .main {
        padding: 2rem 3rem;
    }
    h1, h2, h3, h4 {
        font-weight: 600;
        color: #002851;
    }
    h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    h2 {
        font-size: 1.8rem;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 0.5rem;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
    }
    a {
        color: #0066cc;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    .section {
        margin-bottom: 2rem;
    }
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
        border: 1px solid #f0f0f0;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    .tech-pill {
        display: inline-block;
        background-color: #f0f2f5;
        color: #333;
        padding: 0.3rem 0.6rem;
        border-radius: 1rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        font-size: 0.8rem;
        font-weight: 500;
    }
    .contact-info {
        display: flex;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    .contact-info img {
        margin-right: 0.5rem;
    }
    .project-title {
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    .company {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    .skill-category {
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #002851;
    }
    .footer {
        text-align: center;
        color: #666;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #f0f0f0;
    }
    .profile-section {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
    }
    .profile-image {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        margin-right: 2rem;
    }
    .social-links {
        margin-top: 1rem;
    }
    .social-links a {
        margin-right: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header/Intro Section
col1, col2 = st.columns([1, 5])

with col1:
    # Using st.image for the profile photo - this handles local images correctly
    try:
        st.image("images/profile.jpg", width=600)
    except:
        # Fallback to placeholder if image doesn't exist
        st.image("https://via.placeholder.com/300", width=200)

with col2:
    st.markdown("""
    <h1>Shih-Yu (Fiona) Wu</h1>
    <p style="font-size: 1.2rem; margin-bottom: 1rem;">Frontend Engineer & Creative Technologist</p>
    <p>I'm passionate about building engaging and seamless digital experiences. With three years of frontend development experience, I specialize in React, TypeScript, and performance-driven UI design.</p>
    <div class="social-links">
        <a href="https://github.com/Fiona1121" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/shihyuwu/" target="_blank">LinkedIn</a>
        <a href="https://itzsyboo.dev/" target="_blank">Website</a>
        <a href="mailto:itzsyboo@uw.edu">Email</a>
    </div>
    """, unsafe_allow_html=True)

# About Me Section
st.markdown("## About Me")
st.markdown("""
I'm Fiona Wu, a frontend engineer and creative technologist passionate about building engaging and seamless digital experiences. 
I love blending aesthetics with functionality to create intuitive interfaces that enhance user interaction. When I'm not coding, 
I enjoy exploring design thinking, rapid prototyping, and human-computer interaction.

- 🎨 **Design + Code Enthusiast**: Creating things that are both functional and beautiful
- 💻 **Wrote My First Line of Code at 13**: Started my obsession with building digital experiences
- ☕ **Coffee-Powered Developer**: Dark roast, no sugar—fueling late-night coding sessions
- 🏐 **Loves Volleyball & Soccer**: Any excuse to smash or kick things, count me in!
- 🐱 **Master of Cat Sounds**: I can perfectly fake cat noises—confusing humans and cats alike
""")

# Skills Section
st.markdown("## Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <p class="skill-category">Frontend Development</p>
        <span class="tech-pill">React.js</span>
        <span class="tech-pill">Next.js</span>
        <span class="tech-pill">TypeScript</span>
        <span class="tech-pill">JavaScript</span>
        <span class="tech-pill">HTML</span>
        <span class="tech-pill">Tailwind CSS</span>
        <span class="tech-pill">Redux</span>
        <span class="tech-pill">React Context</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <p class="skill-category">UI/UX & Design</p>
        <span class="tech-pill">Figma</span>
        <span class="tech-pill">Adobe XD</span>
        <span class="tech-pill">Sketch</span>
        <span class="tech-pill">Miro</span>
        <span class="tech-pill">WCAG Compliance</span>
        <span class="tech-pill">ARIA</span>
        <span class="tech-pill">Mobile-First Design</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <p class="skill-category">Backend & DevOps</p>
        <span class="tech-pill">Node.js</span>
        <span class="tech-pill">Firebase</span>
        <span class="tech-pill">GraphQL</span>
        <span class="tech-pill">Git</span>
        <span class="tech-pill">GitHub Actions</span>
        <span class="tech-pill">Jest</span>
        <span class="tech-pill">Cypress</span>
    </div>
    """, unsafe_allow_html=True)

# Projects Section
st.markdown("## Featured Projects")

# Project data
projects = [
    {
        "title": "CheckMate App",
        "company": "Personal Project",
        "description": "A React Native app that automatically extracts and splits receipts using AI. Snap a photo or upload a receipt, and let OpenAI analyze, itemize, and calculate totals for an effortless bill-splitting experience.",
        "tech": ["React Native", "Expo", "TypeScript", "OpenAI"],
        "link": "https://github.com/Fiona1121/CheckMate",
        "link_text": "View on GitHub",
        "image_path": "images/checkmate.jpg"
    },
    {
        "title": "Lanrenpao Website",
        "company": "Bypon Design Ltd.",
        "description": "A platform designed to streamline the process of hosting and discovering murder mystery games. It connects game hosts with players, offering a seamless experience for script distribution, game management, and event organization.",
        "tech": ["Next.js", "React.js", "Tailwind CSS", "Sanity", "GraphQL"],
        "link": "https://www.lanrenpao.com/",
        "link_text": "Visit Website",
        "image_path": "images/lanrenpao.jpg"
    },
    {
        "title": "NTUEE LightDance Editor",
        "company": "Frontend Lead, 2022",
        "description": "An interactive 3D choreography tool designed to synchronize LED light sequences with live dance performances. The tool provides real-time visualization for choreographers.",
        "tech": ["React.js", "TypeScript", "Redux", "Three.js", "GraphQL", "MongoDB"],
        "link": "https://github.com/NTUEELightDance/LightDance-Editor",
        "link_text": "View on GitHub",
        "image_path": "images/lightdance.jpg"
    },
    {
        "title": "Creatify",
        "company": "Memopresso Inc.",
        "description": "A web-based platform designed to empower content creators by providing an intuitive, real-time customization and merchandising experience. The platform enables creators to design, preview, and sell custom products effortlessly.",
        "tech": ["Next.js", "React.js", "Redux", "Tailwind CSS", "Node.js", "Strapi CMS"],
        "link": "https://creatify.tw/",
        "link_text": "Visit Website",
        "image_path": "images/creatify.jpg"
    }
]

# Display projects in two columns
col1, col2 = st.columns(2)
cols = [col1, col2]

for i, project in enumerate(projects):
    with cols[i % 2]:
        # Card container
        st.markdown(f"""
        <div class="card">
            <p class="project-title">{project['title']}</p>
            <p class="company">{project['company']}</p>
            <p>{project['description']}</p>
            <div style="margin: 0.8rem 0;">
                {"".join([f'<span class="tech-pill">{tech}</span>' for tech in project['tech']])}
            </div>
            <a href="{project['link']}" target="_blank">{project['link_text']}</a>
        </div>
        """, unsafe_allow_html=True)

# Beyond Code Section
st.markdown("## Beyond Code")

# Creative projects data
creative_projects = [
    {
        "title": "SoulSip – Emotion Bartender",
        "description": "A Raspberry Pi-powered system that captures user emotions via Pi Camera, sends images to OpenAI for emotion detection, and generates a personalized drink recipe, printed instantly. Designed to create fun and interactive social experiences.",
        "link": "https://youtu.be/TGN7F6eTANY",
        "link_text": "Watch Demo",
        "image_path": "images/soulsip.jpg"
    },
    {
        "title": "Interactive Phone Holder",
        "description": "Inspired by the Flora app, this mechanical phone stand reveals a blooming plant when the phone is placed down, visually reinforcing focus and mindful digital habits. Designed to create a fun, engaging interaction that encourages users to stay present.",
        "image_path": "images/phoneholder.jpg"
    }
]

col1, col2 = st.columns(2)
cols = [col1, col2]

for i, project in enumerate(creative_projects):
    with cols[i % 2]:
        # Card container
        st.markdown(f"""
        <div class="card">
            <p class="project-title">{project['title']}</p>
            <p>{project['description']}</p>
            {f'<a href="{project["link"]}" target="_blank">{project["link_text"]}</a>' if "link" in project else ""}
        </div>
        """, unsafe_allow_html=True)

# Contact Section
st.markdown("## Let's Connect")

st.markdown("""
<div class="card">
    <p>Always open to exciting projects, collaborations, and tech chats! Whether it's about frontend development, design, or just geeking out over anime and cool gadgets, feel free to reach out!</p>
    <div class="contact-info">
        <span>📧</span>
        <a href="mailto:itzsyboo@uw.edu">itzsyboo@uw.edu</a>
    </div>
    <div class="contact-info">
        <span>🌐</span>
        <a href="https://itzsyboo.dev/" target="_blank">https://itzsyboo.dev/</a>
    </div>
    <div class="contact-info">
        <span>👩‍💻</span>
        <a href="https://github.com/Fiona1121" target="_blank">github.com/Fiona1121</a>
    </div>
    <div class="contact-info">
        <span>👔</span>
        <a href="https://www.linkedin.com/in/shihyuwu/" target="_blank">linkedin.com/in/shihyuwu</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 Shih-Yu (Fiona) Wu. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)