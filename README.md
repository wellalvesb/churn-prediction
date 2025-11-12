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

## 📈 Resultados Obtidos
O projeto evoluiu em duas etapas. Focamos em maximizar o **Recall** da classe "Churn" (1).

### Versão 1 (Sem Balanceamento)
* Precision: 0.80
* Recall: 0.31
* *Diagnóstico:* O modelo tinha dificuldade em identificar a classe minoritária.

### Versão 2 (Com SMOTE)
Aplicamos técnica de oversampling (SMOTE) nos dados de treino.
* **Precision:** 0.30 (Caiu, pois o modelo arrisca mais)
* **Recall:** 0.46 (Subiu drasticamente, detectando mais cancelamentos)

> **Conclusão:** A Versão 2 é mais segura para o negócio, pois detecta 46% dos cancelamentos contra apenas 31% da versão anterior.

### Comparativo Visual
| Matriz V1 (Original) | Matriz V2 (Balanceada) |
| :---: | :---: |
| ![Matriz V1](images/confusion_matrix.png) | ![Matriz V2](images/confusion_matrix_v2.png) |
---
## 📱 Aplicação Web (Streamlit)
Para demonstrar o modelo em funcionamento, desenvolvi uma interface web interativa onde é possível simular novos clientes e receber a previsão em tempo real.

**Pré-requisitos para rodar:**
```bash
pip install streamlit
## 🚀 Próximos Passos (Roadmap)
1. **Feature Engineering:** Testar novas variáveis derivadas.

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/wellalvesb/churn-prediction.git](https://github.com/wellalvesb/churn-prediction.git)

   👨‍💻 Autor
Desenvolvido por Welton Alves.
