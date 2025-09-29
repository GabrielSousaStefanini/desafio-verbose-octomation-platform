# Especificação Técnica – Automação de Conversão de Textos para Caixa Alta/Baixa

## 1. Descrição
Esta automação tem como objetivo converter o conteúdo de arquivos de texto em uma pasta para **caixa alta** ou **caixa baixa**, de forma automática.  
Serve para padronização de textos ou preparação de arquivos para processamento adicional.

---

## 2. Escopo
- A automação será executada em um diretório fornecido pelo usuário.  
- Apenas arquivos de texto (`.txt`) serão processados; subpastas serão ignoradas.  
- A automação deve criar novos arquivos com o conteúdo convertido, preservando os originais.  
- O usuário deve poder escolher se quer converter para caixa alta ou caixa baixa.

---

## 3. Regras de Negócio
1. **Entrada do diretório**: o usuário define o caminho onde estão os arquivos de texto.  
2. **Processamento exclusivo de arquivos de texto**: outros tipos de arquivo não serão alterados.  
3. **Escolha do modo de conversão**:  
   - **Caixa alta**: todos os caracteres são convertidos para maiúsculas.  
   - **Caixa baixa**: todos os caracteres são convertidos para minúsculas.  
4. **Criação de novos arquivos**: cada arquivo convertido será salvo com um sufixo indicando o tipo de conversão.  
   - Exemplo: `arquivo.txt` → `arquivo_maiusculas.txt` ou `arquivo_minusculas.txt`  
5. **Execução atômica**: nenhum arquivo original deve ser sobrescrito ou perdido.  
6. **Registro de logs**: todos os processos devem ser logados em um arquivo de log do dia; apenas um arquivo de log deve ser criado por dia. 
7. **Relatório final**: ao término, a automação deve apresentar:  
   - Total de arquivos encontrados  
   - Total de arquivos convertidos com sucesso  

---

## 4. Requisitos Funcionais
- RF01: Permitir a escolha do diretório de entrada.  
- RF02: Listar todos os arquivos `.txt` do diretório, ignorando subpastas.  
- RF03: Aplicar o modo de conversão escolhido pelo usuário (caixa alta ou caixa baixa).  
- RF04: Criar novos arquivos com o conteúdo convertido, preservando os originais.  
- RF05: Registrar log em todas as etapas do processo.  
- RF06: Exibir relatório final de execução.  

---

## 5. Requisitos Não Funcionais
- RNF01: O script deve ser implementado exclusivamente com bibliotecas nativas do Python.  
- RNF02: O tempo de execução deve ser inferior a 1 segundo para até 100 arquivos de tamanho médio.  
- RNF03: O processo deve ser idempotente (rodar duas vezes não deve duplicar efeitos inesperados).  

---

## 6. Fluxo Simplificado
1. Usuário informa diretório de entrada e modo de conversão.  
2. A automação lista arquivos `.txt` do diretório.  
3. Para cada arquivo:  
   - Lê o conteúdo  
   - Converte para caixa alta ou caixa baixa  
   - Salva em um novo arquivo com sufixo apropriado  
4. Registrar log em todas as etapas do processo.  
5. Exibe relatório final com total de arquivos convertidos.
