# Especificação Técnica – Automação de Renomear Arquivos em Lote

## 1. Descrição
Esta automação tem como objetivo renomear arquivos de forma automatizada em um diretório específico, aplicando padrões de nomenclatura definidos pelo usuário.  
O foco é padronizar nomes de arquivos, manter a integridade das extensões e evitar conflitos de sobrescrita.

---

## 2. Escopo
- A automação será executado em um diretório fornecido pelo usuário.
- Apenas arquivos serão processados; subpastas devem ser ignoradas.
- A extensão original de cada arquivo deve ser preservada.
- A automação deve permitir prefixos, sufixos e numeração sequencial nos nomes dos arquivos.

---

## 3. Regras de Negócio
1. **Entrada do diretório**: o usuário define o caminho onde os arquivos estão localizados.
2. **Processamento exclusivo de arquivos**: diretórios não devem ser alterados.
3. **Modos de renomeação**:
   - **Prefixo**: adicionar uma string no início do nome do arquivo.  
     Exemplo: `foto.jpg` → `novo_foto.jpg`
   - **Sufixo**: adicionar uma string antes da extensão.  
     Exemplo: `foto.jpg` → `foto_novo.jpg`
   - **Numeração sequencial**: aplicar numeração incremental preservando a ordem de listagem.  
     Exemplo: `documento.txt` → `documento_1.txt`, `documento_2.txt`
4. **Preservação da extensão**: a parte após o último ponto (`.`) no nome original deve ser mantida.
5. **Resolução de conflitos**: se o novo nome já existir no diretório, a automação deve acrescentar o sufixo `_dup` para evitar sobrescrita.  
   Exemplo: `arquivo.txt` → `arquivo_dup.txt`
6. **Execução atômica**: nenhum arquivo deve ser sobrescrito ou perdido durante o processo.
7. **Registro de logs**: todos os processos devem ser logados em um arquivo de log do dia; apenas um arquivo de log deve ser criado por dia. 
8. **Relatório final**: ao término, a automação deve apresentar:
   - Total de arquivos encontrados
   - Total de arquivos renomeados com sucesso
   - Total de conflitos detectados

---

## 4. Requisitos Funcionais
- RF01: Permitir a escolha do diretório de entrada.
- RF02: Listar todos os arquivos do diretório ignorando subpastas.
- RF03: Aplicar o modo de renomeação escolhido pelo usuário.
- RF04: Garantir preservação da extensão do arquivo.
- RF05: Tratar conflitos de nome com a regra `_dup`.
- RF06: Registrar log em todas as etapas do processo.  
- RF07: Gerar relatório de execução.

---

## 5. Requisitos Não Funcionais
- RNF01: O script deve ser implementado exclusivamente com bibliotecas nativas do Python.
- RNF02: O tempo de execução deve ser inferior a 1 segundo para até 100 arquivos.
- RNF03: O processo deve ser idempotente (rodar duas vezes não deve duplicar efeitos inesperados).

---

## 6. Fluxo Simplificado
1. Usuário informa diretório e modo de renomeação.  
2. A automação lista arquivos do diretório.  
3. Para cada arquivo:  
   - Aplica regra de renomeação  
   - Verifica conflito  
   - Renomeia ou adiciona `_dup`  
4. Registrar log em todas as etapas do processo.  
5. Exibe relatório final.

---
