import re, glob
 
# codesignal analyzingIpAddresses
#author; Nifemi Alpine

files=glob.glob("/root/devops/dir*/.txt")

print(files)
for path in files:
    
    with open(path) as fh:
      fstring = fh.read().replace('\n', '')

    ips=[]
    regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',fstring)
    if regex is not None:
       for match in regex:
           if match not in ips:
               ips.append(match)
               print(match)
