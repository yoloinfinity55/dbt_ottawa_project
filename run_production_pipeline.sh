#!/bin/bash
set -e

echo "Starting Production Pipeline..."

# 1. Navigate to the dbt project folder
cd jaffle_shop

# 2. Install dependencies (Crucial for fresh Airflow containers)
echo "Installing dbt dependencies..."
dbt deps

# 3. Run Models (Using the local profiles.yml)
echo "Running models..."
dbt run --profiles-dir .

# 4. Run Tests (Using the local profiles.yml)
echo "Testing models..."
dbt test --profiles-dir .

echo "Pipeline Finished Successfully!"
