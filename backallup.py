#!/usr/bin/env python3
import json
import os
import subprocess
import cyberpanel_backup

def main():
    # Execute the cyberpanel command and capture its output
    output = subprocess.getoutput("cyberpanel listWebsitesJson")

    # Try to parse the JSON output
    try:
        websites = json.loads(output)
        websites = json.loads(websites)
        
        for website in websites:
            domain = website['domain']
            if domain:
                print(f"Backing up {domain}")
                cyberpanel_backup.newBackup(domain)
                
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return


if __name__ == "__main__":
    main()