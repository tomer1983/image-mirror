"""Utility functions for Image Mirror."""

import os
import yaml
import logging
from typing import Dict
from dotenv import load_dotenv

def setup_logging(level: int = logging.INFO) -> None:
    """Set up logging configuration."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def load_config(config_path: str) -> Dict:
    """Load and parse configuration file."""
    load_dotenv()  # Load environment variables from .env file
    
    if not os.path.exists(config_path):
        return {}
        
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Replace environment variables in config
    if config and isinstance(config, dict):
        _replace_env_vars(config)
    
    return config

def _replace_env_vars(config: Dict) -> None:
    """Replace environment variables in configuration."""
    for key, value in config.items():
        if isinstance(value, dict):
            _replace_env_vars(value)
        elif isinstance(value, str) and value.startswith('${') and value.endswith('}'):
            env_var = value[2:-1]
            config[key] = os.getenv(env_var, '')
