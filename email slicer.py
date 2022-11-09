def email_sclicer(s):
    i=s.index("@")
    return  s[:i],s[i+1:]

email=input("Enter yout email: ")

if "@" in email:
    username,domain=email_sclicer(email)
    print(f"username: {username} and domain: {domain}")
else:
    print("enter correct email")