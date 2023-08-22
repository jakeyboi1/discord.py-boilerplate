# Import needed modules here
import subprocess

#Misc Helper Functions

#Copy text to clipboard
def copy2clip(txt): #defines copy2clip function with a paramater of txt which is a string to copy to the clipboard
    cmd='echo ' + txt.strip()+'|clip' #copies the text
    return subprocess.check_call(cmd, shell=True) #Once done the function returns