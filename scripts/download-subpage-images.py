#!/usr/bin/env python3
import urllib.request
import os
import sys

# High quality curated Unsplash photo IDs precisely matching tech/software/data/domain themes
SERVICES_IMAGES = {
    'data-engineering': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1000&auto=format&fit=crop&q=80', # server racks, data pipelines
    'data-extraction-etl': 'https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=1000&auto=format&fit=crop&q=80', # data flows & digital streams
    'data-visualization': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1000&auto=format&fit=crop&q=80', # business analytics dashboards & charts
    'data-mining-management': 'https://images.unsplash.com/photo-1518186285589-2f7649de83e0?w=1000&auto=format&fit=crop&q=80', # digital data pattern mining
    'desktop-software': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=1000&auto=format&fit=crop&q=80', # coding desktop application workstation
    'machine-learning': 'https://images.unsplash.com/photo-1677442136019-21780efad99a?w=1000&auto=format&fit=crop&q=80', # AI machine learning neural concepts
    'mobile-development': 'https://images.unsplash.com/photo-1526406915894-7bcd65f60845?w=1000&auto=format&fit=crop&q=80', # mobile app development smartphones
    'on-demand-systems': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1000&auto=format&fit=crop&q=80', # tailored agile systems & technology
    'web-development': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1000&auto=format&fit=crop&q=80', # modern web development code & screen
    'small-language-models': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=1000&auto=format&fit=crop&q=80', # local AI model chip & silicon intelligence
    'vector-databases': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1000&auto=format&fit=crop&q=80', # vector matrix data points & high dimensional
    'chatbots': 'https://images.unsplash.com/photo-1531746790731-6c087fecd65a?w=1000&auto=format&fit=crop&q=80', # AI virtual assistant conversational interface
    'neural-networks': 'https://images.unsplash.com/photo-1509228468518-180dd4864904?w=1000&auto=format&fit=crop&q=80', # deep learning nodes & connected network
    'advanced-analytics': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1000&auto=format&fit=crop&q=80', # predictive market trends & financial analytics
    'asset-management': 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1000&auto=format&fit=crop&q=80', # warehouse inventory asset management tracking
    'enterprise-automation': 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1000&auto=format&fit=crop&q=80', # industrial & workflow automated technology
    'business-operations': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1000&auto=format&fit=crop&q=80', # enterprise team operations & strategy
    'cloud-computing': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=80', # global cloud infrastructure network
    'servers-computing': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1000&auto=format&fit=crop&q=80', # high performance server hardware & compute
    'devops': 'https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=1000&auto=format&fit=crop&q=80', # CI/CD continuous deployment git code
    'it-automation': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=80', # IT system automation circuits
    'middleware': 'https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1000&auto=format&fit=crop&q=80' # API integration middleware interconnect
}

SOLUCIONES_IMAGES = {
    'vulnerabilities': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?w=1000&auto=format&fit=crop&q=80', # cybersecurity shield lock monitor
    'seismic-monitoring': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1000&auto=format&fit=crop&q=80', # real-time seismic waves sensors geology
    'sports-results': 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=1000&auto=format&fit=crop&q=80', # sports stadium scores athletics
    'sales-analytics': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1000&auto=format&fit=crop&q=80', # sales dashboard analytics revenue growth
    'radio-streaming': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=1000&auto=format&fit=crop&q=80', # radio broadcast microphone audio console
    'telemedicine': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1000&auto=format&fit=crop&q=80', # virtual health doctor stethoscope digital tablet
    'ticketing': 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=1000&auto=format&fit=crop&q=80', # concert event tickets booking audience
    'odoo-erp': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1000&auto=format&fit=crop&q=80', # enterprise ERP management planning laptop
    'wordpress-plugins': 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=1000&auto=format&fit=crop&q=80', # CMS website extensions and web design
    'iot': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=80', # IoT smart sensors microcontrollers
    'medicine-prices': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=1000&auto=format&fit=crop&q=80', # pharmacy medicine pills pharmacy catalog
    'openclaw': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1000&auto=format&fit=crop&q=80', # digital open crawler automated data extractor
    'barbershop-booking': 'https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1000&auto=format&fit=crop&q=80', # barbershop haircut appointment chair
    'facial-cleaning': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=1000&auto=format&fit=crop&q=80', # spa beauty facial treatment aesthetic care
    'lms-moodle': 'https://images.unsplash.com/photo-1501504905252-473c47e087f8?w=1000&auto=format&fit=crop&q=80', # online learning education virtual classroom
    'laundry-rentals': 'https://images.unsplash.com/photo-1545173168-9f1947eebb7f?w=1000&auto=format&fit=crop&q=80' # modern laundry washers rental equipment
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

def download_item(folder, slug, url):
    dest = f'public/images/{folder}/{slug}.jpg'
    if os.path.exists(dest) and os.path.getsize(dest) > 5000:
        print(f'Already exists: {dest}')
        return
    print(f'Downloading {slug} -> {dest} ...')
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f'Done: {dest} ({os.path.getsize(dest)} bytes)')
    except Exception as e:
        print(f'Error downloading {slug}: {e}', file=sys.stderr)

for slug, url in SERVICES_IMAGES.items():
    download_item('servicios', slug, url)

for slug, url in SOLUCIONES_IMAGES.items():
    download_item('soluciones', slug, url)

print("All downloads finished.")
