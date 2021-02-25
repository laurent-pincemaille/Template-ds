python -m venv venv
git init
git add .
git commit -m "Initial commit"
call venv\Scripts\activate.bat
pip install -e .
pip list
