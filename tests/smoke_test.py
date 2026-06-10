"""
Smoke tests to ensure that core modules and 3rd party dependencies import correctly.
This helps catch issues with missing dependencies or import errors early.
"""

import pytest

def test_core_import():
    """
    Test parsers import correctly
    """

    from parsers import parse_fit
    from parsers import parse_gpx
    from parsers import parse_gz

def test_3rd_party_imports():
    """
    Test 3rd party imports work correctly
    """

    from sklearn.ensemble import RandomForestClassifier
    RandomForestClassifier()

    import streamlit

    import gpxpy
    gpxpy.parse("<gpx></gpx>")  # not just import — actually invoke the parser

    import fitparse
    fitparse.FitFile  # access a class to confirm the C extension loaded

    import magic
    magic.from_buffer(b"test")  # requires libmagic system lib — often breaks on fresh installs

    import duckdb
    con = duckdb.connect()
    con.execute("SELECT 42").fetchone()

    import pandas as pd
    import pyarrow as pa
    import pyarrow.parquet as pq
    import tempfile, os
