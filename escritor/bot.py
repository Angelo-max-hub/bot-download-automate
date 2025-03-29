from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from dotenv import load_dotenv
import os

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    webbot = WebBot()

    # Configure whether or not to run on headless mode
    webbot.headless = True

    # Uncomment to change the default Browser to Firefox
    webbot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    webbot.driver_path = webbot.get_resource_abspath("geckodriver")

    # Entrar no site do SUAP.
    webbot.start_browser()
    webbot.browse("https://suap.ifap.edu.br/edu/disciplinas/")

    # Implement here your logic...
    
    # Variaveis de ambiente.
    load_dotenv("escritor_robotico/escritor/resources/.env")
    meu_nome = os.getenv('meu_nome')
    minha_senha = os.getenv('minha_senha')

    # Obtém os arquivos já baixados
    arquivos_baixados = ["arquivo1", "arquivo 2"]

    # Fazer Login no SUAP
    nome = webbot.find_element(selector= "id_username", by= By.ID)
    nome.send_keys(meu_nome)

    senha = webbot.find_element(selector="id_password", by= By.ID)
    senha.send_keys(minha_senha)

    botao_acessar = webbot.find_element(selector="input.btn", by= By.CSS_SELECTOR)
    botao_acessar.click()

    # Baixar arquivos. 
    def what_files(tr) -> str:
        """
        Retorna o nome do material disponível de uma célula da segunda coluna da tabela "materiais de aula"
        """
        link_material = tr.find_element( By.CSS_SELECTOR, 'td:nth-child(2)').text.encode("utf-8")
        return link_material

    disciplinas = webbot.find_elements("Acessar Disciplina", By.LINK_TEXT)
    for elemento in disciplinas:
        # Apertar em "Acessar Disciplina".
        elemento.click()
        # "Materiais de aula".
        materiais_de_aula = webbot.find_element("/html/body/div/main/ul[1]/li[4]/a", By.XPATH)
        webbot.wait_for_element_visibility(element= materiais_de_aula, visible= True, waiting_time= 10_000)
        materiais_de_aula.click()
        # Materias disponíveis.
        tabela = webbot.find_element("/html/body/div/main/div[7]/div/div/table", By.XPATH)
        itens = tabela.find_elements(By.CSS_SELECTOR, "tbody>tr")
        arquivos_a_baixar = [what_files(x) for x in itens]

        # Baixar arquivos necessários.
        arquivos_necessarios = [x for x in arquivos_a_baixar if  x not in arquivos_baixados]
        for arquivo in arquivos_necessarios:
            # Baixe o arquivo.
            pass

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK.",
    #     total_items=0,
    #     processed_items=0,
    #     failed_items=0
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
