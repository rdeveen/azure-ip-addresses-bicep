#!/usr/bin/env python3
"""
Convert an Azure Service Tags JSON file into a Bicep variable file.

Usage:
    python convert-to-bicep.py <input.json> <output.bicep>
"""

import json
import re
import sys
import os
from datetime import datetime, timezone


def to_bicep_identifier(name: str) -> str:
    """Return a valid Bicep identifier derived from *name*.

    Rules applied:
    - Replace every character that is not a letter, digit, or underscore with
      an underscore.
    - If the resulting string starts with a digit, prepend an underscore so
      that the identifier starts with a letter or underscore (Bicep requires
      identifiers to begin with a letter or underscore).
    """
    sanitized = re.sub(r"[^A-Za-z0-9_]", "_", name)
    if sanitized and sanitized[0].isdigit():
        sanitized = "_" + sanitized
    return sanitized or "_"


def json_to_bicep(input_path: str, output_path: str) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    cloud = data.get("cloud", "Unknown")
    change_number = data.get("changeNumber", "Unknown")
    values = data.get("values", [])

    source_filename = os.path.basename(input_path)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "// Auto-generated file – do not edit manually.",
        f"// Generated at : {generated_at}",
        f"// Source file  : {source_filename}",
        f"// Cloud        : {cloud}",
        f"// Change number: {change_number}",
        "",
    ]

    for entry in values:
        name = entry.get("name", "")
        props = entry.get("properties", {})
        prefixes = props.get("addressPrefixes", [])

        safe_name = to_bicep_identifier(name)

        lines.append(f"var {safe_name} = [")
        for prefix in prefixes:
            lines.append(f"  '{prefix}'")
        lines.append("]")
        lines.append("")

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    print(f"Written {len(values)} service-tag variables to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: convert-to-bicep.py <input.json> <output.bicep>", file=sys.stderr)
        sys.exit(1)

    json_to_bicep(sys.argv[1], sys.argv[2])
