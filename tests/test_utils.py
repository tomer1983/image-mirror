"""Tests for Image Mirror utility functions."""

import pytest
import os
from src.utils import load_config, _replace_env_vars

def test_replace_env_vars(monkeypatch):
    """Test environment variable replacement in config."""
    monkeypatch.setenv('TEST_USERNAME', 'testuser')
    monkeypatch.setenv('TEST_PASSWORD', 'testpass')
    
    config = {
        'username': '${TEST_USERNAME}',
        'password': '${TEST_PASSWORD}',
        'url': 'https://example.com'
    }
    
    _replace_env_vars(config)
    
    assert config['username'] == 'testuser'
    assert config['password'] == 'testpass'
    assert config['url'] == 'https://example.com'

def test_load_config_missing_file():
    """Test loading config with missing file."""
    config = load_config('nonexistent.yaml')
    assert config == {}
