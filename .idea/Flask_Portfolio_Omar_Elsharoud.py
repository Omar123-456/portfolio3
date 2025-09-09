from flask import Flask, render_template_string, send_from_directory, url_for
import os

app = Flask(__name__)


portfolio = {
    "name": "Omar Elsharoud",
    "title": "Software Engineering Student | Software Developer",
    "location": "Cardiff, Wales, CF3 6YP",
    "email": "o.elsharoud@gmail.com",
    "phone": "+44 7881 851872",

    "profile": (
        "Motivated and detail-oriented Software Engineering student with strong practical experience "
        "delivering software projects in both academic and independent settings. Proven ability to lead "
        "teams, design intuitive user interfaces, implement secure systems, and fine-tune AI solutions. "
        "Knowledgeable in Agile methodology and DevOps practices with hands-on networking experience using Cisco Packet Tracer. "
        "Skilled in handling sensitive data, problem-solving under pressure, and delivering user-focused solutions. "
        "Currently seeking a graduate opportunity to apply and grow technical expertise within a fast-paced, innovative environment."
    ),

    "education": [
        {
            "degree": "BSc (Hons) Software Engineering",
            "institution": "Cardiff Metropolitan University",
            "dates": "Sept 2023 – Present"
        },
        {
            "degree": "A-Levels & Equivalent",
            "institution": "Cardiff High School",
            "dates": "Sept 2018 – June 2022",
            "notes": (
                "Subjects: Mathematics, Chemistry, Physics, ICT, Biology, Design & Technology, "
                "Business, English Language, English Literature, Arabic, Welsh, Skills Challenge"
            )
        }
    ],

    "projects": [
        {
            "title": "Welsh Museums Mobile App",
            "items": [
                "Designed and implemented UI/UX independently, ensuring accessibility and bilingual (English/Welsh) support.",
                "Integrated Google Maps API for location and street view functionality.",
                "Built a user-friendly digital resource hub to enhance cultural engagement."
            ]
        },
        {
            "title": "Caravan Rental Website (Team Project – Lead Developer)",
            "items": [
                "Led a small team to build a dynamic rental website using PHP, JavaScript, and SQL.",
                "Implemented a featured slider to highlight available rentals.",
                "Applied early knowledge of databases and back-end logic, laying foundations for advanced booking systems."
            ]
        },
        {
            "title": "Medical Chatbot for NHS Triage",
            "items": [
                "Developed a web-based chatbot powered by AI APIs, trained and fine-tuned to provide accurate triage guidance.",
                "Configured custom filters and training loops to minimise inappropriate responses.",
                "Conducted iterative testing to refine accuracy and ensure patient safety."
            ]
        },
        {
            "title": "Mental Health Support Platform (Team Project – Project Lead)",
            "items": [
                "Oversaw design and development of a mental health support platform with secure SQL database and hashed authentication.",
                "Implemented booking system for therapy sessions and personal mood tracking.",
                "Custom-trained the AI chatbot to respond sensitively and ethically to mental health queries."
            ]
        }
    ],

    "networking_security": (
        "Hands-on practical experience with networking and cybersecurity principles "
        "using Cisco Packet Tracer, including configuration, troubleshooting, and secure design."
    ),

    "experience": [
        {
            "role": "Admin Assistant",
            "company": "HMRC",
            "dates": "Sept 2022 – Present",
            "highlights": [
                "Managed high-volume customer queries under pressure, applying structured problem-solving similar to debugging software.",
                "Processed and safeguarded sensitive financial data in line with compliance frameworks, mirroring secure software engineering practices.",
                "Developed strong attention to detail, process optimisation, and resilience in high-stakes environments."
            ]
        },
        {
            "role": "Customer Assistant",
            "company": "Tesco",
            "dates": "June 2022 – Aug 2022",
            "highlights": [
                "Delivered frontline customer support with a user-first mindset.",
                "Collaborated in agile teams to resolve issues efficiently, reflecting agile workflows in tech environments."
            ]
        },
        {
            "role": "Charity Volunteer",
            "company": "Local Distribution Warehouse",
            "dates": "Various",
            "highlights": [
                "Supported logistics and distribution for local charities in a fast-paced warehouse setting.",
                "Strengthened teamwork, resilience, and problem-solving under time constraints."
            ]
        }
    ],

    "leadership": [
        {
            "role": "Scout Leader",
            "org": "Scouts Association (Ongoing)",
            "highlights": [
                "Organised and led multiple camps and hikes, ensuring safety and logistics for groups.",
                "Mentored children in outdoor and team-based activities, building resilience and collaboration.",
                "Transferred leadership skills into technical project settings, guiding development teams effectively."
            ]
        }
    ],

    "skills": [
        "Python", "Java", "PHP", "JavaScript", "HTML", "CSS", "MySQL", "Android development",
        "Microsoft Office", "DevOps fundamentals (CI/CD, version control, deployment awareness)",
        "Agile methodology (Scrum teamwork, sprint planning, iterative development)",
        "Networking & cybersecurity (Cisco Packet Tracer, secure configurations)",
        "Data security practices (hashing, GDPR compliance, data protection)",
    ],

    "languages": ["English (fluent)", "Arabic (fluent)"],

    "additional_info": [
        "Full UK Driving License (since Oct 2021)",
        "Amateur photographer — edit and publish work on social media",
        "Strong interest in AI, cybersecurity, and scalable web applications"
    ],

    "cv_path": os.path.join(os.getcwd(), 'Omar_Elsharoud_CV 2026.docx')
}


