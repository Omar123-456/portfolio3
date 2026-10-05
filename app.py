from flask import Flask, render_template_string, send_from_directory, url_for
import os

app = Flask(__name__)

portfolio = {
    "name": "Omar El-Sharoud",
    "title": "Software Engineer",
    "location": "Cardiff, Wales, CF3 6YP",
    "email": "f.elsharoud@gmail.com",
    "phone": "+44 7881 851872",

    "profile": (
        "Motivated and detail-orientated Software Engineer with a strong foundation spanning the "
        "Full Software Development Lifecycle (SDLC). Possesses robust practical experience delivering "
        "complex, database-driven software projects across both academic and independent settings. Proficient in "
        "Microsoft Windows Platform development, with a solid structural understanding of OS architecture, system "
        "services, and security features. A proven technical leader skilled at implementing secure systems and "
        "executing comprehensive unit, integration, and regression testing pipelines. Seeking a software "
        "engineering opportunity to apply technical expertise within a fast-paced, innovative environment."
    ),

    "education": [
        {
            "degree": "BSc (Hons) Software Engineering",
            "institution": "Cardiff Metropolitan University",
            "dates": "Sept 2023 – Graduate (06/2026)",
            "notes": "Relevant Modules: Operating Systems & Architecture, Advanced Object-Orientated Programming, Database Management Systems, Systems Analysis & Design."
        },
        {
            "degree": "A-Levels & Equivalents",
            "institution": "Cardiff High School",
            "dates": "Sept 2018 – June 2022",
            "notes": "Subjects Covered: Mathematics, ICT, Physics, Chemistry, Biology, Design & Technology, Business Studies."
        }
    ],

    "projects": [
        {
            "title": "Bayan Academy Website",
            "items": [
                "Built the official website and online registration system for Bayan Academy (Salam Centre, Cardiff) in PHP and MySQL, with a bilingual English and Arabic public site covering pathways, courses, timetable, fees calculator and FAQ.",
                "Integrated online card payments for registration and a family payment link for outstanding balances, with server-side pricing, webhooks that record payments even if the payer never returns, and automatic confirmation of each payment with the provider's API.",
                "Implemented the fee rules (per-term, annual and monthly Direct Debit options, family and multi-course discounts, promo codes) with a daily cron job for fee entries, payment reminders and an office digest.",
                "Created a staff area where the Director and teachers manage registrations, payments, promo codes, the course catalogue, emails and the site's wording without touching code."
            ]
        },
        {
            "title": "Dar Ul Isra Platform",
            "items": [
                "Developed and continue to maintain the official website of Dar Ul Isra mosque and community centre (darulisra.org.uk) on WordPress as the sole technical lead, serving a large, diverse community: live prayer times, programmes and events, services, room booking and online donations.",
                "Built a multi-step Youth Halaqas registration (ages 7-18) capturing child, parent/guardian, emergency, medical and photography-consent details, with age and gender grouping, several children per submission, a waiting list, and Stripe payment so card details are never handled by the mosque.",
                "Built the Iqraa Quran School registration for up to three students per family, recording Quran reading level, guardian and emergency contacts, medical details and consent with a typed digital signature.",
                "Optimised the site for accessibility, mobile responsiveness and technical SEO, and supported the community's mobile app for prayer times and event notifications."
            ]
        },
        {
            "title": "WhatsApp AI Automation SaaS",
            "items": [
                "Built a multi-tenant SaaS platform using Node.js, Express, PostgreSQL, and Docker that connects seamlessly to WhatsApp Web to automate intelligent, context-aware replies powered by the Google Gemini API.",
                "Engineered persistent, Puppeteer-based session management with compressed database-backed archival, enabling flawless WhatsApp connectivity across container rebuilds without requiring user re-authentication.",
                "Designed a multi-group monitoring system featuring per-chat AI persona overrides, a one-tap web-scraping knowledge pipeline, and an automated availability calendar engine with iCal export functionality for autonomous scheduling.",
                "Containerised and deployed the entire infrastructure via Docker Compose to Hugging Face Spaces with automated CI/CD pipelines, featuring a mobile-responsive telemetry dashboard and secure JWT/Bcrypt authentication."
            ]
        },
        {
            "title": "Align",
            "items": [
                "Founded and built Align, a halal, privacy-first Muslim marriage platform live on Google Play (App Store in review) and on the web, as a solo full-stack and mobile engineer. Stack: Express and SQLite API, Expo / React Native member app for iOS, Android and browser, and a React 19 + Vite web client for the website, wali portal, community-centre portal and admin console.",
                "Designed a multi-journey psychometric assessment (40+ adaptive screens with conditional branching) feeding a weighted compatibility engine with dealbreaker filtering, bidirectional scoring and cold-start handling.",
                "Built a privacy-first member experience: staged photo reveal (blurred and silhouette variants generated server-side), voice notes and in-app voice/video calls via Agora, AES-256 encryption of sensitive PII, JWT authentication, Google/Apple sign-in and face-detection liveness verification.",
                "Delivered separate wali and community-centre portals, including a native centre portal in the app with an interview and vetting workflow, certificates and member requests, plus an admin console, moderation and ban-appeal tooling.",
                "Implemented subscriptions and a match-acceptance paywall with in-app purchases on mobile and Stripe on the web, plus gift cards, push notifications (FCM/APNs) and multi-language localisation including Arabic.",
                "Shipped through Fly.io with persistent SQLite replicated by Litestream and GitHub Actions CI/CD where a push to main is a release; supported by Vitest unit tests, Playwright end-to-end tests and written security, data-protection and launch-readiness reviews."
            ]
        },
        {
            "title": "AccomFix",
            "items": [
                "Developed a full-stack web application utilising the LAMP stack (PHP, MySQL, Apache, HTML/CSS/JS) to streamline automated maintenance reporting and triage workflows within the student housing sector.",
                "Engineered a custom 'Link Code' multi-tenancy architecture, guaranteeing secure, frictionless onboarding and total data isolation between independent landlords and tenant clusters.",
                "Implemented a priority-based ticketing workflow featuring secure multipart file uploads for visual evidence alongside a real-time, AJAX-driven live messaging system.",
                "Designed a role-based administrative dashboard leveraging SQL aggregate functions for real-time issue analytics, status management, and automated CSV data exportation.",
                "Enforced strict web security best practices, deploying Bcrypt for password hashing and PDO prepared statements to completely mitigate SQL injection vulnerabilities."
            ]
        },
        {
            "title": "CampusTasker",
            "items": [
                "Engineered a localised peer-to-peer web marketplace using PHP, MySQL, and Vanilla JavaScript designed to connect community residents with university students for local tasks.",
                "Integrated third-party spatial APIs (Postcodes.io and Leaflet.js) using PHP cURL to build an interactive mapping system that dynamically geocodes locations and calculates real-time distances.",
                "Designed a secure, relational database schema implementing robust error-handling for API timeouts and comprehensive data validation.",
                "Built an asynchronous messaging system and dynamic marketplace filters using the JavaScript Fetch API, enabling real-time DOM polling and UI updates without full-page reloads.",
                "Applied the POST/Redirect/GET (PRG) architectural pattern to ensure secure state management and prevent duplicate database entries during form submissions."
            ]
        },
        {
            "title": "QuizCraft",
            "items": [
                "Developed a dynamic, custom MVC-architected web application enabling users to build, publish, and evaluate highly interactive educational quizzes.",
                "Designed a normalised relational database schema using PDO to securely manage users, complex relational quiz structures, dynamic multiple-choice arrays, and submission logs.",
                "Engineered advanced quiz flow logic, including automated grading engines and conditional branching paths based on real-time user selections.",
                "Built a highly interactive front-end utilising Vanilla JavaScript for real-time DOM manipulation, allowing users to dynamically alter form elements seamlessly."
            ]
        },
        {
            "title": "Mental Health Support Platform",
            "items": [
                "Oversaw the entire development lifecycle from initial requirement gathering through to deployment, managing task delegation within an Agile framework.",
                "Developed a secure web application with robust user authentication frameworks, session tracking, and encrypted database hashing.",
                "Conducted rigorous unit testing on booking algorithms and security modules to guarantee data integrity and system stability."
            ]
        }
    ],

    "skills_categorized": [
        {
            "category": "Enterprise & Cloud (OGI)",
            "items": ['Microsoft Power Platform (Power Apps, Power Automate, Dataverse)', 'Dynamics 365 Customer Service', 'Model-Driven Apps', 'Azure DevOps & CI/CD', 'Microsoft Azure', 'Microsoft Entra ID', 'SharePoint Online', 'REST API Integrations', 'Billing & Finance System Integrations', 'Dynamics 365 Plugin Development', 'React', 'Node.js', 'PostgreSQL', 'Solution Architecture', 'Requirements Gathering', 'UAT & Production Deployments', 'Technical Documentation & Handover Creation', 'Business Process Automation']
        },
        {
            "category": "Languages & Web",
            "items": ["Python", "Java", "PHP", "JavaScript", "SQL (MySQL, PostgreSQL)", "HTML", "CSS", "WordPress"]
        },
        {
            "category": "Windows Ecosystem",
            "items": ["Windows OS Architecture", "System Services", "Frameworks", "Security Features"]
        },
        {
            "category": "DevOps & Tools",
            "items": ["Git", "GitHub (Branching, Pull Requests, Version Control)", "Docker", "Docker Compose", "CI/CD Pipelines", "Cisco Packet Tracer"]
        },
        {
            "category": "Methodologies & Testing",
            "items": ["Agile (Scrum)", "Full SDLC Management", "Unit Testing", "Integration & System Testing", "Advanced Debugging"]
        },
        {
            "category": "Security & Compliance",
            "items": ["Data Hashing (Bcrypt, SHA)", "Secure Session Management", "PDO Prepared Statements", "GDPR Awareness"]
        }
    ],

    "experience": [
        {
            "role": "Web Developer Intern",
            "company": "OGI",
            "dates": "2026",
            "summary": 'Web Developer Intern with experience delivering enterprise business solutions using Microsoft Power Platform, Dynamics 365, Azure, SharePoint and custom web applications. Contributed to large-scale projects including annual recurring billing automation, Dynamics customer-service enhancements, warehouse operations ticketing, contract-import integrations and the AssetTrack asset management platform. Experienced in Power Apps, Power Automate, Dataverse, Azure DevOps CI/CD, REST API integrations, Azure hosting, technical documentation and solution deployment across development, UAT and production environments.',
            "projects": [
                {"title": 'Annual Recurring Billing', "role": 'Power Platform / Dynamics Developer', "desc": "Helped bring annual recurring billing to OGI's Dynamics environment, covering renewals, annual contract handling and pricing. Reworked the pricing logic and product synchronisation, updated the Power Automate flows and Dynamics plugins, and connected everything to the BillingBooth API, with JavaScript web resources on the front end. Also handled testing and deployment planning.", "tech": ['Dynamics 365', 'Dataverse', 'Power Automate', 'BillingBooth API', 'JavaScript', 'Azure DevOps', 'Power Platform Solutions']},
                {"title": 'IP Allocation Visibility in Dynamics', "role": 'Dynamics 365 Developer', "desc": "Built a way for customer service teams to see a customer's Fixed IPv4 and Routed Subnet allocations directly in Dynamics 365. Added the new fields, updated the forms and customer records, wrote the high-level design document, and tested the solution through to UAT and production.", "tech": ['Dynamics 365', 'Dataverse', 'Model-Driven Apps', 'Solution Management', 'UAT Testing']},
                {"title": 'Warehouse Ticketing System', "role": 'Power Platform Developer', "desc": "Designed and delivered an end-to-end ticketing system for the warehouse team: ticket submission, automatic numbering, confirmation emails, status updates and SharePoint integration. Wrote the test plans, deployed to UAT, then took it through the release pipeline to production, delivering the warehouse team's follow-up change requests along the way.", "tech": ['SharePoint Online', 'Power Apps', 'Power Automate', 'Dataverse', 'Azure DevOps', 'CI/CD Pipelines']},
                {"title": 'PSI Fusion Contract Import', "role": 'Power Platform Developer', "desc": 'Built an integration that pulls thousands of PDF contract records from PSI Fusion into Dataverse using Power Automate, with a one-off bulk migration followed by automated daily imports of new and changed records. Includes duplicate prevention, metadata management and error handling, plus a model-driven app for finding and opening the documents.', "tech": ['Power Automate', 'Dataverse', 'Model-Driven Apps', 'REST APIs', 'JSON']},
                {"title": 'AssetTrack', "role": 'Full Stack Developer', "desc": 'Developed AssetTrack, an internal platform for tracking engineering assets and certifications. Includes engineer, manager and admin roles, expiry tracking and certification management, with authentication and security controls built in.', "tech": ['React', 'Node.js', 'Express', 'PostgreSQL', 'Microsoft Entra ID', 'Azure DevOps']},
                {"title": 'AssetTrack Azure Migration', "role": 'Cloud & Application Developer', "desc": 'Planned and drove the move of AssetTrack from local Docker infrastructure to Azure. Designed the Azure architecture, role-based access model, database migration approach and Entra ID authentication, and wrote the security documentation, VPN access requirements and deployment policies.', "tech": ['Azure App Service', 'Azure PostgreSQL', 'Azure Key Vault', 'Entra ID', 'Docker', 'VPN & Networking']},
                {"title": 'Dynamics 365 Plugin & Solution Development', "role": 'Dynamics Developer', "desc": 'Developed and tested Dynamics plugins and solutions covering customer service records, pricing, product synchronisation, order processing and billing integrations, and released them through Azure DevOps pipelines as managed solutions into UAT and production.', "tech": ['Dynamics 365', 'C# Plugins', 'Dataverse', 'Azure DevOps', 'Managed Solutions']},
                {"title": 'Power Platform CI/CD & Environments', "role": 'Power Platform Developer', "desc": 'Managed the solution lifecycle across Development, UAT and Production: deployments, connection references, environment variables, managed and unmanaged solutions, and Azure DevOps release pipelines.', "tech": ['Power Platform', 'Azure DevOps', 'Connection References', 'Environment Variables']},
            ]
        },
        {
            "role": "Administrative Assistant",
            "company": "HMRC",
            "dates": "Sept 2022 – Sept 2023",
            "highlights": [
                "Managed high-volume customer queries, applying highly structured, analytical problem-solving methodologies mirroring software debugging workflows.",
                "Processed sensitive data in strict accordance with compliance frameworks and data protection legislation, mirroring backend security practices.",
                "Developed exceptional skills in process optimisation, systematic troubleshooting, and delivering accurate results under tight operational pressure."
            ]
        }
    ],

    "leadership": [
        {
            "role": "Youth Programme Coordinator & Lead Mentor",
            "org": "Community Hub (Sept 2024 – Present)",
            "highlights": [
                "Designed and implemented a comprehensive three-year educational and development curriculum tailored for distinct youth demographics.",
                "Facilitated weekly interactive sessions focusing on strategic analysis, character building, historical studies, and community ethics.",
                "Mentored young adults through complex social topics, actively fostering personal accountability, resilience, and critical thinking skills.",
                "Adapted advanced historical texts into engaging, accessible narratives while successfully coordinating project logistics and managing volunteer teams."
            ]
        },
        {
            "role": "Scout Leader",
            "org": "The Scouts Association (Ongoing)",
            "highlights": [
                "Organised and led large-scale camps and expeditions, taking full responsibility for risk assessments, safety protocols, and complex logistics.",
                "Mentored youth members to foster teamwork, resilience, and practical problem-solving capabilities.",
                "Successfully transferred these leadership skills into technical settings by guiding software development teams, setting clear objectives, and delegating development tasks effectively."
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
  <title>{{p.name}} | Portfolio</title>
  
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
      padding: 120px 20px 40px;
      
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
      transition: transform 0.3s ease-in-out;
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
    
    @media (max-width: 768px) {
        nav { 
            width: 90%;
            max-width: 100%;
            gap: 12px; 
            padding: 12px 10px;
            border-radius: 20px;
            top: 15px;
        }
        
        nav.nav-hidden {
            transform: translate(-50%, -150%);
        }
        
        nav a {
            font-size: 15px; 
        }
        section { 
            padding: 140px 15px 40px;
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
            {% if proj.title == "Dar Ul Isra Platform" %}
              <a href="https://darulisra.org.uk" target="_blank" style="color:inherit; text-decoration:none;">{{proj.title}} ↗</a>
            {% elif proj.title == "WhatsApp AI Automation SaaS" %}
              <a href="https://omar123-456-whattsappbot.hf.space/" target="_blank" style="color:inherit; text-decoration:none;">{{proj.title}} ↗</a>
            {% elif proj.title == "Align" %}
              <a href="https://align-marrige-app.fly.dev/" target="_blank" style="color:inherit; text-decoration:none;">{{proj.title}} <span style="font-size: 16px; color: #94a3b8; font-weight: 400; font-style: italic;">(Under Development)</span> ↗</a>
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
        {% if ex.summary %}<p style="font-size:18px; color:#cbd5e1;">{{ex.summary}}</p>{% endif %}
        {% if ex.highlights %}
        <ul>
            {% for h in ex.highlights %}
              <li>{{h}}</li>
            {% endfor %}
        </ul>
        {% endif %}
        {% for pr in ex.projects or [] %}
          <div style="border-top:1px solid #334155; margin-top:20px; padding-top:15px;">
            <h4 style="margin:0; color:#f1f5f9;">{{pr.title}}</h4>
            <p style="font-size:16px; margin:4px 0 10px; color:#38bdf8; font-weight:600;">{{pr.role}}</p>
            <p style="font-size:17px; color:#cbd5e1; margin:0 0 10px;">{{pr.desc}}</p>
            <p style="font-size:15px; color:#94a3b8; margin:0;"><strong>Technologies:</strong> {{ pr.tech | join(' · ') }}</p>
          </div>
        {% endfor %}
      </div>
    {% endfor %}

    <h2 style="margin-top: 60px;">Leadership & Volunteering</h2>
    {% for l in p.leadership %}
      <div class="card">
        <h3>{{l.role}} <span style="font-weight:400; font-size:20px; color:#94a3b8;">| {{l.org}}</span></h3>
        <ul>
            {% for h in l.highlights %}<li>{{h}}</li>{% endfor %}
        </ul>
      </div>
    {% endfor %}
  </section>

  <footer>
    <p>© {{p.name}} | Portfolio Website</p>
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

        let lastScrollTop = 0;
        const nav = document.querySelector('nav');

        window.addEventListener('scroll', function() {
            let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            if (window.innerWidth <= 768) {
                if (scrollTop > lastScrollTop && scrollTop > 60) {
                    nav.classList.add('nav-hidden');
                } else {
                    nav.classList.remove('nav-hidden');
                }
            } else {
                nav.classList.remove('nav-hidden');
            }
            
            lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; 
        });
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