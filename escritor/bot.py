from botcity.web import WebBot, Browser, By
from botcity.web.parsers import table_to_dict
from botcity.maestro import *
from botcity.web.browsers.firefox import default_options
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
    webbot.headless = False

    # Uncomment to change the default Browser to Firefox
    webbot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    webbot.driver_path = webbot.get_resource_abspath("geckodriver")
    
    # New destination to the downloads.
    webbot.download_folder_path = "/home/angelo/Área de trabalho/documentos/downloads_automates"

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
    # Quando outra página é carregada, os elementos rastreados antes precisam ser encontrados novamente, 
    # pois os objetos criados não funcionam. Por isso, os encontro em cada iteração.
    disciplinas = webbot.find_elements("Acessar Disciplina", By.LINK_TEXT)
    quant_disciplinas = len(disciplinas)
    
    for i in range(quant_disciplinas + 1):

        # Apertar em "Acessar Disciplina".
        disciplina = disciplinas[i]
        disciplina.click()

        # "Materiais de aula". É uma aba que precisa ser clicada. Mostra uma tabela com os materiais.
        materiais_de_aula = webbot.find_element("/html/body/div/main/ul[1]/li[4]/a", By.XPATH)
        webbot.wait_for_element_visibility(element= materiais_de_aula, visible= True, 
                                               waiting_time= 10_000)
        materiais_de_aula.click()

        # Tabela Materiais de Estudo. 
        # "Descrição" é a coluna onde estão os links para materias lançados pelos professores.
        # As vezes, não existe tabela, pois algum professor não mandou materiais.
        elemento_tabela = webbot.find_element("/html/body/div/main/div[7]/div/div/table", By.XPATH)
        tabela_materiais = table_to_dict(elemento_tabela)

        links_para_materiais = [x['descrição'] for x in tabela_materiais]
        links_processados = [processar(x) for x in links_para_materiais]
        arquivos_a_baixar = to_download(links_para_materiais)

        # Clicar nos links para download de materiais.
        for name_file in arquivos_a_baixar:
            try:
                link = webbot.find_element(selector= name_file, by= By.LINK_TEXT)
                link.click()
            except AttributeError: # Link leva a outra página.
                webbot.back()

        # Voltar para a página onde estão todas as disciplinas. 
        webbot.back()
        webbot.back()

        # Esperar a página carregar. Uso o título "Minhas Disciplinas" presente na página das 
        # disciplinas. 
        titulo_qualquer = webbot.find_element("Minhas Disciplinas", By.LINK_TEXT)
        webbot.wait_for_element_visibility(titulo_qualquer, visible= True, waiting_time= 10_000)


        # Rastrear novamente as disciplinas se necessário.
        # Se já é última disciplina, isso não é preciso.
        if not i == quant_disciplinas:
            disciplinas = webbot.find_elements("Acessar Disciplina", By.LINK_TEXT)
        

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
