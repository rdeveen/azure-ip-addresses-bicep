# azure-ip-addresses-bicep

Azure IP Addresses in Bicep format — automatically kept up to date.

## Overview

This repository contains Bicep variable files that list every Azure IP address prefix, grouped by [Azure Service Tag](https://learn.microsoft.com/azure/virtual-network/service-tags-overview).  
The files are re-generated automatically each week as Microsoft publishes updated Service Tag lists.

## Generated files

| File | Source cloud |
|------|-------------|
| `ServiceTags_Public.bicep` | Azure Public Cloud |
| `ServiceTags_China.bicep` | Azure China Cloud |
| `ServiceTags_AzureGovernment.bicep` | Azure US Government Cloud |
| `ServiceTags_AzureGermany.bicep` | Azure Germany Cloud |

Each file contains one Bicep `var` per service tag.  The variable name is the
service-tag name (dots and hyphens replaced by underscores) and its value is an
array of CIDR address prefixes, for example:

```bicep
var AzureActiveDirectory = [
  '20.190.128.0/18'
  '40.126.0.0/18'
  // …
]
```

## How it works

The workflow file [`.github/workflows/update-servicetags.yml`](.github/workflows/update-servicetags.yml):

1. Runs every **Monday at 06:00 UTC** (and can be triggered manually).
2. Fetches the latest Service Tags JSON for each cloud from the Microsoft Download Center.
3. Calls [`scripts/convert-to-bicep.py`](scripts/convert-to-bicep.py) to convert each JSON file into a Bicep variable file.
4. Commits and pushes any updated files back to the repository.

## Generating files locally

```bash
# Download the JSON (replace the URL with the current one from the Microsoft Download Center)
curl -L "https://download.microsoft.com/download/7/1/d/71d86715-5596-4529-9b13-da13a5de5b63/ServiceTags_Public_20260413.json" \
     -o ServiceTags_Public.json

# Convert to Bicep
python scripts/convert-to-bicep.py ServiceTags_Public.json ServiceTags_Public.bicep
```

## Source URLs (Microsoft Download Center)

| Cloud | Download page |
|-------|--------------|
| Public | <https://www.microsoft.com/en-us/download/details.aspx?id=56519> |
| China | <https://www.microsoft.com/en-us/download/details.aspx?id=57062> |
| US Government | <https://www.microsoft.com/en-us/download/details.aspx?id=57063> |
| Germany | <https://www.microsoft.com/en-us/download/details.aspx?id=57064> |
