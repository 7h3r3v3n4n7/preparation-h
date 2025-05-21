from urllib.parse import urlparse

input_file = "target_urls.txt"
output_file = "targets.txt"

domains = set()

with open(input_file, "r") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        parsed = urlparse(line)
        domain = parsed.hostname or ''
        if domain.startswith('www.'):
            domain = domain[4:]
        if domain:
            domains.add(domain)

with open(output_file, "w") as outfile:
    for domain in sorted(domains):
        outfile.write(domain + "\n")

print(f"Wrote {len(domains)} unique domains to '{output_file}'")
