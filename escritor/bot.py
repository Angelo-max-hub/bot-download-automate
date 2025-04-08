from botcity.web import WebBot, Browser, By
from botcity.web.parsers import table_to_dict
from botcity.maestro import *
from dotenv import load_dotenv
import os
import ipdb
from utils.function_what_to_download import to_download


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
    meu_nome = os.environ["usuario_suap"]
    minha_senha = os.environ["senha_suap"]
    # Fazer Login no SUAP
    campo_nome = webbot.find_element(selector= "id_username", by= By.ID)
    campo_nome.send_keys(meu_nome)

    campo_senha = webbot.find_element(selector="id_password", by= By.ID)
    campo_senha.send_keys(minha_senha)

    botao_acessar = webbot.find_element(selector="input.btn", by= By.CSS_SELECTOR)
    botao_acessar.click()


    # Clicar em cada disciplina e baixar arquivos necessários.
    disciplinas = webbot.find_elements("Acessar Disciplina", By.LINK_TEXT)
    for disciplina in disciplinas:

        # Apertar em "Acessar Disciplina".
        disciplina.click()

        # "Materiais de aula". É uma aba que precisa ser clicada. Mostra uma tabela com os materiais.
        materiais_de_aula = webbot.find_element("/html/body/div/main/ul[1]/li[4]/a", By.XPATH)
        webbot.wait_for_element_visibility(element= materiais_de_aula, visible= True, waiting_time= 10_000)
        materiais_de_aula.click()

        # Tabela Materiais de Estudo. 
        # "Descrição" é a coluna onde estão os links para materias lançados pelos professores.
        elemento_tabela = webbot.find_element("/html/body/div/main/div[7]/div/div/table", By.XPATH)
        tabela_materiais = table_to_dict(elemento_tabela)

        links_para_materiais = [x['descrição'] for x in tabela_materiais]
        arquivos_a_baixar = to_download(links_para_materiais)
        
        # Clicar nos links para download de materiais.
        for name_file in arquivos_a_baixar:
            link = webbot.find_element(selector= name_file, by= By.LINK_TEXT)
            link.click()
        
        # Voltar para a página onde estão todas as disciplinas. 
        webbot.back()
        webbot.back()

        # Esperar a página carregar. 
        titulo_qualquer = webbot.find_element("Minhas Disciplinas", By.LINK_TEXT)
        webbot.wait_for_element_visibility(titulo_qualquer, visible= True, waiting_time= 10_000)


        

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
    ipdb.set_trace()
    main()
