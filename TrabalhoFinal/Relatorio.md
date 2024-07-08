# Relatório de Implementação do Compilador em Python com Ply

Este relatório descreve a implementação de um compilador parcial da linguagem C utilizando a biblioteca Ply em Python, relacionando-a aos conceitos teóricos abordados na disciplina de Compiladores.

## Palavras-Chave e Tokens

Inicialmente, foram identificadas 33 palavras-chave da linguagem C e criadas 43 expressões regulares para interpretar símbolos e tipos comuns na linguagem, totalizando 76 tokens para o compilador. Esses tokens são essenciais para a análise léxica e sintática do código-fonte.

## Parser e Reconhecimento de Código

O compilador utiliza um parser baseado em funções definidas pelo usuário para reconhecer e interpretar diferentes trechos de código C. Foram implementadas funções para lidar com estruturas abstratas como definições de funções e estruturas de controle (`if`, `for`, `while`, `switch`), assim como trechos literais como declarações e atribuições de variáveis.

## Regras Semânticas Implementadas

Para garantir a corretude semântica do código interpretado, foram impostas as seguintes regras:

1. **Variáveis não inicializadas:** O compilador verifica se uma variável foi inicializada antes de ser utilizada em uma expressão.
   
2. **Tipagem de Variáveis:** Não é permitido declarar uma variável de um tipo e atribuir a ela um valor de outro tipo.

3. **Declaração de Variáveis:** Não é permitido declarar duas variáveis com o mesmo nome no mesmo escopo.

## Estado Atual e Limitações

Atualmente, o compilador enfrenta desafios na análise sintática, especialmente no reconhecimento completo de estruturas como definições de funções e blocos `if`. Isso limita sua funcionalidade completa como um compilador de C.

## Futuro do Projeto

Pretendo continuar o desenvolvimento do projeto para resolver os problemas sintáticos restantes e completar as funcionalidades planejadas. O código será refinado e otimizado conforme necessário para alcançar um compilador robusto e funcional.

## Link para o Repositório

O progresso e a versão final do projeto serão disponibilizados no seguinte repositório do GitHub:

[Link para o Repositório do GitHub](link_github)
