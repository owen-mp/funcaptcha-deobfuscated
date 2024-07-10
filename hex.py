import re
f = open('funcaptcha_api.js', 'r').read()

def replace(match):
    return str(int(match.group(0), 16))

regex = r"0x[a-z0-9]+"
reg = re.sub(regex, replace, f)

f = open('funcaptcha_api.js', 'w').write(reg)
