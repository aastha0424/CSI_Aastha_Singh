# extract_model_params.py

import pickle
import yaml
import json
import os

# === File paths ===
PKL_FILE = "model.pkl"
YAML_OUTPUT = "model_params.yaml"
JSON_OUTPUT = "model_params.json"

# === Load the pickle file ===
if not os.path.exists(PKL_FILE):
    print(f"❌ Error: '{PKL_FILE}' not found in the current directory.")
    exit(1)

with open(PKL_FILE, "rb") as f:
    model = pickle.load(f)

# === Extract readable model parameters ===
try:
    params = model.get_params()
except AttributeError:
    print("❌ The loaded object does not have a get_params() method (not an sklearn-style model).")
    exit(1)

# === Save as YAML ===
with open(YAML_OUTPUT, "w") as f_yaml:
    yaml.dump(params, f_yaml, default_flow_style=False)
print(f"✅ Saved model parameters to '{YAML_OUTPUT}'")

# === Save as JSON ===
with open(JSON_OUTPUT, "w") as f_json:
    json.dump(params, f_json, indent=4)
print(f"✅ Saved model parameters to '{JSON_OUTPUT}'")
