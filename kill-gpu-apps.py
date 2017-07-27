import subprocess, os
import xml.etree.ElementTree as ET

# Obtain nvidia-smi output in XML format 
output = subprocess.Popen(["c:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi", "-q", "-x"],stdout=subprocess.PIPE)
nvidia_smi_output = output.communicate()[0]

# Parse string to XML
nvidia_xml_document = ET.fromstring(nvidia_smi_output)

# Find PID nodes
pids = []
for node in nvidia_xml_document.findall(".//pid"):
  pids.append(node.text)


# Kill PIDs
for pid in pids:
  os.system("taskkill /f /pid " + pid)
