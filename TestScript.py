from datetime import datetime

# CONFIG - Set GitHub username and repo name
GITHUB_USERNAME = "rohinipatil-dev"
REPO_NAME = "AgentXTest"
FILE_NAME = "welcome.html"

# Generate simple HTML content
html_content = f"""
<html>
<head><title>AutoThinker Test</title></head>
<body>
    <h1>Report Generated</h1>
    <p>Timestamp: {datetime.now()}</p>
    <p>Welcome to AutoThinker AI</p>
</body>
</html>
"""

# Save HTML file
with open(FILE_NAME, "w") as f:
    f.write(html_content)

# Construct the GitHub Pages URL
public_url = f"https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/{FILE_NAME}"

print(f"✅ Report generated: {FILE_NAME}")
print(f"🌐 View it here: {public_url}")
