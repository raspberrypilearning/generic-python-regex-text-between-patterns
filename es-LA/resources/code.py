import re

text = '''
start
Aquí hay una línea
end
start
y aquí hay otra
end'''

match = re.findall(r'(?<=start).*?(?=end)', text, flags=re.DOTALL)



