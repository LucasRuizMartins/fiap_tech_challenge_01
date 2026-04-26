# 📦 Guia: Como Salvar Modelos na Pasta `models/`

## 🚀 Início Rápido

```python
from tech_challenge_01.models import manager

# Salvar modelo
manager.save_joblib(seu_modelo, "nome_do_modelo")

# Carregar modelo
modelo = manager.load_joblib("nome_do_modelo")
```

---

## 📋 Opções de Persistência

### 1️⃣ **JOBLIB** ⭐ (Recomendado para sklearn)

**Quando usar:** Modelos scikit-learn (RandomForest, GradientBoosting, etc)

```python
# Salvar
manager.save_joblib(rf, "random_forest_nps")

# Carregar
rf = manager.load_joblib("random_forest_nps")
```

**Vantagens:**
- ✅ Mais rápido que pickle para arrays NumPy
- ✅ Melhor para arquivos grandes
- ✅ Compatível com todos os modelos sklearn
- ✅ Suporta compressão automática

---

### 2️⃣ **PICKLE** (Alternativa genérica)

**Quando usar:** Qualquer objeto Python serializável

```python
# Salvar
manager.save_pickle(seu_modelo, "meu_modelo")

# Carregar
modelo = manager.load_pickle("meu_modelo")
```

**Vantagens:**
- ✅ Formato padrão Python
- ✅ Funciona com qualquer objeto

**Desvantagens:**
- ❌ Mais lento para dados grandes
- ❌ Vulnerabilidades de segurança

---

## 💾 Salvando Métricas e Informações

### Salvar Métricas de Desempenho

```python
metricas = {
    "r2_score": 0.87,
    "mae": 0.45,
    "rmse": 0.52,
    "modelo": "RandomForest"
}

manager.save_metrics(metricas, "meu_modelo")
```

**Arquivo gerado:** `models/meu_modelo_metrics.json`

### Carregar Métricas

```python
metricas = manager.load_metrics("meu_modelo")
print(f"R² Score: {metricas['r2_score']}")
```

---

### Salvar Informações do Modelo

```python
info = {
    "nome_modelo": "RandomForestRegressor",
    "features": ["feature1", "feature2", "feature3"],
    "hiperparametros": {
        "n_estimators": 100,
        "max_depth": 10,
        "random_state": 42
    },
    "data_treinamento": "desafio_nps_fase_1.csv"
}

manager.save_model_info(info, "meu_modelo")
```

**Arquivo gerado:** `models/meu_modelo_info.json`

### Carregar Informações

```python
info = manager.load_model_info("meu_modelo")
print(f"Features: {info['features']}")
```

---

## 📂 Estrutura de Arquivos

```
models/
├── random_forest_nps.joblib           # Modelo
├── random_forest_nps_metrics.json     # Métricas
├── random_forest_nps_info.json        # Informações
├── gradient_boosting_nps.joblib       # Outro modelo
└── ...
```

---

## 🔍 Listar Modelos Disponíveis

```python
modelos = manager.list_models()
print(modelos)

# Saída:
# {
#   'joblib': ['random_forest_nps.joblib', 'gradient_boosting_nps.joblib'],
#   'pickle': [],
#   'metrics': ['random_forest_nps_metrics.json']
# }
```

---

## 📝 Exemplo Completo

```python
from tech_challenge_01.models import manager

# 1. Treinar modelo
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 2. Calcular métricas
from sklearn.metrics import r2_score, mean_absolute_error
r2 = r2_score(y_test, modelo.predict(X_test))
mae = mean_absolute_error(y_test, modelo.predict(X_test))

# 3. Salvar tudo
manager.save_joblib(modelo, "meu_melhor_modelo")

manager.save_metrics({
    "r2_score": r2,
    "mae": mae,
    "n_amostras_teste": len(y_test)
}, "meu_melhor_modelo")

manager.save_model_info({
    "features": X.columns.tolist(),
    "hiperparametros": modelo.get_params(),
    "data_criacao": "2026-04-25"
}, "meu_melhor_modelo")

# 4. Carregar em uma nova sessão
modelo_novo = manager.load_joblib("meu_melhor_modelo")
metricas = manager.load_metrics("meu_melhor_modelo")
info = manager.load_model_info("meu_melhor_modelo")

print(f"Modelo carregado com R² = {metricas['r2_score']}")
```

---

## 🎯 Melhores Práticas

| ✅ Faça | ❌ Evite |
|--------|---------|
| Use **joblib** para sklearn | Use pickle para modelos sklearn |
| Salve métricas junto | Salve apenas o modelo |
| Documente features usadas | Confie em memória |
| Use nomes descritivos | `modelo1.joblib`, `m.joblib` |
| Versione seus modelos | `modelo_v1`, `modelo_v2` | Sobreescreva modelos antigos |
| Use controle de versão Git | Salve binários sem controle |

---

## 🔗 Referências

- [Joblib Documentation](https://joblib.readthedocs.io/)
- [Pickle Documentation](https://docs.python.org/3/library/pickle.html)
- [Sklearn Model Persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
