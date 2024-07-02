import json

def load_data(data_file):
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except:
        return {}
    
def save_data(TO_UPDATE, FILEDIR):
    try:
        with open(FILEDIR, "w") as f:
            json.dump(TO_UPDATE, f, indent = 4)
    except Exception as e:
        print("Failed to update {FILEDIR}. Exception:", e)