import re

text = '''
start
Here is a line
end
start
and here is some more
end'''

match = re.findall(r'(?<=start).*?(?=end)', text, flags=re.DOTALL)



