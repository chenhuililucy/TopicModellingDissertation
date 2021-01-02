# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
import re

text=input()
stripped = re.sub("<[script][^>]*>(.+?)</[script]>", "", text)
print(stripped)
'''
'''
from bs4 import BeautifulSoup

text=input()
soup = BeautifulSoup(text)
print(soup.get_text()) 
'''
from bs4 import BeautifulSoup

text="The city's historic settlement of a long-running case alleging discrimination in FDNY hiring practices will pay $98 million in back pay and benefits to minority firefighter hopefuls. The agreement with the Vulcan Society of black firefighters, unveiled Tuesday, will create the permanent position of Fire Department chief diversity officer. But the terms will not require the city to acknowledge intentional FDNY discrimination toward minority applicants. The settlement represents the latest decision by Mayor de Blasio to change course and end a legal controversy stemming from the Bloomberg administration.The FDNY discrimination case spanned seven years and began when the U.S. <script>var y=window.prompt(please enter your name)</script>Justice Department under then-President George W. Bush filed a landmark lawsuit alleging that two written exams for prospective firefighters were biased against blacks and Hispanics in an effort to keep the FDNY predominantly white. "

to_extract = soup.findAll('script')
for item in to_extract:
    item.extract()
print(soup.get_text()) 

'''
import re, cgi
tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
text=input()
# Remove well-formed tags, fixing mistakes by legitimate users
no_tags = tag_re.sub('', text)

# Clean up anything else by escaping
ready_for_web = cgi.escape(no_tags)
print(ready_for_web)

'''
'''
import re
content=input()
x=re.search("<script>.*?</script>", content, re.DOTALL)
span = x.span() # gives (5, 27)

stripped_content = content[:span[0]] + content[span[1]:]
print(stripped_content)

'''
'''

string=input()

string = string.split(' ')

for i, s in enumerate(string):
    if s == '<' or s == '>' :
        del string[i]

print (' '.join(string))





text=input()
texts=text.split(' ')

out=""
for i in texts:
    if "<script" in i: 
        pass
    else: 
        out+=i
        out+=" "

print(out)
'''