# Setup Instructions

Follow these steps on a Rocky Linux machine to prepare the environment for the CSV comparison project.

1. **Install pyenv and pyenv‑virtualenv** (if not already installed):
   ```bash
   git clone https://github.com/pyenv/pyenv.git ~/.pyenv
   git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
   source ~/.bashrc
   ```

2. **Install the required Python version**
   ```bash
   # Use the version specified in .python-version
   pyenv install $(cat .python-version)
   pyenv virtualenv $(cat .python-version) csv-compare-env
   pyenv local csv-compare-env
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install polars
   ```

After these steps, you can run the comparison script using:
```bash
python src/main.py
```
