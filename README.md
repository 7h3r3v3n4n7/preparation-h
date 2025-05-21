# Domain Extractor for Port Scanning

This script extracts unique domain names from a list of URLs to prepare input for a port scanner (e.g., `nmap`). It removes protocols (`http`, `https`), strips `www.` subdomains, and ensures the output list contains only unique domain names.

## 📄 Input Format

A plain text file (`target_urls.txt` by default) containing one URL per line:

```
https://www.example.com/page  
http://api.example.com/data?id=1  
https://www.example.com/another  
```

## ✅ Output

A sorted list of unique domain names (excluding `www.`), saved to `targets.txt`:

```
api.example.com  
example.com  
```

## 🚀 Usage

1. Save your list of URLs in a file named `target_urls.txt` (or change the filename in the script).
2. Run the script:

   ```bash
   python3 prepare.py
   ```

3. The output will be saved to `targets.txt`.

## 🧠 Notes

- The script ignores URL paths, parameters, and fragments.
- Domains are deduplicated based on hostname (excluding `www.`).
- Only valid hostnames are included in the final output.

## 🛠 Dependencies

- Python 3 (no external libraries needed)
