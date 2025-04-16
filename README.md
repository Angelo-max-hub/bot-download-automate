# O que é este projeto
Criei este bot para agilizar um processo que até hoje fiz manualmente: entrar na plataforma de ensino da minha faculdade (SUAP), baixar arquivos de materiais de estudo,
reorganizar os arquivos baixados e já existentes em diferentes pastas.

# Versão atual.
Alpha. Não está finalizado. Atualmente, o bot, que deveria entrar na platarforma de ensino SUAP (da minha faculdade) e baixar todos os materiais de aula necessários, não consegue fazer isso corretamente. 

O script Python no arquivo "main" possui alguns erros também. Apesar disso, não o corrigirei agora, porque estou trabalhando em um módulo C responsável por processamento de texto, que usarei para que o bot apenas baixe arquivos que ainda não foram baixados (o módulo irá comparar 2 nomes de arquivos - um link e um file salvo - e retornará "True" se representam o mesmo arquivo, e "False", caso o contrário). Ele é necessário porque os dois (link para download e arquivo salvo) são muito diferentes, o que dificulta determinar um download já foi feito com base nos arquivos salvos. Estou aberto a sugestões sobre alternativas para resolver esse problema.

# Ferramentas usadas
Usei ou usarei as seguintes ferramentas:
- python
- Botcity
- OS
# Como usar
Não é possível que outros usuários além de mim usem esse bot. Ele serve para baixar arquivos automaticamete da platarforma de ensino da minha faculdade, então ele é 
completamente customizado para mim. Mas, se alguém precisar de um bot que faz algo parecido, talvez eu possa fazer um, de graça, apenas pela experiência e para aumentar o meu
portifólio.

# O objetivo do projeto
Meu objetivo com esse bot é provar para recrutadores que sei usar a ferramenta e platarforma de automação RPA Botcity, além de dominar python.

# Estou aberto a críticas
Ficarei feliz de receber sugestões sobre o projeto.

# O código em ação
Dentro da pasta "resources", há um arquivo ".mp4" que mostra automação acontecendo.

# Presença de dados sensíveis
Me esqueci de colocar o arquivo ".env" com minha conta e senha do SUAP no gitignore, então ele foi publicado com o resto do projeto. Mas já mudei a senha da conta, e o arquivo .env não estará nos próximos commits.
