# README - Compilador Parcial de C em Python

Este é um compilador parcial de C implementado em Python utilizando a biblioteca Ply. O compilador atualmente tem algumas limitações e bugs conhecidos, especialmente relacionados ao reconhecimento de funções e estruturas `if`.

## Executando o Compilador

Para executar o compilador, utilize o seguinte comando:

```python compiler.py <path_to_file>```


Onde `<path_to_file>` é o caminho para o arquivo de entrada em C que você deseja compilar.

## Bugs Conhecidos

- **Reconhecimento de Funções:** O compilador pode ter dificuldade em reconhecer corretamente chamadas de funções.
  
- **Estruturas `if`:** Pode haver problemas na análise de estruturas condicionais `if`.

## Regras Semânticas Implementadas

Durante a implementação, foram estabelecidas as seguintes regras semânticas:

1. **Variáveis não inicializadas:** Não é permitido chamar uma variável que não tenha sido inicializada previamente.
   
2. **Tipagem de Variáveis:** Não é permitido declarar uma variável de um tipo e atribuir a ela um valor de outro tipo.

3. **Declaração de Variáveis:** Não é permitido declarar duas variáveis com o mesmo nome no mesmo escopo.

## Estado Atual e Limitações

Este compilador parcial é funcional em um aspecto geral, mas pode não lidar adequadamente com funções complexas e estruturas condicionais em todos os casos. Alguns bugs podem afetar a precisão e a completude da compilação.
