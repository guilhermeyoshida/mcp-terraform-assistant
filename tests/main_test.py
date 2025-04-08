import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp.main import parse_args, main

def test_parse_args_default():
    """Test parsing arguments with default values"""
    with patch('sys.argv', ['main.py']):
        args = parse_args()
        assert args.host == 'localhost'
        assert args.port == 8080
        assert args.terraform_dir == '.'
        assert args.debug is False

def test_parse_args_custom():
    """Test parsing arguments with custom values"""
    test_args = [
        'main.py',
        '--host', '0.0.0.0',
        '--port', '9000',
        '--terraform-dir', '/path/to/terraform',
        '--debug'
    ]
    with patch('sys.argv', test_args):
        args = parse_args()
        assert args.host == '0.0.0.0'
        assert args.port == 9000
        assert args.terraform_dir == '/path/to/terraform'
        assert args.debug is True

def test_main_function():
    """Test the main function"""
    with patch('mcp.main.parse_args') as mock_parse_args, \
         patch('mcp.main.Config') as mock_config, \
         patch('mcp.main.Server') as mock_server:
        
        # Setup mock arguments
        mock_args = MagicMock()
        mock_args.host = 'localhost'
        mock_args.port = 8080
        mock_args.terraform_dir = '.'
        mock_args.debug = False
        mock_parse_args.return_value = mock_args
        
        # Setup mock config
        mock_config_instance = MagicMock()
        mock_config.from_args.return_value = mock_config_instance
        
        # Setup mock server
        mock_server_instance = MagicMock()
        mock_server.return_value = mock_server_instance
        
        # Call main function
        main()
        
        # Verify the mocks were called correctly
        mock_parse_args.assert_called_once()
        mock_config.from_args.assert_called_once_with(mock_args)
        mock_server.assert_called_once_with(mock_config_instance)
        mock_server_instance.start.assert_called_once() 