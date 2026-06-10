
from lxml import etree
import pandas as pd
from datetime import datetime
from pipeline.utils.parse_utils import xml_setup


def extract_metadata(file_path, root, ns) -> dict:
    name_elem = root.find(".//d:name", ns)
    activity_name = name_elem.text if name_elem is not None else None

    type_elem = root.find(".//d:type", ns)
    activity_type = type_elem.text if type_elem is not None else None

    first_time = root.find(".//d:trkpt/d:time", ns)

    start_time = None
    if first_time is not None:
        start_time = datetime.fromisoformat(
            first_time.text.replace("Z", "+00:00")
        )

    metadata = {
        "activity_name" : activity_name,
        "activity_type" : activity_type,
        "start_time" : start_time,
        "file_name" : file_path.split("/")[-1]
    }

    return metadata

def parse_gpx(file_path) -> tuple[pd.DataFrame, dict]:
    ns = xml_setup()

    tree = etree.parse(file_path)
    root = tree.getroot()

    data = []

    for pt in root.xpath("//d:trkpt", namespaces=ns):
        lat = float(pt.get("lat"))
        lon = float(pt.get("lon"))

        ele = pt.find("d:ele", ns)
        time = pt.find("d:time", ns)

        # Extensions
        hr = pt.find(".//gpxtpx:hr", ns)
        cad = pt.find(".//gpxtpx:cad", ns)
        power = pt.find(".//d:power", ns)

        data.append({
            "lat": lat,
            "lon": lon,
            "elevation": float(ele.text) if ele is not None else None,
            "time": time.text if time is not None else None,
            "heart_rate": int(hr.text) if hr is not None else None,
            "cadence": int(cad.text) if cad is not None else None,
            "power": int(power.text) if power is not None else None
        })

    df = pd.DataFrame(data)

    metadata = extract_metadata(file_path, root, ns)

    print(df.head())
    print(metadata)

    return df, metadata


if __name__ == "__main__":
    file_path = r"/Users/rishabagarwal/Desktop/projects/activity_dashboards/tests/fixtures/8335406398.gpx"
    parse_gpx(file_path)