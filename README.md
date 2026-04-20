# azure-ip-addresses-bicep

Azure IP Addresses in Bicep format — automatically kept up to date.

## Overview

This repository contains Bicep variable files that list every Azure IP address prefix, grouped by [Azure Service Tag](https://learn.microsoft.com/azure/virtual-network/service-tags-overview).  
The files are re-generated automatically each week as Microsoft publishes updated Service Tag lists.

> **Important:** These are **variable library files**, not stand-alone deployable Bicep templates. They must be consumed by your own Bicep templates as described in [How to use the Bicep files](#how-to-use-the-bicep-files).

## Prerequisites

- **Bicep CLI ≥ 0.21** — required for compile-time `import` support.

## Generated files

| File | Source cloud |
|------|-------------|
| `ServiceTags_Public.bicep` | Azure Public Cloud |
| `ServiceTags_China.bicep` | Azure China Cloud |
| `ServiceTags_AzureGovernment.bicep` | Azure US Government Cloud |
| `ServiceTags_AzureGermany.bicep` | Azure Germany Cloud |

Each file contains one Bicep `var` per service tag. The variable name is the
service-tag name (dots and hyphens replaced by underscores) and its value is an
array of CIDR address prefixes, for example:

```bicep
var AzureActiveDirectory = [
  '20.190.128.0/18'
  '40.126.0.0/18'
  // …
]
```

## How to use the Bicep files

These files are **variable library files** — they contain only `var` declarations and are not deployable on their own. Import a file directly into your Bicep template using the compile-time `import` syntax and reference any variable by name.

```bicep
import * as serviceTags from './ServiceTags_Public.bicep'

// serviceTags.<VariableName> is an array of CIDR strings, e.g.:
// serviceTags.LogicApps  →  [ '13.65.86.0/24', '13.65.93.0/24', … ]
```

Adapt the import path to match where you have placed `ServiceTags_Public.bicep` relative to your template.

## Using the modules from the registry

The Bicep files are published to the **GitHub Container Registry (GHCR)** as OCI artifacts after every update, so you can consume them directly from the registry without copying any files into your project.

### Available modules

| Module | Registry reference |
|--------|--------------------|
| Azure Public Cloud | `br:ghcr.io/rdeveen/azure-ip-addresses-bicep/servicetags-public:latest` |
| Azure China Cloud | `br:ghcr.io/rdeveen/azure-ip-addresses-bicep/servicetags-china:latest` |
| Azure US Government Cloud | `br:ghcr.io/rdeveen/azure-ip-addresses-bicep/servicetags-azuregovernment:latest` |
| Azure Germany Cloud | `br:ghcr.io/rdeveen/azure-ip-addresses-bicep/servicetags-azuregermany:latest` |

Modules are also tagged by date (`YYYYMMDD`) for pinning to a specific release, e.g. `servicetags-public:20260420`.

### Prerequisites

- **Bicep CLI ≥ 0.21** — required for `import` support and OCI registry consumption.
- The packages are public, so **no credentials are required** to pull them. You can reference these modules directly without any extra configuration.
- Optionally, add `ghcr.io` as a trusted registry in a `bicepconfig.json` (see the alias example below) to enable shorter import paths.

### Simple example

Consume the Public Cloud module directly from the registry — no local file copy needed:

```bicep
// main.bicep
module publicTags 'br:ghcr.io/rdeveen/azure-ip-addresses-bicep/servicetags-public:latest' = {
  name: 'publicTags'
  params: {}
}

// Access a service-tag variable via the module outputs
// NOTE: Because the Bicep files use 'var' (not 'output'), wrap the variable
// in an intermediate module or use the import pattern below.
```

The recommended approach for Bicep ≥ 0.21 is the `import` syntax. First, define an alias in `bicepconfig.json`:

```json
// bicepconfig.json
{
  "moduleAliases": {
    "br": {
      "azureIpAddresses": {
        "registry": "ghcr.io",
        "modulePath": "rdeveen/azure-ip-addresses-bicep"
      }
    }
  }
}
```

Then import the module using the alias:

```bicep
// With alias defined in bicepconfig.json:
import * as serviceTags from 'br/azureIpAddresses:servicetags-public:latest'

var allowedRanges = serviceTags.AzureMonitor
```

### How it works (registry)

The GitHub Actions workflow re-publishes updated modules to GHCR automatically each week, right after committing the refreshed Bicep files. The `latest` tag always points to the most recent build, while dated tags (e.g. `20260420`) allow you to pin to a specific release for reproducible deployments.

## Sample — Logic App (Consumption) with firewall and IP whitelisting

This example deploys a Logic App (Consumption) inside an App Service Environment-style access restriction. An **IP restriction** on the Logic App allows inbound calls only from the Azure **LogicApps** service-tag prefixes (e.g. managed connector infrastructure) and from **AzureMonitor** (for alert webhooks). All other traffic is denied.

```bicep
import * as serviceTags from './ServiceTags_Public.bicep'

param location string = resourceGroup().location
param logicAppName string = 'my-logic-app'

// Combine the IP ranges you want to whitelist
var allowedPrefixes = concat(serviceTags.LogicApps, serviceTags.AzureMonitor)

// Build the ipSecurityRestrictions array from the combined prefix list
var ipRestrictions = [for (prefix, i) in allowedPrefixes: {
  ipAddress: prefix
  action: 'Allow'
  priority: 100 + i
  name: 'Allow-${i}'
}]

resource logicAppPlan 'Microsoft.Web/serverfarms@2023-01-01' = {
  name: '${logicAppName}-plan'
  location: location
  sku: {
    name: 'WS1'
    tier: 'WorkflowStandard'
  }
  properties: {}
}

resource logicApp 'Microsoft.Web/sites@2023-01-01' = {
  name: logicAppName
  location: location
  kind: 'functionapp,workflowapp'
  properties: {
    serverFarmId: logicAppPlan.id
    siteConfig: {
      // Deny all traffic that does not match an Allow rule
      ipSecurityRestrictionsDefaultAction: 'Deny'
      ipSecurityRestrictions: ipRestrictions
    }
  }
}
```

> **Tip:** Replace `serviceTags.LogicApps` and `serviceTags.AzureMonitor` with whichever service-tag variables your scenario requires. All available variable names match the Azure Service Tag names (dots and hyphens replaced by underscores).

## How it works

The workflow file [`.github/workflows/update-servicetags.yml`](.github/workflows/update-servicetags.yml):

1. Runs every **Monday at 06:00 UTC** (and can be triggered manually).
2. Fetches the latest Service Tags JSON for each cloud from the Microsoft Download Center.
3. Calls [`scripts/convert-to-bicep.py`](scripts/convert-to-bicep.py) to convert each JSON file into a Bicep variable file.
4. Commits and pushes any updated files back to the repository.
5. Publishes the four Bicep modules to GHCR as OCI artifacts (tagged with the current date and `latest`).

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
