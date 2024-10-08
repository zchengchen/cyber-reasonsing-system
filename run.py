import argparse
import json
import subprocess
import re
import os

parser = argparse.ArgumentParser(description="A tool to manage commands like 'history --enable'")
subparsers = parser.add_subparsers(dest='command', help='Available commands')
history_parser = subparsers.add_parser('history', help='Handle history command')
history_parser.add_argument('--enable', action='store_true', help='run the script using previous records in the analysis_result.json.')
history_parser.add_argument('--disable', action='store_true', help='run the script from scratch.')
args = parser.parse_args()

if args.command == "history" and args.enable:
    print("Analysis potential vlunerabilities from all commits of nginx-source...")
    command = "python3 gpt_for_vuln_detect.py"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Anlysis finished and result are stored in analysis_result.json.")

analysis_result = []
with open("analysis_result.json", "r") as file:
    analysis_result = json.load(file)
vuln_commits = []
vuln_funcs = []
for each_analysis in analysis_result:
    pattern = r'FALSE'
    matches = re.findall(pattern, each_analysis["analysis"], re.DOTALL)
    if len(matches) == 0:
        vuln_commits.append(each_analysis)
for each_commit in vuln_commits:
    text = each_commit["analysis"]
    pattern = r'TRUE(?: \[(.*?)\])+'
    matches = re.findall(r'\[(.*?)\]', text)
    if len(matches) == 0:
        continue
    vuln_func = {"commit_index": each_commit["commit_index"], "vuln_func": []}
    for match in matches:
        if match[0:3] == "ngx":
            vuln_func["vuln_func"].append(match)
    vuln_funcs.append(vuln_func)
print(vuln_funcs)
            
