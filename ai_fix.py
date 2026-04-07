# ai_fix.py (no API key version)

def get_fix(log):
    return "Fix: You forgot quotes → use print('Hello')"

log = "NameError: name 'Hello' is not defined"

fix = get_fix(log)
print("AI Suggestion:\n", fix)