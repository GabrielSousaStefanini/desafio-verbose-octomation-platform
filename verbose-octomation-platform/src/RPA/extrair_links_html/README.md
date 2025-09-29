# Especificação Técnica – Automação de Extração de Links de Arquivo HTML

## 1. Descrição
Esta automação tem como objetivo percorrer arquivos HTML salvos localmente e extrair todos os links contidos nas tags `<a href="">`.  
O resultado é uma lista organizada de URLs, que pode ser usada para análises ou processamento posterior.

---

## 2. Escopo
- A automação será executado em arquivos HTML especificados pelo usuário.  
- Apenas arquivos `.html` ou `.htm` serão processados; outros tipos de arquivo serão ignorados.  
- A automação deve extrair apenas links contidos em atributos `href` de tags `<a>`.  
- O usuário deve poder definir o arquivo de entrada e o arquivo de saída para armazenar os links extraídos.

---

## 3. Regras de Negócio
1. **Entrada do arquivo**: o usuário informa o caminho do arquivo HTML a ser processado.  
2. **Processamento exclusivo de arquivos HTML**: outros tipos de arquivo não serão alterados.  
3. **Extração de links**: a automação deve identificar todas as tags `<a>` e capturar o valor do atributo `href`.  
4. **Formato do arquivo de saída**: os links devem ser gravados em um arquivo de texto, um link por linha.  
5. **Remoção de duplicados**: links repetidos não devem ser gravados mais de uma vez.  
6. **Execução atômica**: nenhum link deve ser perdido ou sobrescrito durante o processo.  
7. **Registro de logs**: todos os processos devem ser logados em um arquivo de log do dia; apenas um arquivo de log deve ser criado por dia. 
8. **Relatório final**: ao término, a automação deve apresentar:  
   - Total de links encontrados  
   - Total de links únicos extraídos

---

## 4. Requisitos Funcionais
- RF01: Permitir a escolha do arquivo HTML de entrada.  
- RF02: Extrair todos os valores do atributo `href` de tags `<a>`.  
- RF03: Gravar os links em um arquivo de saída, um por linha.  
- RF04: Remover links duplicados do resultado final.  
- RF05: Registrar log em todas as etapas do processo.  
- RF06: Exibir relatório final com total de links encontrados e únicos.

---

## 5. Requisitos Não Funcionais
- RNF01: O script deve ser implementado exclusivamente com bibliotecas nativas do Python.  
- RNF02: O processamento deve ser rápido para arquivos HTML de tamanho médio (até 5 MB).  
- RNF03: O processo deve ser idempotente (rodar duas vezes não deve duplicar links no arquivo de saída).

---

## 6. Fluxo Simplificado
1. Usuário informa arquivo HTML de entrada e arquivo de saída.  
2. A automação lê o conteúdo do arquivo HTML.  
3. Identifica todas as tags `<a>` e captura os valores do atributo `href`.  
4. Remove links duplicados.  
5. Grava os links extraídos no arquivo de saída.  
6. Registrar log em todas as etapas do processo.  
7. Exibe relatório final com total de links encontrados e únicos.
