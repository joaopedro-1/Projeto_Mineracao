# Projeto de Mineração

## 🧑‍💻 Autor  

- João Pedro de Lima e Silva (201921250031) - joao.silva.4@academico.ifpb.edu.br

## 🎯 Tema e Motivação  
  Inicialmente, a proposta era utilizar um sensor giroscópio para coletar dados de motores de ar-condicionado e analisar o comportamento dos mesmos ao longo do tempo. No entanto, devido à demanda por mais estrutura e tempo para essa abordagem, optou-se pela utilização de uma base de dados pronta.

  O conjunto de dados da NASA foi selecionado por conter uma grande quantidade de informações sobre motores a jato operando até o ponto de falha. Isso permite a análise do desgaste e da vida útil de motores de forma eficiente. Além de ser uma base confiável e amplamente utilizada, ela oferece um bom cenário para aplicar técnicas de mineração de dados e prever falhas com base nos padrões de funcionamento registrados.
## 📊 Conjunto de Dados Selecionado  
- **Nome do conjunto de dados:**
  
  Kaggle - NASA Turbofan Jet Engine Data Set
  
- **Fonte:**

  Kaggle: https://www.kaggle.com/datasets/behrad3d/nasa-cmaps
  
  Referência oficial: https://www.nasa.gov/intelligent-systems-division/
  
- **Descrição breve:**  
  O conjunto de dados apresenta informações simuladas de motores a jato operando até a falha, geradas pela NASA por meio do simulador C-MAPSS. Cada motor é monitorado por 21 sensores e 3 variáveis operacionais ao longo de vários ciclos de operação. A base está dividida em quatro subconjuntos (FD001 a FD004), que representam diferentes cenários de variabilidade nas condições e nos modos de falha. Neste projeto, foi utilizado inicialmente o subset FD001, que possui condições operacionais e modos de falha fixos. O objetivo principal é prever a quantidade de ciclos restantes antes da falha (Remaining Useful Life - RUL).
  
- **Justificativa para a escolha:**  
  O conjunto é completo, confiável e amplamente utilizado em pesquisas voltadas para manutenção preditiva. Permite trabalhar com séries temporais de dados sensoriais, possibilitando análises aprofundadas sobre degradação de motores. Além disso, oferece uma base sólida para aplicação de modelos estatísticos e de aprendizado de máquina em problemas reais relacionados à vida útil de componentes mecânicos.
---

## ❓ Perguntas ou Hipóteses  
- Qual é o padrão de degradação dos motores ao longo dos ciclos de operação?
- É possível prever com boa precisão a vida útil restante (RUL) de um motor com base nos dados dos sensores?
- Existe algum sensor ou variável que se destaque como mais relevante na previsão da falha?
- O comportamento dos sensores se altera de forma perceptível nas fases finais antes da falha?
- Técnicas de regressão simples (como regressão linear) conseguem resultados competitivos em relação a modelos mais complexos?

## 🔍 Metodologia  
O projeto seguiu um fluxo de trabalho estruturado:
1 **Exploração e Limpeza:**
-Carregamento dos dados.
-Renomeação das colunas para melhor compreensão.
-Identificação e tratamento de valores ausentes ou duplicados.
2 **Análise Exploratória (EDA):**
3 **Engenharia de Features:**
4 **Modelagem Preditiva:**
## 🛠️ Ferramentas Utilizadas  
*A preencher na próxima etapa.*  
Quais linguagens, bibliotecas ou softwares serão utilizados no projeto.

## 📈 Resultados  
*A preencher após as análises.*  
Resumo visual e interpretativo dos principais achados.

## 📌 Conclusões  
*A preencher no final do projeto.*  
Síntese dos aprendizados e implicações das análises realizadas.

## ⚠️ Limitações e Trabalhos Futuros  
*A preencher no final do projeto.*  
Quais foram as limitações do estudo e o que poderia ser feito com mais tempo ou dados adicionais.

---

