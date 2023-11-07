import subprocess

if __name__ == '__main__':
    
    command = 'streamlit run src/App.py'
    subprocess.call(command.split())