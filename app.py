from flask import Flask, render_template_string, send_from_directory, url_for
import os

app = Flask(__name__)

portfolio = {
    "name": "Omar Elsharoud",
    "title": "Software Engineering Graduate | Aspiring Software Developer",
    "location": "Cardiff, Wales, CF3 6YP",
    "email": "f.elsharoud@gmail.com",
    "phone": "+44 7881 851872",

    "profile": (
        "Motivated and detail-oriented Software Engineering graduate with a strong foundation in the "
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
            "dates": "Sept 2023 – 06/2026",
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
            "title": "Dar Ul Isra Website (darulisra.org.uk)",
            "items": [
                "Developed and maintain the official community website (darulisra.org.uk) using WordPress, serving as a central digital hub for the local community.",
                "Integrated dynamic functionality including automated prayer timetables, event management calendars, and secure donation gateways.",
                "Optimized the UI/UX for accessibility, mobile responsiveness, and SEO, ensuring critical community information is easily accessible to a diverse user base."
            ]
        },
        {
            "title": "AccomFix – Full-Stack Property Management System",
            "items": [
                "Developed a full-stack web application using the LAMP stack (PHP, MySQL, HTML/CSS/JS) to streamline maintenance reporting and triage in the student housing sector.",
                "Engineered a custom 'Link Code' multi-tenancy architecture, enabling secure, frictionless onboarding between independent landlords and tenant clusters.",
                "Implemented a priority-based ticketing workflow featuring secure multipart file uploads for visual evidence and a real-time, AJAX-driven live messaging system.",
                "Designed a role-based administrative dashboard utilizing SQL aggregate functions for real-time issue analytics, status management, and CSV data exportation.",
                "Enforced strict web security best practices, utilizing Bcrypt for password hashing and PDO prepared statements to mitigate SQL injection vulnerabilities."
            ]
        },
        {
            "title": "CampusTasker – Full-Stack Web Application",
            "items": [
                "Engineered a full-stack, localized micro-job marketplace using PHP, MySQL, JavaScript, HTML, and CSS to connect community residents with university students.",
                "Integrated third-party APIs (Postcodes.io and Leaflet.js) using PHP cURL to build an interactive spatial mapping system that dynamically geocodes locations and calculates real-time distances between users and tasks.",
                "Designed a secure, relational database schema and implemented PDO prepared statements to prevent SQL injection vulnerabilities, alongside robust error-handling for API timeouts.",
                "Built an asynchronous, peer-to-peer messaging system and dynamic marketplace filters using the JavaScript Fetch API, enabling real-time UI updates and data polling without full-page reloads.",
                "Applied the POST/Redirect/GET (PRG) architectural pattern to ensure secure state management and prevent duplicate database entries during form submissions."
            ]
        },
        {
            "title": "QuizCraft – Full-Stack Quiz Management Platform (PHP, MySQL, Vanilla JS, HTML5, CSS3)",
            "items": [
                "Developed a dynamic, custom MVC-architected web application that enables users to create, publish, and evaluate interactive quizzes.",
                "Designed a normalized relational database schema using PDO to securely manage users, complex quiz structures, dynamic multiple-choice options, and submission data.",
                "Engineered advanced quiz flow logic, including conditional branching (allowing distinct 'next question' paths based on user selection) and automated grading systems.",
                "Built a highly interactive front-end utilizing Vanilla JavaScript for real-time DOM manipulation, enabling users to dynamically add, edit, and remove form elements without page reloads.",
                "Secured the application with robust, session-based user authentication, state management, and prepared SQL statements to prevent injection vulnerabilities.",
                "Created a centralized creator dashboard to manage content and review user submissions, featuring side-by-side comparisons of submitted text answers against defined model answers."
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

    "skills_categorized": [
        {
            "category": "Languages & Web",
            "items": ["Python", "Java", "PHP", "JavaScript", "HTML", "CSS", "SQL (MySQL)", "WordPress"]
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
            "role": "Youth Program Coordinator / Lead Youth Mentor",
            "org": "Community Youth Program",
            "highlights": [
                "Designed and implemented a comprehensive 3-year educational and development curriculum for distinct youth demographics (ages 7–18).",
                "Facilitated weekly 2-hour interactive sessions focusing on historical studies, strategic analysis, character building, and community ethics.",
                "Mentored young adults through complex social and moral topics, fostering personal accountability, resilience, and critical thinking skills.",
                "Adapted advanced historical texts into engaging narratives, coordinated program logistics, and cultivated a safe, inclusive environment for leadership development."
            ]
        },
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

    "cv_path": os.path.join(os.getcwd(), 'Omar_Elsharoud_CV.docx')
}

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{{p.name}} — Portfolio</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">

  <style>
    body {
      font-family: 'Outfit', sans-serif; 
      margin:0; 
      background:#0f172a; 
      color:#f1f5f9; 
      line-height:1.6; 
      scroll-behavior:smooth;
      font-size: 20px; 
    }

    section {
      min-height: 60vh; 
      display:flex; 
      flex-direction:column; 
      justify-content:center; 
      align-items:center; 
      padding: 120px 20px 40px; /* Increased top padding so fixed nav doesn't overlap content */
      
      opacity: 0; 
      transform: translateY(80px);
      transition: opacity 0.8s ease-out, transform 0.8s ease-out;
      
      max-width: 1100px;
      margin: 0 auto;
    }

    section.visible {
      opacity: 1; 
      transform: translateY(0);
    }

    h1 {
      font-size: 80px; 
      font-weight: 800; 
      margin-bottom: 20px;
      text-align: center;
      background: linear-gradient(to right, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    h2 {
      font-size: 48px; 
      font-weight: 700; 
      margin-bottom: 40px;
      color: #38bdf8;
      border-bottom: 3px solid #38bdf8;
      padding-bottom: 10px;
      text-align: center;
    }

    h3 {
      font-size: 28px;
      color: #e2e8f0;
      margin-top: 0;
      margin-bottom: 15px;
      font-weight: 600;
    }

    p, li {
      font-size: 20px; 
      color: #cbd5e1;
      font-weight: 300;
    }

    .text-center { text-align: center; }
    
    nav {
      position:fixed; 
      top:20px; 
      left:50%; 
      transform:translateX(-50%);
      display:flex; 
      flex-wrap: wrap;
      justify-content: center;
      gap:25px; 
      background:rgba(15, 23, 42, 0.85); 
      backdrop-filter: blur(12px);
      padding:15px 30px; 
      border-radius:50px; 
      border: 1px solid rgba(255,255,255,0.1);
      box-shadow:0 10px 30px rgba(0,0,0,0.5);
      z-index:1000;
      max-width: 90%;
    }
    nav a {
      color:#f1f5f9; 
      text-decoration:none; 
      font-size:18px; 
      font-weight:500; 
      transition:color 0.3s;
    }
    nav a:hover {
      color:#38bdf8;
    }
    
    .card {
        background: #1e293b;
        padding: 30px;
        border-radius: 20px;
        margin-bottom: 25px;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #334155;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-sizing: border-box; 
    }

    .card:hover {
        transform: translateY(-8px); 
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
        border-color: #38bdf8;
    }
    
    ul { padding-left:25px; }
    ul li { margin:10px 0; }
    
    .skill-category {
      width: 100%;
      margin-bottom: 30px;
      text-align: center;
    }
    .skill-category h4 {
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 14px;
        margin-bottom: 15px;
        font-weight: 600;
    }
    .chip {
      display:inline-block;
      padding:10px 20px;
      border-radius:999px;
      background:#334155;
      margin:6px;
      font-size:18px;
      font-weight:500;
      transition: all 0.3s;
      border: 1px solid #475569;
    }
    .chip:hover {
        background: #38bdf8;
        color: #0f172a;
        transform: scale(1.05);
    }

    img.profile {
      width:240px; 
      height:240px; 
      border-radius:50%; 
      border:8px solid #38bdf8;
      object-fit:cover; 
      margin-bottom:30px; 
      box-shadow: 0 0 40px rgba(56, 189, 248, 0.3);
      transition: transform 0.5s;
    }
    img.profile:hover {
        transform: scale(1.05) rotate(2deg);
    }

    footer {
      padding:60px 20px;
      text-align:center;
      font-size:18px;
      color:#64748b;
    }
    
    /* MOBILE FIXES */
    @media (max-width: 768px) {
        nav { 
            width: 95%; /* Makes the nav spread across the screen */
            max-width: 100%;
            gap: 12px; 
            padding: 12px 10px;
            border-radius: 20px; /* Forms a wider pill rather than a squashed square */
            top: 15px;
        }
        nav a {
            font-size: 15px; 
        }
        section { 
            padding: 140px 15px 40px; /* Pushes content far down to avoid the multi-line mobile nav */
            min-height: auto; 
        }
        h1 { font-size: 48px; }
        h2 { font-size: 36px; }
        .card { padding: 20px; }
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
    <p style="font-size:28px; color:#38bdf8; font-weight: 500; text-align: center;">{{p.title}}</p>
    <p class="text-center">{{p.location}}<br>
    <a href="mailto:{{p.email}}" style="color:#f1f5f9; text-decoration: underline;">{{p.email}}</a> • {{p.phone}}</p>
  </section>

  <section id="profile">
    <h2>Profile</h2>
    <p class="text-center" style="max-width: 900px; line-height: 1.8;">{{p.profile}}</p>
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
          <h3 style="color:#38bdf8;">
            {% if proj.title == "Dar Ul Isra Website (darulisra.org.uk)" %}
              <a href="https://darulisra.org.uk" target="_blank" style="color:inherit; text-decoration:none;">{{proj.title}} ↗</a>
            {% else %}
              {{proj.title}}
            {% endif %}
          </h3>
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
          <p style="color:#38bdf8; margin-top:0; font-weight:600;">{{e.institution}} | {{e.dates}}</p>
          {% if e.notes %}
            <p style="font-size:18px; color:#94a3b8; margin-top:10px;">{{e.notes}}</p>
          {% endif %}
      </div>
    {% endfor %}
  </section>

  <section id="experience">
    <h2>Professional Experience</h2>
    {% for ex in p.experience %}
      <div class="card">
        <h3>{{ex.role}} <span style="font-weight:400; font-size:20px; color:#94a3b8;">at {{ex.company}}</span></h3>
        <p style="font-size:16px; margin-top:-10px; margin-bottom:15px; color:#38bdf8; font-weight:600;">{{ex.dates}}</p>
        <ul>
            {% for h in ex.highlights %}
              <li>{{h}}</li>
            {% endfor %}
        </ul>
      </div>
    {% endfor %}

    <h2 style="margin-top: 60px;">Leadership</h2>
    {% for l in p.leadership %}
      <div class="card">
        <h3>{{l.role}} <span style="font-weight:400; font-size:20px; color:#94a3b8;">— {{l.org}}</span></h3>
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
    document.addEventListener("DOMContentLoaded", function() {
        const sections = document.querySelectorAll("section");
        
        if (sections.length > 0) {
            const observer = new IntersectionObserver((entries) => {
              entries.forEach(entry => {
                if (entry.isIntersecting) { 
                    entry.target.classList.add("visible"); 
                }
              });
            }, {
                threshold: 0.02, 
                rootMargin: "50px" 
            });

            sections.forEach(sec => observer.observe(sec));
        }
    });
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