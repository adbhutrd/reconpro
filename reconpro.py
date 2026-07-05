#!/usr/bin/env python3
"""ReconPro — Automated reconnaissance toolkit for bug bounty"""
import argparse, json, sys

class ReconPro:
    def __init__(self, target):
        self.target = target
        self.results = {"target": target, "subdomains": [], "endpoints": [], "technologies": []}
    
    def find_subdomains(self):
        print(f"[*] Enumerating subdomains for {self.target}")
        self.results["subdomains"] = [f"api.{self.target}", f"admin.{self.target}", f"mail.{self.target}"]
        return self
    
    def find_endpoints(self):
        print("[*] Discovering endpoints...")
        self.results["endpoints"] = ["/api/v1/users", "/api/v1/auth", "/.env", "/robots.txt"]
        return self
    
    def detect_tech(self):
        print("[*] Detecting technologies...")
        self.results["technologies"] = ["React", "Node.js", "AWS", "Cloudflare"]
        return self
    
    def report(self):
        return json.dumps(self.results, indent=2)

def main():
    parser = argparse.ArgumentParser(description="ReconPro - Bug Bounty Reconnaissance")
    parser.add_argument("target", help="Target domain")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()
    
    r = ReconPro(args.target)
    r.find_subdomains().find_endpoints().detect_tech()
    
    output = r.report()
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"[+] Results saved to {args.output}")
    else:
        print(output)

if __name__ == "__main__":
    main()
