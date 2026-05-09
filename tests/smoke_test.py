import gpxpy
gpxpy.parse("<gpx></gpx>")  # not just import — actually invoke the parser
print("gpxpy smoke test passed")

import fitparse
fitparse.FitFile  # access a class to confirm the C extension loaded
print("fitparse smoke test passed")

import magic
magic.from_buffer(b"test")  # requires libmagic system lib — often breaks on fresh installs
print("magic smoke test passed")

import duckdb
con = duckdb.connect()
con.execute("SELECT 42").fetchone()
print("duckdb smoke test passed")

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import tempfile, os

df = pd.DataFrame({"a": [1, 2, 3]})
with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as f:
    pq.write_table(pa.Table.from_pandas(df), f.name)
    result = pq.read_table(f.name).to_pandas()
    assert len(result) == 3
    print("pandas/pyarrow smoke test passed")
    os.unlink(f.name)

import streamlit  # just the import — you can't run the app but confirm it loads
print("streamlit smoke test passed")

from sklearn.ensemble import RandomForestClassifier
RandomForestClassifier()
print("sklearn smoke test passed")