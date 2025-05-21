# Projeto de Mineração

## 🧑‍💻 Autor  

- João Pedro de Lima e Silva (201921250031) - joao.silva.4@academico.ifpb.edu.br

## 🎯 Tema e Motivação  
  Como entusiasta da área de hardware e sistemas embarcados, no início, a ideia era usar um sensor giroscópio para coletar dados de motores de ar-condicionado e analisar o comportamento deles ao longo do tempo. Mas como isso ia demandar mais estrutura e tempo, decidi usar uma base de dados pronta.

  Escolhi esse conjunto da NASA porque já traz muitos dados sobre motores a jato funcionando até falharem, o que tem tudo a ver com o que eu queria estudar: o desgaste e o tempo de vida útil de motores. Além disso, é um conjunto bem conhecido e confiável, o que me dá mais liberdade pra focar nas análises e aplicar técnicas de mineração de dados pra prever falhas e entender os padrões de funcionamento desses motores.
## 📊 Conjunto de Dados Selecionado  
- **Nome do conjunto de dados:**
  Kaggle - NASA Turbofan Jet Engine Data Set
  
- **Fonte:**

  Kaggle: https://www.kaggle.com/datasets/behrad3d/nasa-cmaps
  
  Referência oficial: https://www.nasa.gov/intelligent-systems-division/
  
- **Descrição breve:**  
  Esse conjunto traz dados simulados de motores a jato funcionando até a falha, gerados pela NASA usando o simulador C-MAPSS. Cada motor tem vários ciclos de operação, e em cada um deles são registrados dados de sensores e condições operacionais. Ao todo são 21 sensores, mais 3 variáveis operacionais, e um identificador do motor. A base é dividida em quatro subconjuntos com diferentes cenários e modos de falha. O foco principal é usar esses dados pra prever quanto tempo de vida útil (RUL) ainda resta pro motor antes de falhar.

  O conjunto abrange quatro diferentes conjuntos de teste (FD001 a FD004), cada um representando diferentes combinações de variabilidade nas condições operacionais e nas falhas. Neste projeto, foi utilizado inicialmente o subset FD001, que possui condições operacionais e modos de falha fixos.


- **Justificativa para a escolha:**  
  Escolhi esse conjunto de dados porque ele é bem completo, confiável e já foi usado em vários estudos sobre manutenção preditiva. Ele permite trabalhar com séries temporais de sensores reais de motores simulados, o que ajuda a entender como os motores se degradam com o tempo. Além disso, é ideal pra testar modelos de regressão e aprendizado de máquina voltados pra prever a vida útil dos motores. Como gosto da parte de hardware e sensores, achei que essa base encaixa bem com o tipo de problema que me interessa.

---

## ❓ Perguntas ou Hipóteses  
*Começar a planejar com perguntas de Estatística Descritiva*  
Liste aqui as perguntas de pesquisa ou hipóteses estatísticas que o grupo pretende investigar com base nos dados.

## 🔍 Metodologia  
*A preencher na próxima etapa.*  
Indique quais técnicas estatísticas serão utilizadas (análise exploratória, testes, correlações, modelos, etc.).

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

