"""
Módulo para gerenciar persistência de modelos de ML.

Fornece funções para salvar e carregar modelos treinados em diferentes formatos.
"""

import json
import pickle
from pathlib import Path
from typing import Any, Dict, Optional

import joblib


class ModelManager:
    """Gerenciador de persistência de modelos."""

    def __init__(self, models_dir: str = "models"):
        """
        Inicializa o gerenciador de modelos.

        Args:
            models_dir: Diretório onde os modelos serão salvos. Default: "models"
        """
        self.models_dir = Path(models_dir)
        self.models_dir.mkdir(exist_ok=True)

    def save_joblib(self, model: Any, filename: str) -> Path:
        """
        Salva um modelo usando joblib (recomendado para sklearn).

        Args:
            model: Modelo treinado
            filename: Nome do arquivo (sem extensão)

        Returns:
            Path: Caminho completo do arquivo salvo
        """
        filepath = self.models_dir / f"{filename}.joblib"
        joblib.dump(model, filepath)
        print(f"✅ Modelo salvo em: {filepath}")
        return filepath

    def save_pickle(self, model: Any, filename: str) -> Path:
        """
        Salva um modelo usando pickle.

        Args:
            model: Modelo treinado
            filename: Nome do arquivo (sem extensão)

        Returns:
            Path: Caminho completo do arquivo salvo
        """
        filepath = self.models_dir / f"{filename}.pkl"
        with open(filepath, "wb") as f:
            pickle.dump(model, f)
        print(f"✅ Modelo salvo em: {filepath}")
        return filepath

    def load_joblib(self, filename: str) -> Any:
        """
        Carrega um modelo salvo com joblib.

        Args:
            filename: Nome do arquivo (com ou sem extensão .joblib)

        Returns:
            Any: Modelo carregado
        """
        if not filename.endswith(".joblib"):
            filename = f"{filename}.joblib"
        filepath = self.models_dir / filename
        model = joblib.load(filepath)
        print(f"✅ Modelo carregado de: {filepath}")
        return model

    def load_pickle(self, filename: str) -> Any:
        """
        Carrega um modelo salvo com pickle.

        Args:
            filename: Nome do arquivo (com ou sem extensão .pkl)

        Returns:
            Any: Modelo carregado
        """
        if not filename.endswith(".pkl"):
            filename = f"{filename}.pkl"
        filepath = self.models_dir / filename
        with open(filepath, "rb") as f:
            model = pickle.load(f)
        print(f"✅ Modelo carregado de: {filepath}")
        return model

    def save_metrics(self, metrics: Dict[str, Any], filename: str) -> Path:
        """
        Salva métricas de desempenho em JSON.

        Args:
            metrics: Dicionário com métricas
            filename: Nome do arquivo (sem extensão)

        Returns:
            Path: Caminho completo do arquivo salvo
        """
        filepath = self.models_dir / f"{filename}_metrics.json"
        with open(filepath, "w") as f:
            json.dump(metrics, f, indent=2, default=str)
        print(f"✅ Métricas salvas em: {filepath}")
        return filepath

    def load_metrics(self, filename: str) -> Dict[str, Any]:
        """
        Carrega métricas de desempenho de JSON.

        Args:
            filename: Nome do arquivo (com ou sem extensão)

        Returns:
            Dict: Dicionário com as métricas
        """
        if not filename.endswith("_metrics.json"):
            filename = f"{filename}_metrics.json"
        filepath = self.models_dir / filename
        with open(filepath, "r") as f:
            metrics = json.load(f)
        print(f"✅ Métricas carregadas de: {filepath}")
        return metrics

    def list_models(self) -> Dict[str, list]:
        """
        Lista todos os modelos salvos no diretório.

        Returns:
            Dict: Dicionário com tipos de arquivos e suas listas
        """
        models = {
            "joblib": [f.name for f in self.models_dir.glob("*.joblib")],
            "pickle": [f.name for f in self.models_dir.glob("*.pkl")],
            "metrics": [f.name for f in self.models_dir.glob("*_metrics.json")],
        }
        return models

    def save_model_info(self, model_info: Dict[str, Any], filename: str) -> Path:
        """
        Salva informações sobre o modelo (hiperparâmetros, features, etc).

        Args:
            model_info: Dicionário com informações do modelo
            filename: Nome do arquivo (sem extensão)

        Returns:
            Path: Caminho completo do arquivo salvo
        """
        filepath = self.models_dir / f"{filename}_info.json"
        with open(filepath, "w") as f:
            json.dump(model_info, f, indent=2, default=str)
        print(f"✅ Informações do modelo salvas em: {filepath}")
        return filepath

    def load_model_info(self, filename: str) -> Dict[str, Any]:
        """
        Carrega informações sobre o modelo.

        Args:
            filename: Nome do arquivo (com ou sem extensão)

        Returns:
            Dict: Dicionário com as informações
        """
        if not filename.endswith("_info.json"):
            filename = f"{filename}_info.json"
        filepath = self.models_dir / filename
        with open(filepath, "r") as f:
            model_info = json.load(f)
        print(f"✅ Informações do modelo carregadas de: {filepath}")
        return model_info


# Instância global para facilitar uso
manager = ModelManager()
