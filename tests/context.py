"""
    Title: test_calculator.py

    Author: Shayne Cardwell

    Description: This module adds context to testing suite
"""

# import os
import sys
from pathlib import Path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, Path(__file__).absolute().parent)  # Python 3 only

import app
