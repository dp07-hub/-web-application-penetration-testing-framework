🛡️ Web Application Penetration Testing Framework
A Flask-based security scanner that detects common web vulnerabilities like XSS, SQL Injection, CSRF, missing HTTP security headers, and hidden directories.
Includes a login page, colorful UI, and export options (PDF/CSV) for scan results.

🚀 Features
🔐 Login page (default credentials)

🌐 URL scanning via web interface

🧪 Vulnerability detection:

Reflected XSS

Basic SQL Injection

CSRF form detection

Missing HTTP Security Headers

Directory brute-force with wordlist

📤 Export scan results as PDF or CSV

🎨 Stylish, responsive user interface

🧩 Easy to extend (modular core)

🖥️ Demo Screenshot

📁 Folder Structure
pgsql
Copy
Edit
web_pentest_framework_flask/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── login.html
│   └── index.html
├── core/
│   ├── header_checker.py
│   ├── xss_scanner.py
│   ├── sqli_scanner.py
│   ├── csrf_scanner.py
│   └── dir_bruteforce.py
├── utils/
│   ├── export_pdf.py
│   └── export_csv.py
└── wordlist.txt
🛠️ Installation
✅ 1. Clone and Set Up
bash
Copy
Edit
unzip web_pentest_framework_flask_export_enabled.zip
cd web_pentest_framework_flask
✅ 2. Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
✅ 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ 4. Run the App
bash
Copy
Edit
python app.py
🔑 Default Login Credentials
Username	Password
admin	pass123

You can change these in app.py.

🌐 Access the App
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
📤 Export Options
After scanning, click:

Export as PDF → Generates scan_report.pdf

Export as CSV → Generates scan_report.csv

These files are saved in the current working directory.

🔧 Future Enhancements (Optional)
👥 User registration & role-based access

📊 Scan history with timestamp

🌙 Dark mode toggle

🔄 Scan progress indicator

📦 Packaging as .exe or .deb

📜 License
This project is open-source and free to use for educational and ethical testing purposes.
