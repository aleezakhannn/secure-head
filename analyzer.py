import requests
import ipaddress
import socket

security_headers = [
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Content-Security-Policy",
    "Referrer-Policy",
    "Permissions-Policy"
]

def is_safe_url(url):
    try:
        domain = url.replace("https://", "").replace("http://", "").split("/")[0]
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        return "invalid"  # site doesn't exist / can't be found
    
    ip_obj = ipaddress.ip_address(ip)
    if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local:
        return "blocked"
    return "safe"


def check_headers(url):
    if not url.startswith("http"):
        url = "https://" + url
    
    safety = is_safe_url(url)
    if safety == "blocked":
        return "unsafe"
    if safety == "invalid":
        return "error"
    
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        return "error"
    
    found_headers = response.headers
    
    results = []
    for header in security_headers:
        if header in found_headers:
            results.append((header, True))
        else:
            results.append((header, False))
    
    return results

def calculate_score(results):
    total = len(results)
    found = sum(1 for header, present in results if present)
    
    percentage = (found / total) * 100
    
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 25:
        grade = "D"
    else:
        grade = "F"
    
    return percentage, grade

# Test it
if __name__ == "__main__":
    data = check_headers("instagram.com")
    for header, present in data:
        status = "✅ Found" if present else "❌ Missing"
        print(header, "-", status)

    percentage, grade = calculate_score(data)
    print("\nScore:", round(percentage), "%  |  Grade:", grade)