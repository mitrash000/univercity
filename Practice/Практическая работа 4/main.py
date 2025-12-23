import re
import csv
import ssl
import urllib.request

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
response = urllib.request.urlopen(url)
html_content = response.read().decode("utf-8")


pattern = r'(?:<a[^>]+class[^>]+>)(?P<name>[^<]+)(?:[^(]+location">)(?P<address>[^<]+)(?:([^>]+>){4,9}\s)(?:[^>]+>)(?P<phone>[^<]+)(?:<\/dd>)(?:([^>]+>){4,7}\s)(?:[^>]+>)(?P<hours>[^<]+)(?:<\/dd>)(?:[^<a])'

all_matches = []
matches = re.finditer(pattern, html_content)

for match in matches:
    all_matches.append(match)
print(matches)


with open('data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Phone', 'Hours'])
    
    for match in all_matches:
       
        name = (match.group('name')).strip()
        address = (match.group('address')).strip()
        phone = (match.group('phone')).strip()
        hours = (match.group('hours')).strip()
        
        writer.writerow([name, address, phone, hours])



for match in all_matches:
    print("name:", match.group('name').strip())
    print("address:", match.group('address').strip())
    print("phone:", match.group('phone').strip())
    print("hours:", match.group('hours').strip())
    print("\n")

if not all_matches:
    print("No match found.")
