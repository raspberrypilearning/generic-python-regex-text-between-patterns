import re

tekst = '''
start
Hier is een regel
einde
start
en hier is nog wat meer
einde'''

match = re.findall(r'(?<=start).*?(?=einde)', tekst, flags=re.DOTALL)



