# Especificação Técnica – Automação de Temporizador com Notificação Sonora

## 1. Descrição
Esta automação tem como objetivo criar um **temporizador** simples que notifica o usuário ao final de um período definido.  
A notificação é sonora (via `winsound` no Windows ou `print('\a')` em sistemas Unix) e serve para alertas de pausas, intervalos ou tarefas rápidas.

---

## 2. Escopo
- A automação será executado via linha de comando ou interface mínima de terminal.  
- O usuário deve poder definir a duração do temporizador em minutos ou segundos.  
- A automação deve emitir uma notificação sonora ao final do tempo.  
- A automação deve permitir a execução de múltiplos temporizadores de forma sequencial ou isolada.  

---

## 3. Regras de Negócio
1. **Entrada da duração**: o usuário informa quanto tempo o temporizador deve contar.  
2. **Unidades de tempo**: aceitar entradas em segundos ou minutos.  
3. **Notificação sonora**: a automação deve reproduzir um alerta ao término do período.  
   - No Windows, utilizar `winsound.Beep`.  
   - Em outros sistemas, utilizar `print('\a')` para sinal sonoro básico.  
4. **Execução sequencial**: se houver múltiplos temporizadores, cada um deve iniciar após a conclusão do anterior.  
5. **Interrupção**: o usuário pode cancelar o temporizador a qualquer momento via interrupção de teclado (`Ctrl+C`).  
7. **Registro de logs**: todos os processos devem ser logados em um arquivo de log do dia; apenas um arquivo de log deve ser criado por dia. 
8. **Relatório final**: ao término, exibir a duração definida e o status (concluído ou cancelado).

---

## 4. Requisitos Funcionais
- RF01: Permitir entrada da duração do temporizador.  
- RF02: Aceitar unidades de tempo em segundos ou minutos.  
- RF03: Reproduzir notificação sonora ao término do temporizador.  
- RF04: Permitir execução de múltiplos temporizadores sequenciais.  
- RF05: Permitir interrupção pelo usuário.  
- RF06: Registrar log em todas as etapas do processo.  
- RF07: Exibir relatório final com status e duração definida.

---

## 5. Requisitos Não Funcionais
- RNF01: O script deve ser implementado exclusivamente com bibliotecas nativas do Python.  
- RNF02: O temporizador deve ter precisão mínima de ±1 segundo.  
- RNF03: O processo deve ser idempotente e seguro para múltiplas execuções consecutivas.  

---

## 6. Fluxo Simplificado
1. Usuário informa a duração do temporizador (segundos ou minutos).  
2. A automação inicia a contagem regressiva.  
3. Ao término do período:  
   - Emite notificação sonora  
   - Exibe mensagem de conclusão  
4. Para múltiplos temporizadores, repete o processo para cada um.  
5. Registrar log em todas as etapas do processo.  
6. O usuário pode interromper o temporizador a qualquer momento com `Ctrl+C`.
