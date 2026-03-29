"""
extract_pypi_maintainer_emails.py
author: timsonner.com
Program that extracts package maintainer/author emails from PyPI packages by fetching the simple index and then querying each package's metadata.
Errors are silent (no output for packages that fail or have no email).
example output:
somepackagename: maintainer@contoso.com
"""

import random
import requests

# Configuration
URL = "https://pypi.org/simple/"

# User agents for rotation
USER_AGENTS = [
    # Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    # macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0",
    # Linux
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
]


def get_random_ua():
    return random.choice(USER_AGENTS)


def fetch_package_index():
    """Fetch the PyPI simple index page."""
    headers = {"User-Agent": get_random_ua()}
    try:
        response = requests.get(URL, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching package index: {e}")
        return None


def extract_package_names(html_content):
    """
    Extract package names from the simple index HTML.
    The simple index is an HTML list of <a href="...">packagename</a> entries.
    """
    package_names = []
    for line in html_content.splitlines():
        package_name = line[line.find(">") + 1:line.rfind("<")]
        package_names.append(package_name)
    return package_names


def extract_maintainer_email(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    headers = {"User-Agent": get_random_ua()}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        info = data.get("info", {})
        # Prefer maintainer_email, then author_email
        email = info.get("maintainer_email") or info.get("author_email")
        if email != "UNKNOWN":
            return email
        else:
            return None
    except Exception:
        # Silent failure: return None for any error
        return None


def main():
    # Fetch package index
    html = fetch_package_index()
    if html is None:
        print("main(): Failed to fetch the package index.")
        return

    # Extract package names
    packages = extract_package_names(html)
    if not packages:
        print("main(): No package names found in package index.")
        return

    # Extract package maintainer emails from each package and print results
    count = 0
    for pkg in packages:
        email = extract_maintainer_email(pkg)
        if email:
            print(f"{pkg}: {email}")
        count += 1

if __name__ == "__main__":
    main()
