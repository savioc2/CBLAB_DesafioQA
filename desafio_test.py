from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ipdb 



def test_login_usuario_sem_cadastro():
    SITE_LINK = "https://app.cocobambu.com/entrar?backPage=on-boarding%2Fdelivery%3FnextPage%3D%252Fdelivery"

    options = webdriver.ChromeOptions()
    options.binary_location = "bin/chrome"
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get(SITE_LINK)

    # Passo 1: Informar um email válido
    email_input = driver.find_element(
        By.XPATH,
        "/html/body/app-root/ion-app/main/ion-router-outlet/app-login/div/div/form/div[1]/ion-input/input",
    )
    email_input.send_keys("savioc.unb@gmail.com")

    # Passo 2: Informar uma senha inválida
    senha_input = driver.find_element(
        By.XPATH,
        "/html/body/app-root/ion-app/main/ion-router-outlet/app-login/div/div/form/div[3]/ion-input/input",
    )
    senha_input.send_keys("fraca")

    # Passo 3: Clicar no botão "Entrar"
    entrar_button = driver.find_element(
        By.XPATH,
        "/html/body/app-root/ion-app/main/ion-router-outlet/app-login/div/div/div[2]/button",
    )
    entrar_button.click()

    time.sleep(2)

    # Passo 4: Clicar em "Cadastre-se"
    cadastra_button = driver.find_element(
        By.XPATH,
        "/html/body/app-root/ion-app/main/ion-router-outlet/app-login/div/div/div[3]/ion-col[1]/span[2]",
    )
    cadastra_button.click()

    time.sleep(2)
    # Passo 5: Preencher os campos com dados válidos:
    nomeCompleto_input = driver.find_element(
        By.XPATH,
        "/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[1]/ion-input/input",
    )
    nomeCompleto_input.send_keys("Savio Cunha de Carvalho")

    email1_input = driver.find_element(
        By.XPATH,
        "/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[3]/ion-input/input",
    )
    email1_input.send_keys("saviocunha.unb@gmail.com")

    senha_input = driver.find_element(
        By.XPATH,
        "/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[5]/ion-input/input",
    )
    senha_input.send_keys("Cococ2.")

    confirmaSenha_input = driver.find_element(
        By.XPATH,
        "/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[7]/ion-input/input",
    )
    confirmaSenha_input.send_keys("Cococ2.")

    time.sleep(2)

    wait = WebDriverWait(driver, 10)

    estado_button = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH, "//ion-sel-1-lbl",
                # "/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[9]/ion-select//label",
            )
        )
    )     
    estado_button.click()
    ipdb.set_trace()

    wait = WebDriverWait(driver, 5)

    escolhaEstado_button = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/app-root/ion-app/ion-action-sheet/div[2]/div/div[1]/button[8]",
            )
        )
    )
    escolhaEstado_button.click()

    wait = WebDriverWait(driver, 5)

    notificicacao_button = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[11]/ion-item[1]/ion-checkbox//label",
            )
        )
    )
    notificicacao_button.click()

    wait = WebDriverWait(driver, 5)

    termos_button = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[11]/ion-item[2]/ion-checkbox//label",
            )
        )
    )
    termos_button.click()

    # Resultados Esperados
    time.sleep(30)  # Aguardar para verificação (tempo de espera pode variar)
    # assert "Tela Principal" in driver.title  # Verifica se o usuário foi redirecionado para a tela principal

    driver.quit()


# def test_reset_senha():
#     SITE_LINK = "https://app.cocobambu.com/entrar?backPage=on-boarding%2Fdelivery%3FnextPage%3D%252Fdelivery"

#     options = webdriver.ChromeOptions()
#     options.binary_location = 'bin/chrome'
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()

#     driver.get(SITE_LINK)

test_login_usuario_sem_cadastro()
