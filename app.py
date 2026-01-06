from flask import Flask, render_template_string, send_from_directory, url_for
import os

app = Flask(__name__)

# ---- Updated Portfolio Data based on new CV ----
portfolio = {
    "name": "Omar Elsharoud",
    "title": "Software Engineering Student | Aspiring Software Developer",
    "location": "Cardiff, Wales, CF3 6YP",
    "email": "f.elsharoud@gmail.com",
    "phone": "+44 7881 851872",

    "profile": (
        "Motivated and detail-oriented Software Engineering student with a strong foundation in the "
        "Full Software Development Lifecycle (SDLC). Possess strong practical experience delivering "
        "software projects in both academic and independent settings. Proficient in Microsoft Windows "
        "Platform development, with a solid understanding of OS architecture, services, and security features. "
        "Proven ability to lead teams, implement secure systems, and execute comprehensive unit and software testing. "
        "Seeking a graduate opportunity to apply technical expertise in a fast-paced, innovative environment."
    ),

    "education": [
        {
            "degree": "BSc (Hons) Software Engineering",
            "institution": "Cardiff Metropolitan University",
            "dates": "Sept 2023 – Present",
            "notes": "Relevant Modules: Operating Systems, Advanced Programming, Database Management."
        },
        {
            "degree": "A-Levels & Equivalent",
            "institution": "Cardiff High School",
            "dates": "Sept 2018 – June 2022",
            "notes": (
                "Subjects: Mathematics, Chemistry, Physics, ICT, Biology, Design & Technology, "
                "Business."
            )
        }
    ],

    "projects": [
        {
            "title": "QuizCraft – Online Assessment Platform",
            "items": [
                "Architected a secure web application using PHP 8.0 and MySQL, adhering to a strict MVC (Model-View-Controller) architecture to ensure scalable code organization.",
                "Engineered a Directed Graph data structure to handle conditional logic, enabling complex branching paths where user answers dictate the next question.",
                "Implemented core Design Patterns including the Singleton Pattern for optimized database connections and the Factory Pattern for dynamic question rendering.",
                "Ensured system reliability and security by writing comprehensive Unit and Integration tests using PHPUnit and utilizing PDO Prepared Statements to prevent SQL injection."
            ]
        },
        {
            "title": "Mental Health Support Platform (Team Lead)",
            "items": [
                "Oversaw the Full Development Lifecycle, from requirement gathering to deployment and testing.",
                "Developed a secure web app with user authentication (PHP sessions) and SQL database hashing.",
                "Conducted unit testing on booking algorithms and security features to ensure data integrity.",
                "Managed the project codebase using GitHub, ensuring version control and smooth collaboration.",
                "Fine-tuned an AI chatbot for ethical interaction regarding sensitive mental health queries."
            ]
        },
        {
            "title": "Medical Chatbot for NHS Triage",
            "items": [
                "Developed a web-based chatbot using AI APIs, fine-tuned for accurate triage guidance.",
                "Implemented rigorous software testing protocols to refine answers, limiting inappropriate responses through custom filters.",
                "Focused on safety and reliability, mirroring critical system architecture standards."
            ]
        },
        {
            "title": "Caravan Rental Website (Lead Developer)",
            "items": [
                "Led a team to build a dynamic rental website using PHP, JavaScript, and SQL.",
                "Utilized Agile methodologies for sprint planning and iterative development.",
                "Implemented back-end logic and database structures that laid the foundation for advanced booking systems."
            ]
        },
        {
            "title": "Welsh Museums Mobile App",
            "items": [
                "Designed and implemented UI/UX independently, ensuring accessibility and bilingual support.",
                "Integrated Google Maps API for location functionality.",
                "Managed source code and feature updates via GitHub."
            ]
        }
    ],

    # Refactored skills to match the Categories in the new CV
    "skills_categorized": [
        {
            "category": "Languages & Web",
            "items": ["Python", "Java", "PHP", "JavaScript", "HTML", "CSS", "SQL (MySQL)"]
        },
        {
            "category": "Windows Ecosystem",
            "items": ["Microsoft Windows Platform Development", "Windows OS Architecture", "Development Frameworks", "System Services", "Security Features"]
        },
        {
            "category": "DevOps & Tools",
            "items": ["GitHub (Branching, PRs)", "Git", "Version Control", "CI/CD Awareness", "Cisco Packet Tracer"]
        },
        {
            "category": "Methodologies & Testing",
            "items": ["Agile (Scrum)", "Full SDLC Management", "Unit Testing", "Software Testing (Integration/System)", "Debugging"]
        },
        {
            "category": "Security",
            "items": ["Data Hashing", "Secure Session Management", "GDPR Compliance Awareness"]
        }
    ],

    "experience": [
        {
            "role": "Admin Assistant",
            "company": "HMRC",
            "dates": "Sept 2022 – Sep 2023",
            "highlights": [
                "Managed high-volume customer queries, applying structured problem-solving similar to software debugging.",
                "Processed sensitive data in line with strict compliance frameworks, mirroring security practices in software engineering.",
                "Gained strong skills in process optimization and working under pressure."
            ]
        },
        {
            "role": "Charity Volunteer",
            "company": "Local Distribution Warehouse",
            "dates": "July 2018 – Sep 2018",
            "highlights": [
                "Supported logistics and distribution, strengthening teamwork and communication skills."
            ]
        }
    ],

    "leadership": [
        {
            "role": "Scout Leader",
            "org": "Scouts Association (Ongoing)",
            "highlights": [
                "Organized and led camps and hikes, ensuring safety and logistics.",
                "Mentored youth, fostering teamwork, resilience, and problem-solving.",
                "Transferred leadership skills into technical settings by guiding development teams and delegating tasks effectively."
            ]
        }
    ],

    "languages": ["English (Bilingual)", "Arabic (Bilingual)"],

    "additional_info": [
        "Full UK Driving License (since Oct 2021)."
    ],

    # Update this filename to match your actual CV filename
    "cv_path": os.path.join(os.getcwd(), 'Omar_Elsharoud_CV.docx')
}


