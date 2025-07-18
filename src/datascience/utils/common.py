import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Lee un archivo YAML y lo devuelve como ConfigBox

    Args:
        path_to_yaml (str): ruta del archivo YAML

    Raises:
        ValueError: si el archivo YAML está vacío
        e: cualquier otra excepción

    Returns:
        ConfigBox: datos cargados como atributos de clase
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Archivo YAML cargado correctamente: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("El archivo YAML está vacío")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Crea una lista de directorios

    Args:
        path_to_directories (list): lista con las rutas de los directorios
        verbose (bool, opcional): mostrar logs si está activado. Por defecto es True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directorio creado en: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Guarda un diccionario como archivo JSON

    Args:
        path (Path): ruta del archivo JSON
        data (dict): datos a guardar
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"Archivo JSON guardado en: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Carga datos desde un archivo JSON

    Args:
        path (Path): ruta del archivo JSON

    Returns:
        ConfigBox: datos cargados como atributos de clase
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Archivo JSON cargado correctamente desde: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Guarda datos en formato binario (usualmente modelos u objetos)

    Args:
        data (Any): datos u objetos a guardar
        path (Path): ruta del archivo binario
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Archivo binario guardado en: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Carga datos desde un archivo binario

    Args:
        path (Path): ruta del archivo binario

    Returns:
        Any: objeto almacenado en el archivo
    """
    data = joblib.load(path)
    logger.info(f"Archivo binario cargado desde: {path}")
    return data
