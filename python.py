import re
import pdfkit

with open('../Downloads/sitemaps/urllist.txt') as f:
    websites = f.readlines()

websites = [x.strip() for x in websites]
options ={
    'javascript-delay': 30000
}

for site in websites:
    name = site.rsplit('/', 1)[-1]
    name = re.sub(r'\.html$', '', name)
    name = re.sub(r'[.]', '-', name)
    if name is '': name='home'

    pdfkit.from_url(site, f'all2/{name}.pdf', options=options)