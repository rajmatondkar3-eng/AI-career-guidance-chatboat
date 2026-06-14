# career_data.py
# This file contains all career information used by the app.
# Each career is a dictionary with details like skills, salary, resources, etc.

CAREERS = {
    "Data Scientist": {
        "description": "Analyzes large datasets to extract insights and build predictive models.",
        "skills": ["Python", "Statistics", "Machine Learning", "SQL", "Data Visualization"],
        "salary_range": "₹6,00,000 - ₹25,00,000 / year",
        "certifications": ["Google Data Analytics", "IBM Data Science", "Microsoft Azure Data Scientist"],
        "resources": ["Coursera - Data Science Specialization", "Kaggle Learn", "Fast.ai"],
        "interview_questions": [
            "What is the difference between supervised and unsupervised learning?",
            "Explain overfitting and how to prevent it.",
            "What is a p-value?",
            "How do you handle missing data?",
            "Explain the bias-variance tradeoff."
        ],
        "growth": "Senior Data Scientist -> Lead Data Scientist -> Chief Data Officer"
    },
    "Web Developer": {
        "description": "Builds and maintains websites and web applications.",
        "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
        "salary_range": "₹3,00,000 - ₹15,00,000 / year",
        "certifications": ["Meta Front-End Developer", "FreeCodeCamp Certifications", "AWS Developer Associate"],
        "resources": ["MDN Web Docs", "FreeCodeCamp", "The Odin Project"],
        "interview_questions": [
            "What is the difference between var, let, and const?",
            "Explain the box model in CSS.",
            "What is REST API?",
            "How does React's virtual DOM work?",
            "What is asynchronous JavaScript?"
        ],
        "growth": "Junior Developer -> Senior Developer -> Tech Lead -> Engineering Manager"
    },
    "AI/ML Engineer": {
        "description": "Designs and deploys machine learning models and AI systems.",
        "skills": ["Python", "Deep Learning", "TensorFlow", "PyTorch", "Mathematics"],
        "salary_range": "₹8,00,000 - ₹30,00,000 / year",
        "certifications": ["TensorFlow Developer Certificate", "Deep Learning Specialization (Andrew Ng)"],
        "resources": ["DeepLearning.AI", "PyTorch Tutorials", "Papers with Code"],
        "interview_questions": [
            "Explain backpropagation.",
            "What is a convolutional neural network?",
            "Difference between RNN and LSTM?",
            "What is transfer learning?",
            "Explain gradient descent."
        ],
        "growth": "ML Engineer -> Senior ML Engineer -> AI Architect -> AI Research Lead"
    },
    "Cybersecurity Analyst": {
        "description": "Protects systems and networks from cyber threats and attacks.",
        "skills": ["Networking", "Linux", "Ethical Hacking", "Cryptography", "SIEM Tools"],
        "salary_range": "₹4,00,000 - ₹18,00,000 / year",
        "certifications": ["CompTIA Security+", "CEH", "CISSP"],
        "resources": ["TryHackMe", "Cybrary", "HackTheBox"],
        "interview_questions": [
            "What is a firewall?",
            "Explain the difference between symmetric and asymmetric encryption.",
            "What is a DDoS attack?",
            "What is two-factor authentication?",
            "Explain SQL injection."
        ],
        "growth": "Security Analyst -> Security Engineer -> Security Architect -> CISO"
    },
    "Cloud Engineer": {
        "description": "Manages cloud infrastructure and services for organizations.",
        "skills": ["AWS", "Azure", "Docker", "Kubernetes", "Linux"],
        "salary_range": "₹5,00,000 - ₹22,00,000 / year",
        "certifications": ["AWS Solutions Architect", "Azure Administrator", "Google Cloud Engineer"],
        "resources": ["AWS Training", "A Cloud Guru", "Kubernetes Docs"],
        "interview_questions": [
            "What is the difference between IaaS, PaaS, and SaaS?",
            "Explain how auto-scaling works.",
            "What is a container?",
            "Explain VPC in AWS.",
            "What is Infrastructure as Code?"
        ],
        "growth": "Cloud Engineer -> Senior Cloud Engineer -> Cloud Architect -> Cloud Solutions Director"
    },
    "Mobile App Developer": {
        "description": "Builds applications for Android and iOS platforms.",
        "skills": ["Java", "Kotlin", "Swift", "Flutter", "UI/UX Design"],
        "salary_range": "₹3,50,000 - ₹16,00,000 / year",
        "certifications": ["Google Associate Android Developer", "Apple Developer Certification"],
        "resources": ["Android Developer Docs", "Flutter Docs", "Ray Wenderlich"],
        "interview_questions": [
            "What is the activity lifecycle in Android?",
            "Explain state management in Flutter.",
            "What is the difference between native and hybrid apps?",
            "How do you handle app performance optimization?",
            "What is MVVM architecture?"
        ],
        "growth": "App Developer -> Senior Developer -> Mobile Architect -> Mobile Team Lead"
    },
    "Business Analyst": {
        "description": "Bridges the gap between business needs and technical solutions.",
        "skills": ["Excel", "SQL", "Communication", "Data Analysis", "Power BI"],
        "salary_range": "₹4,00,000 - ₹14,00,000 / year",
        "certifications": ["CBAP", "PMI-PBA", "Microsoft Power BI Certification"],
        "resources": ["Coursera Business Analysis", "Udemy BA Courses", "BA Times"],
        "interview_questions": [
            "What is SWOT analysis?",
            "How do you gather requirements from stakeholders?",
            "What is a use case diagram?",
            "Explain the difference between functional and non-functional requirements.",
            "What tools do you use for data analysis?"
        ],
        "growth": "Business Analyst -> Senior BA -> Product Manager -> Director of Strategy"
    },
    "DevOps Engineer": {
        "description": "Automates and streamlines software development and deployment.",
        "skills": ["CI/CD", "Docker", "Kubernetes", "Linux", "Scripting"],
        "salary_range": "₹6,00,000 - ₹24,00,000 / year",
        "certifications": ["Docker Certified Associate", "CKA (Kubernetes)", "AWS DevOps Engineer"],
        "resources": ["KodeKloud", "DevOps Roadmap", "Jenkins Docs"],
        "interview_questions": [
            "What is CI/CD?",
            "Explain the difference between Docker and Kubernetes.",
            "What is a Jenkins pipeline?",
            "How do you handle configuration management?",
            "What is blue-green deployment?"
        ],
        "growth": "DevOps Engineer -> Senior DevOps Engineer -> DevOps Architect -> Platform Lead"
    },
    "UI/UX Designer": {
        "description": "Designs user-friendly interfaces and experiences for products.",
        "skills": ["Figma", "Adobe XD", "Wireframing", "User Research", "Prototyping"],
        "salary_range": "₹3,00,000 - ₹14,00,000 / year",
        "certifications": ["Google UX Design Certificate", "Adobe Certified Professional"],
        "resources": ["Figma Academy", "Nielsen Norman Group", "Interaction Design Foundation"],
        "interview_questions": [
            "What is the difference between UI and UX?",
            "Explain the design thinking process.",
            "What is a wireframe?",
            "How do you conduct user research?",
            "What is a usability test?"
        ],
        "growth": "UX Designer -> Senior UX Designer -> UX Lead -> Head of Design"
    },
    "Database Administrator": {
        "description": "Manages and maintains organizational databases for performance and security.",
        "skills": ["SQL", "Database Design", "Backup & Recovery", "Performance Tuning", "Oracle/MySQL"],
        "salary_range": "₹4,00,000 - ₹16,00,000 / year",
        "certifications": ["Oracle Certified DBA", "Microsoft SQL Server Certification"],
        "resources": ["Oracle University", "SQL Zoo", "MySQL Documentation"],
        "interview_questions": [
            "What is normalization?",
            "Explain ACID properties.",
            "What is indexing and why is it important?",
            "How do you perform database backup and recovery?",
            "What is a deadlock?"
        ],
        "growth": "DBA -> Senior DBA -> Database Architect -> Data Infrastructure Manager"
    },
    "Network Engineer": {
        "description": "Designs, implements, and maintains computer networks.",
        "skills": ["Networking", "Cisco", "Routing & Switching", "Firewalls", "TCP/IP"],
        "salary_range": "₹3,50,000 - ₹15,00,000 / year",
        "certifications": ["CCNA", "CCNP", "CompTIA Network+"],
        "resources": ["Cisco Networking Academy", "Packet Tracer Labs", "Network+ Study Guides"],
        "interview_questions": [
            "What is the OSI model?",
            "Explain the difference between TCP and UDP.",
            "What is subnetting?",
            "What is VLAN?",
            "Explain how DNS works."
        ],
        "growth": "Network Engineer -> Senior Network Engineer -> Network Architect -> IT Infrastructure Head"
    },
    "Product Manager": {
        "description": "Oversees product development from conception to launch.",
        "skills": ["Strategy", "Communication", "Agile", "Market Research", "Roadmapping"],
        "salary_range": "₹8,00,000 - ₹30,00,000 / year",
        "certifications": ["Certified Scrum Product Owner", "Product Management Certificate (PMI)"],
        "resources": ["Product School", "Reforge", "Mind the Product"],
        "interview_questions": [
            "How do you prioritize features?",
            "Explain how you would launch a new product.",
            "What metrics do you track for product success?",
            "How do you handle conflicting stakeholder requests?",
            "Describe your experience with Agile methodology."
        ],
        "growth": "Associate PM -> Product Manager -> Senior PM -> VP of Product"
    },
    "Game Developer": {
        "description": "Designs and builds video games for various platforms.",
        "skills": ["C++", "Unity", "Unreal Engine", "Game Design", "3D Modeling"],
        "salary_range": "₹3,50,000 - ₹15,00,000 / year",
        "certifications": ["Unity Certified Developer", "Unreal Engine Certification"],
        "resources": ["Unity Learn", "Unreal Engine Docs", "GameDev.tv"],
        "interview_questions": [
            "Explain the game loop.",
            "What is the difference between Unity and Unreal Engine?",
            "How do you optimize game performance?",
            "What is collision detection?",
            "Explain object pooling."
        ],
        "growth": "Game Developer -> Senior Developer -> Lead Game Designer -> Creative Director"
    },
    "Digital Marketing Specialist": {
        "description": "Plans and executes online marketing campaigns to grow brand presence.",
        "skills": ["SEO", "Social Media Marketing", "Content Marketing", "Google Analytics", "PPC"],
        "salary_range": "₹2,50,000 - ₹12,00,000 / year",
        "certifications": ["Google Digital Marketing Certificate", "HubSpot Content Marketing", "Meta Blueprint"],
        "resources": ["Google Skillshop", "HubSpot Academy", "Moz SEO Guide"],
        "interview_questions": [
            "What is SEO and why is it important?",
            "Explain the difference between organic and paid traffic.",
            "What is a conversion rate?",
            "How do you measure campaign success?",
            "What is A/B testing?"
        ],
        "growth": "Marketing Specialist -> Marketing Manager -> Head of Marketing -> CMO"
    },
    "Blockchain Developer": {
        "description": "Develops decentralized applications and smart contracts.",
        "skills": ["Solidity", "Blockchain Concepts", "Smart Contracts", "Cryptography", "Web3.js"],
        "salary_range": "₹6,00,000 - ₹25,00,000 / year",
        "certifications": ["Certified Blockchain Developer", "Ethereum Developer Certification"],
        "resources": ["CryptoZombies", "Ethereum Docs", "Solidity Documentation"],
        "interview_questions": [
            "What is a smart contract?",
            "Explain how a blockchain works.",
            "What is the difference between public and private blockchains?",
            "What is gas in Ethereum?",
            "Explain consensus mechanisms."
        ],
        "growth": "Blockchain Developer -> Senior Developer -> Blockchain Architect -> CTO"
    },
    "QA/Test Engineer": {
        "description": "Ensures software quality through systematic testing processes.",
        "skills": ["Manual Testing", "Automation Testing", "Selenium", "Test Case Design", "Bug Tracking"],
        "salary_range": "₹3,00,000 - ₹12,00,000 / year",
        "certifications": ["ISTQB Certification", "Certified Selenium Tester"],
        "resources": ["ISTQB Syllabus", "Selenium Docs", "Test Automation University"],
        "interview_questions": [
            "What is the difference between manual and automation testing?",
            "Explain the software testing life cycle.",
            "What is regression testing?",
            "How do you write a test case?",
            "What is the difference between smoke and sanity testing?"
        ],
        "growth": "QA Engineer -> Senior QA Engineer -> Test Lead -> QA Manager"
    },
    "IT Support Specialist": {
        "description": "Provides technical support and troubleshooting for IT systems.",
        "skills": ["Troubleshooting", "Operating Systems", "Networking Basics", "Customer Service", "Hardware"],
        "salary_range": "₹2,00,000 - ₹8,00,000 / year",
        "certifications": ["CompTIA A+", "ITIL Foundation", "Microsoft Certified IT Professional"],
        "resources": ["CompTIA Resources", "ITIL Foundation Course", "TechTerms"],
        "interview_questions": [
            "How do you troubleshoot a slow computer?",
            "What is the difference between hardware and software issues?",
            "Explain the ticketing system process.",
            "How do you handle a frustrated user?",
            "What is remote desktop support?"
        ],
        "growth": "IT Support -> System Administrator -> IT Manager -> IT Director"
    },
    "Data Engineer": {
        "description": "Builds and maintains data pipelines and infrastructure for analytics.",
        "skills": ["Python", "SQL", "ETL", "Apache Spark", "Data Warehousing"],
        "salary_range": "₹6,00,000 - ₹22,00,000 / year",
        "certifications": ["Google Cloud Data Engineer", "AWS Data Analytics Certification"],
        "resources": ["DataCamp", "Apache Spark Docs", "Designing Data-Intensive Applications (book)"],
        "interview_questions": [
            "What is ETL?",
            "Explain the difference between a data lake and a data warehouse.",
            "What is Apache Spark used for?",
            "How do you ensure data quality?",
            "Explain partitioning in big data systems."
        ],
        "growth": "Data Engineer -> Senior Data Engineer -> Data Architect -> Head of Data Engineering"
    },
    "Embedded Systems Engineer": {
        "description": "Develops software for embedded hardware and IoT devices.",
        "skills": ["C", "C++", "Microcontrollers", "RTOS", "Circuit Design"],
        "salary_range": "₹4,00,000 - ₹16,00,000 / year",
        "certifications": ["Certified Embedded Systems Professional", "ARM Accredited Engineer"],
        "resources": ["Embedded.com", "Arduino Docs", "FreeRTOS Documentation"],
        "interview_questions": [
            "What is an RTOS?",
            "Explain the difference between microprocessor and microcontroller.",
            "What is interrupt handling?",
            "How do you debug embedded systems?",
            "Explain memory-mapped I/O."
        ],
        "growth": "Embedded Engineer -> Senior Embedded Engineer -> Firmware Architect -> Hardware Engineering Lead"
    },
    "Technical Writer": {
        "description": "Creates documentation, manuals, and guides for technical products.",
        "skills": ["Writing", "Markdown", "API Documentation", "Research", "Editing Tools"],
        "salary_range": "₹3,00,000 - ₹10,00,000 / year",
        "certifications": ["Certified Professional Technical Communicator (CPTC)"],
        "resources": ["Google Technical Writing Courses", "Write the Docs", "Grammarly"],
        "interview_questions": [
            "How do you simplify complex technical concepts?",
            "What tools do you use for documentation?",
            "How do you structure an API document?",
            "Explain your editing and review process.",
            "How do you handle feedback from engineers?"
        ],
        "growth": "Technical Writer -> Senior Technical Writer -> Documentation Lead -> Content Strategy Manager"
    }
}

# List of all unique skills across all careers (used in profile form)
ALL_SKILLS = sorted(list(set(skill for career in CAREERS.values() for skill in career["skills"])))

# List of all career names
CAREER_NAMES = list(CAREERS.keys())
