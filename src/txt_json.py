import json
import sys

# Use the number of clusters from the command-line argument
num_clusters = sys.argv[1]  # e.g., "10"

obj_temp=[]
with open(f"./workspace/cluster_center_{num_clusters}.txt", "r+", encoding="utf-8") as ori:
    item: str
    for item in ori:
        obj_temp.append(eval(item))

json_temp=open(f"./workspace/cluster_center_{num_clusters}.json", "w", encoding="utf-8")
h=json.dumps(obj_temp,indent=1)
json_temp.write(h)
