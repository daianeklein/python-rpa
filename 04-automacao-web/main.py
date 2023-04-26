import pyautogui
import time

chrome_tab = pyautogui.locateCenterOnScreen("img/new-tab-chrome.png", confidence=0.8)
pyautogui.click(chrome_tab[0]/2, chrome_tab[1]/2, duration=1)
pyautogui.typewrite('https://www.gabrielcasemiro.com.br/atividade_pyautogui', interval=0.1)
pyautogui.press('return')
time.sleep(5)

with open("membros.csv") as f:
    next(f)
    
    for line in f:
        line=line.strip()
        line=line.split(";")
        print("Dados: ", line)

        name=line[0]
        sex=line[1]
        email=line[2]
        phone=line[3]

        name_loc = pyautogui.locateCenterOnScreen("img/nome.png", confidence=0.8)
        pyautogui.click(name_loc[0]/2, name_loc[1]/2, duration=1)
        pyautogui.typewrite(name, interval=0.25)

        email_loc = pyautogui.locateCenterOnScreen("img/email.png", confidence=0.8)
        pyautogui.click(email_loc[0]/2, email_loc[1]/2, duration=1)
        pyautogui.typewrite(email, interval=0.25)

        telefone_loc = pyautogui.locateCenterOnScreen("img/telefone.png", confidence=0.8)
        pyautogui.click(telefone_loc[0]/2, telefone_loc[1]/2, duration=1)
        pyautogui.typewrite(phone, interval=0.25)

        sexo_loc = pyautogui.locateCenterOnScreen("img/sexo.png", confidence=0.8)
        pyautogui.click(sexo_loc[0]/2, sexo_loc[1]/2, duration=1)
        
        if sex=="Masculino":
            masc_loc = pyautogui.locateCenterOnScreen("img/masculino.png", confidence=0.8)
            pyautogui.click(masc_loc[0]/2, masc_loc[1]/2, duration=1)
        else:
            fem_loc = pyautogui.locateCenterOnScreen("img/feminino.png", confidence=0.8)
            pyautogui.click(fem_loc[0]/2, fem_loc[1]/2, duration=1)
        
        pyautogui.screenshot(f"cadastro_{name}.png")
        
        cadastro_loc = pyautogui.locateCenterOnScreen("img/botao_enviar.png", confidence=0.8)
        pyautogui.click(cadastro_loc[0]/2, cadastro_loc[1]/2, duration=1)

        time.sleep(3)

pyautogui.alert(text="Programa finalizado com sucesso!", title="Aviso do sistema", button="OK")









        