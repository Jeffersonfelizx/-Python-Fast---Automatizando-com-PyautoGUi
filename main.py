import pyautogui

pyautogui.alert("Iniciando a aplicaçao, Clique em Ok para Prosseguir ")


frases = "'Projeto enviado no processo automatizado by Jefferson Felix' "
githubAutomatizando = "https://github.com/Jeffersonfelizx/Python-Fast---Automatizando-PyautoGui"

# Funcoes 

# Abrir pasta 
def abrir_pasta(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.doubleClick(x,y)
    pyautogui.PAUSE = 2.0

# Descobrir posiçao 
def posicao_do_mouse():
    pyautogui.sleep(10)
    a = pyautogui.position()
    return print(a)

# Entrando na interface Git 
def git(): 
    pyautogui.rightClick(533,261); 
    pyautogui.click(202,490)
    pyautogui.write("git init"); pyautogui.press("Enter")
    pyautogui.write(f"git pull");pyautogui.press("Enter")
    pyautogui.write("git status"); pyautogui.press("Enter")
    pyautogui.write("git add ."); pyautogui.press("Enter")
    pyautogui.write(f"git commit -m {frases}"); pyautogui.press("Enter")
    pyautogui.write(f"git remote set-url origin {githubAutomatizando}"); pyautogui.press("Enter")
    pyautogui.write(f"git remote add origin {githubAutomatizando}");pyautogui.press("Enter")
    pyautogui.write("git push -u origin master");pyautogui.press("Enter")
    pyautogui.write("exit"); pyautogui.press("Enter")

def exit():
    pyautogui.click(1235,104)  

abrir_pasta(22,464)
abrir_pasta(534,229)
abrir_pasta(534,229)
git()
exit()