# 🔮 Churn Prediction: Retenção de Clientes com IA

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit--Learn-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)

---

## 💼 Descrição do Projeto
Este projeto resolve um problema clássico de empresas de assinatura: o **Churn** (cancelamento). Utilizando dados históricos, construímos um modelo preditivo capaz de identificar clientes com alta probabilidade de saída.

**Impacto no Negócio:** Identificar o churn preventivamente permite que a equipe de marketing aja antes que o cliente cancele, economizando custo de aquisição (CAC) e mantendo a receita recorrente (LTV).

---

## 📂 Estrutura do Projeto
O projeto está organizado da seguinte forma:
├── data/ # Dataset bruto e processado (CSV) ├── images/ # Gráficos gerados pelo modelo para visualização ├── notebooks/ # Jupyter Notebooks com a análise passo a passo ├── README.md # Documentação do projeto

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas Principais:**
    * `Pandas` e `Numpy` (Manipulação de dados)
    * `Matplotlib` e `Seaborn` (Visualização)
    * `Scikit-Learn` (Machine Learning - Random Forest)

---

## 📊 Resultados Obtidos
O foco da modelagem foi maximizar o **Recall** da classe "Churn" (1), pois o custo de não detectar um cancelamento é maior do que oferecer um desconto desnecessário.

* **Acurácia Global:** 97%
* **Precision (Churn):** 0.80
* **Recall (Churn):** 0.31*

> ⚠️ *Nota: O Recall de 31% indica dificuldade do modelo com dados desbalanceados. Próximas versões incluirão técnicas de SMOTE.*

### Visualização da Performance
![Matriz de Confusão](images/confusion_matrix.png)
*A matriz acima mostra onde o modelo acertou (diagonal azul escura) e onde errou.*

---

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/wellalvesb/churn-prediction.git](https://github.com/wellalvesb/churn-prediction.git)

   👨‍💻 Autor
Desenvolvido por Welton Alves.