# ---- New interactive template ----
TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{{p.name}} — Portfolio</title>
  <style>
    body {
      font-family: 'Inter', Arial, sans-serif;
      margin:0; 
      background:#0f172a; 
      color:#f1f5f9; 
      line-height:1.8; 
      scroll-behavior:smooth;
    }
    section {
      min-height:100vh; 
      display:flex; 
      flex-direction:column; 
      justify-content:center; 
      align-items:center; 
      padding:80px 20px;
      opacity:0; 
      transform:translateY(50px);
      transition: all 1s ease-out;
    }
    section.visible {
      opacity:1; 
      transform:translateY(0);
    }
    h1 {
      font-size:64px; 
      font-weight:800; 
      margin-bottom:20px;
    }
    h2 {
      font-size:42px; 
      font-weight:700; 
      margin-bottom:20px;
      color:#38bdf8;
    }
    p, li {
      font-size:22px;
      max-width:900px;
      text-align:center;
    }
    nav {
      position:fixed; 
      top:20px; 
      left:50%; 
      transform:translateX(-50%);
      display:flex; 
      gap:20px; 
      background:#1e293b; 
      padding:12px 24px; 
      border-radius:12px; 
      box-shadow:0 4px 20px rgba(0,0,0,0.5);
      z-index:1000;
    }
    nav a {
      color:#f1f5f9; 
      text-decoration:none; 
      font-size:18px; 
      font-weight:600; 
      transition:color 0.3s;
    }
    nav a:hover {
      color:#38bdf8;
    }
    ul {list-style: none; padding:0;}
    ul li {margin:10px 0;}
    .chip {
      display:inline-block;
      padding:12px 18px;
      border-radius:999px;
      background:#1e293b;
      margin:6px;
      font-size:18px;
      font-weight:600;
      transition:transform 0.3s;
    }
    .chip:hover {transform:scale(1.1);}
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
      font-size:18px;
      color:#94a3b8;
    }
  </style>
</head>
<body>
  <nav>
    <a href="#home">Home</a>
    <a href="#profile">Profile</a>
    <a href="#education">Education</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#skills">Skills</a>
    <a href="#leadership">Leadership</a>
  </nav>

  <section id="home">
    <img src="{{ url_for('static', filename='profile.jpg') }}" class="profile">
    <h1>{{p.name}}</h1>
    <p style="font-size:28px;">{{p.title}}</p>
    <p>{{p.location}} • <a href="mailto:{{p.email}}" style="color:#38bdf8">{{p.email}}</a> • {{p.phone}}</p>
  </section>

  <section id="profile">
    <h2>Profile</h2>
    <p>{{p.profile}}</p>
  </section>

  <section id="education">
    <h2>Education</h2>
    {% for e in p.education %}
      <p><strong>{{e.degree}}</strong> — {{e.institution}} ({{e.dates}})</p>
      {% if e.notes %}<p style="font-size:20px;color:#94a3b8">{{e.notes}}</p>{% endif %}
    {% endfor %}
  </section>

  <section id="projects">
    <h2>Technical Projects</h2>
    {% for proj in p.projects %}
      <p><strong>{{proj.title}}</strong></p>
      <ul>
        {% for item in proj["items"] %}
          <li>{{item}}</li>
        {% endfor %}
      </ul>
    {% endfor %}
  </section>

  <section id="experience">
    <h2>Professional Experience</h2>
    {% for ex in p.experience %}
      <p><strong>{{ex.role}}</strong> — {{ex.company}} ({{ex.dates}})</p>
      <ul>
        {% for h in ex.highlights %}
          <li>{{h}}</li>
        {% endfor %}
      </ul>
    {% endfor %}
  </section>



  <section id="leadership">
    <h2>Leadership & Volunteering</h2>
    {% for l in p.leadership %}
      <p><strong>{{l.role}}</strong> — {{l.org}}</p>
      <ul>
        {% for h in l.highlights %}<li>{{h}}</li>{% endfor %}
      </ul>
    {% endfor %}
  </section>
  
    <section id="skills">
    <h2>Skills & Additional Info</h2>
    <div>
      {% for s in p.skills %}<span class="chip">{{s}}</span>{% endfor %}
    </div>
    <div style="margin-top:20px">
      {% for l in p.languages %}<span class="chip">{{l}}</span>{% endfor %}
    </div>
    <div style="margin-top:20px">
      {% for add in p.additional_info %}<p>{{add}}</p>{% endfor %}
    </div>
  </section>

  <footer>
    <p>© {{p.name}} — Portfolio Website</p>
  </footer>

  <script>
    // scroll animation
    const sections = document.querySelectorAll("section");
    const observer = new IntersectionObserver((entries)=>{
      entries.forEach(entry=>{
        if(entry.isIntersecting){ entry.target.classList.add("visible"); }
      });
    }, {threshold:0.2});
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

from Flask_Portfolio_Omar_Elsharoud import app as application