# ---- Updated Interactive Template ----
TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{{p.name}} — Portfolio</title>
  <style>
    body {
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      margin:0; 
      background:#0f172a; 
      color:#f1f5f9; 
      line-height:1.8; 
      scroll-behavior:smooth;
    }
    section {
      min-height:90vh; 
      display:flex; 
      flex-direction:column; 
      justify-content:center; 
      align-items:center; 
      padding:60px 20px;
      opacity:0; 
      transform:translateY(50px);
      transition: all 1s ease-out;
      max-width: 1000px;
      margin: 0 auto;
    }
    section.visible {
      opacity:1; 
      transform:translateY(0);
    }
    h1 {
      font-size:64px; 
      font-weight:800; 
      margin-bottom:20px;
      text-align: center;
    }
    h2 {
      font-size:38px; 
      font-weight:700; 
      margin-bottom:30px;
      color:#38bdf8;
      border-bottom: 2px solid #38bdf8;
      padding-bottom: 10px;
    }
    h3 {
      font-size: 24px;
      color: #e2e8f0;
      margin-top: 0;
      margin-bottom: 10px;
    }
    p, li {
      font-size:18px;
      color: #cbd5e1;
    }
    .text-center { text-align: center; }
    
    nav {
      position:fixed; 
      top:20px; 
      left:50%; 
      transform:translateX(-50%);
      display:flex; 
      gap:20px; 
      background:rgba(30, 41, 59, 0.9); 
      backdrop-filter: blur(10px);
      padding:12px 24px; 
      border-radius:12px; 
      box-shadow:0 4px 20px rgba(0,0,0,0.5);
      z-index:1000;
    }
    nav a {
      color:#f1f5f9; 
      text-decoration:none; 
      font-size:16px; 
      font-weight:600; 
      transition:color 0.3s;
    }
    nav a:hover {
      color:#38bdf8;
    }
    
    /* Project & Experience Cards */
    .card {
        background: #1e293b;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    ul { padding-left:20px; }
    ul li { margin:8px 0; }
    
    /* Skills Chips */
    .skill-category {
      width: 100%;
      margin-bottom: 25px;
      text-align: center;
    }
    .skill-category h4 {
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .chip {
      display:inline-block;
      padding:8px 16px;
      border-radius:999px;
      background:#334155;
      margin:5px;
      font-size:16px;
      font-weight:500;
      transition: all 0.3s;
      border: 1px solid #475569;
    }
    .chip:hover {
        background: #38bdf8;
        color: #0f172a;
        transform: translateY(-2px);
    }

    img.profile {
      width:220px; 
      height:220px; 
      border-radius:50%; 
      border:6px solid #38bdf8;
      object-fit:cover; 
      margin-bottom:20px; 
      transition:transform 0.6s;
    }
    img.profile:hover {transform:scale(1.08);}

    footer {
      padding:40px;
      text-align:center;
      font-size:16px;
      color:#64748b;
    }
    
    @media (max-width: 768px) {
        nav { display: none; } /* Simple hide for mobile for this demo */
        section { padding: 40px 15px; }
        h1 { font-size: 42px; }
    }
  </style>
</head>
<body>
  <nav>
    <a href="#home">Home</a>
    <a href="#profile">Profile</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#education">Education</a>
    <a href="#experience">Experience</a>
  </nav>

  <section id="home">
    <img src="{{ url_for('static', filename='profile.jpg') }}" class="profile" alt="Profile Picture">
    <h1>{{p.name}}</h1>
    <p style="font-size:24px; color:#38bdf8;">{{p.title}}</p>
    <p class="text-center">{{p.location}}<br>
    <a href="mailto:{{p.email}}" style="color:#f1f5f9; text-decoration: underline;">{{p.email}}</a> • {{p.phone}}</p>
  </section>

  <section id="profile">
    <h2>Profile</h2>
    <p class="text-center" style="max-width: 800px;">{{p.profile}}</p>
  </section>

  <section id="skills">
    <h2>Technical Skills</h2>
    {% for cat in p.skills_categorized %}
      <div class="skill-category">
        <h4>{{ cat.category }}</h4>
        <div>
            {% for item in cat['items'] %}
                <span class="chip">{{ item }}</span>
            {% endfor %}
        </div>
      </div>
    {% endfor %}
    
    <div style="margin-top: 40px; text-align: center;">
        <h4>Languages & Additional</h4>
        {% for l in p.languages %}<span class="chip" style="background: #38bdf8; color: #0f172a;">{{l}}</span>{% endfor %}
        {% for info in p.additional_info %}<span class="chip" style="background: #38bdf8; color: #0f172a;">{{info}}</span>{% endfor %}
    </div>
  </section>

  <section id="projects">
    <h2>Technical Projects</h2>
    {% for proj in p.projects %}
      <div class="card">
          <h3 style="color:#38bdf8;">{{proj.title}}</h3>
          <ul>
            {% for item in proj["items"] %}
              <li>{{item}}</li>
            {% endfor %}
          </ul>
      </div>
    {% endfor %}
  </section>

  <section id="education">
    <h2>Education</h2>
    {% for e in p.education %}
      <div class="card" style="text-align: center;">
          <h3 style="color:#f1f5f9; margin-bottom: 5px;">{{e.degree}}</h3>
          <p style="color:#38bdf8; margin-top:0;">{{e.institution}} | {{e.dates}}</p>
          {% if e.notes %}
            <p style="font-size:16px; color:#94a3b8; margin-top:10px;">{{e.notes}}</p>
          {% endif %}
      </div>
    {% endfor %}
  </section>

  <section id="experience">
    <h2>Professional Experience</h2>
    {% for ex in p.experience %}
      <div class="card">
        <h3>{{ex.role}} <span style="font-weight:400; font-size:18px; color:#94a3b8;">at {{ex.company}}</span></h3>
        <p style="font-size:14px; margin-top:-10px; margin-bottom:15px; color:#38bdf8;">{{ex.dates}}</p>
        <ul>
            {% for h in ex.highlights %}
              <li>{{h}}</li>
            {% endfor %}
        </ul>
      </div>
    {% endfor %}

    <h2 style="margin-top: 40px;">Leadership</h2>
    {% for l in p.leadership %}
      <div class="card">
        <h3>{{l.role}} <span style="font-weight:400; font-size:18px; color:#94a3b8;">— {{l.org}}</span></h3>
        <ul>
            {% for h in l.highlights %}<li>{{h}}</li>{% endfor %}
        </ul>
      </div>
    {% endfor %}
  </section>

  <footer>
    <p>© {{p.name}} — Portfolio Website</p>
  </footer>

  <script>
    const sections = document.querySelectorAll("section");
    const observer = new IntersectionObserver((entries)=>{
      entries.forEach(entry=>{
        if(entry.isIntersecting){ entry.target.classList.add("visible"); }
      });
    }, {threshold:0.15});
    sections.forEach(sec=>observer.observe(sec));
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    has_cv = os.path.exists(portfolio['cv_path'])
    return render_template_string(TEMPLATE, p=portfolio, has_cv=has_cv)

@app.route('/download-cv')
def download_cv():
    if os.path.exists(portfolio['cv_path']):
        folder, filename = os.path.split(portfolio['cv_path'])
        return send_from_directory(folder, filename, as_attachment=True)
    else:
        return "CV file not found on the server.", 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)