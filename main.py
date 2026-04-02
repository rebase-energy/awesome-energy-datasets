import json


CATEGORY_FIELDS = ["data_type", "energy_sector", "format", "coverage"]
REQUIRED_FIELDS = ["name", "description"] + CATEGORY_FIELDS + ["links"]
TABLE_HEADERS = ["name", "description", "data_type", "energy_sector", "format", "coverage", "links"]


def load_json(path):
    with open(path) as f:
        return json.load(f)


def validate(data, mapping):
    for entry in data:
        for field in REQUIRED_FIELDS:
            if field not in entry:
                raise ValueError(f"Entry '{entry.get('name', '?')}' missing field '{field}'")

        for field in CATEGORY_FIELDS:
            for value in entry[field]:
                if value not in mapping[field]:
                    raise ValueError(
                        f"Entry '{entry['name']}': unknown {field} value '{value}'. "
                        f"Valid values: {list(mapping[field].keys())}"
                    )


def sort_data(data):
    data.sort(key=lambda e: e["name"].lower())
    for entry in data:
        for field in CATEGORY_FIELDS:
            entry[field].sort()


def format_header(field):
    return field.replace("_", " ").title()


def convert_table(data, mapping):
    headers = [format_header(h) for h in TABLE_HEADERS]
    header_row = "| " + " | ".join(headers) + " |"

    alignments = []
    for h in TABLE_HEADERS:
        if h in CATEGORY_FIELDS:
            alignments.append(":---:")
        else:
            alignments.append(":---")
    separator_row = "| " + " | ".join(alignments) + " |"

    rows = [header_row, separator_row]
    for entry in data:
        cells = []
        for h in TABLE_HEADERS:
            if h == "name":
                cells.append(f"`{entry['name']}`")
            elif h == "description":
                cells.append(entry["description"])
            elif h in CATEGORY_FIELDS:
                emojis = " ".join(mapping[h][v] for v in entry[h])
                cells.append(emojis)
            elif h == "links":
                link_parts = []
                for key, url in entry["links"].items():
                    link_parts.append(f"[[{key}]]({url})")
                cells.append(", ".join(link_parts))
        rows.append("| " + " | ".join(cells) + " |")

    return "\n".join(rows)


def custom_json_dump(data):
    lines = ["["]
    for i, entry in enumerate(data):
        lines.append("  {")
        keys = list(entry.keys())
        for j, key in enumerate(keys):
            value = entry[key]
            comma = "," if j < len(keys) - 1 else ""
            if isinstance(value, list):
                items = ", ".join(f'"{v}"' for v in value)
                lines.append(f'    "{key}": [{items}]{comma}')
            elif isinstance(value, dict):
                lines.append(f'    "{key}": {{')
                dict_keys = list(value.keys())
                for k, dk in enumerate(dict_keys):
                    dcomma = "," if k < len(dict_keys) - 1 else ""
                    lines.append(f'      "{dk}": "{value[dk]}"{dcomma}')
                lines.append(f"    }}{comma}")
            else:
                lines.append(f'    "{key}": "{value}"{comma}')
        entry_comma = "," if i < len(data) - 1 else ""
        lines.append(f"  }}{entry_comma}")
    lines.append("]")
    return "\n".join(lines) + "\n"


def main():
    mapping = load_json("mapping.json")
    data = load_json("data.json")

    validate(data, mapping)
    sort_data(data)

    # Write sorted data back
    with open("data.json", "w") as f:
        f.write(custom_json_dump(data))

    # Generate table
    table = convert_table(data, mapping)
    with open("dataset_table.md", "w") as f:
        f.write(table + "\n")

    # Insert into template
    with open("README_no_table.md") as f:
        template = f.read()

    readme = template.replace("<!-- table_placeholder -->", table)
    with open("README.md", "w") as f:
        f.write(readme)

    print(f"Generated README.md with {len(data)} datasets.")


if __name__ == "__main__":
    main()
