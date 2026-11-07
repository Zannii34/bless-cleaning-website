Write-Host "Starting Bless's Cleaning Service Website..." -ForegroundColor Cyan

# 1. Create a virtual environment if it doesn't exist
if (-Not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# 2. Activate the virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

# 3. Install requirements
Write-Host "Installing requirements..." -ForegroundColor Yellow
pip install -r requirements.txt

# 4. Run the Python app
Write-Host "Launching Website! Open your browser and go to http://127.0.0.1:5000" -ForegroundColor Green
python app.py