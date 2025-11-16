import json

# Input and output files
input_file = "tarpaulin-report.json"
output_file = "coverage-percentage.json"

# Read tarpaulin JSON
with open(input_file, "r") as f:
    data = json.load(f)

# Extract total coverage (float 0-1) and convert to integer percentage
coverage_float = data.get("coverage", 0.0)
coverage_pct = int(coverage_float)

# Prepare JSON for Shields.io or other uses
coverage_json = {
    "coverage": coverage_pct
}

# Write output JSON
with open(output_file, "w") as f:
    json.dump(coverage_json, f)

print(f"Generated {output_file} with coverage {coverage_pct}%")
