# azure-ip-addresses-bicep

Azure IP Addresses in Bicep format — automatically kept up to date.

## Overview

This repository contains Bicep variable files that list every Azure IP address prefix, grouped by [Azure Service Tag](https://learn.microsoft.com/azure/virtual-network/service-tags-overview).  
The files are re-generated automatically each week as Microsoft publishes updated Service Tag lists.

Each service tag is stored in its own `.bicep` file (one variable per file) to stay within the Bicep compiler limit of 512 variables per file.

> **Important:** These are **variable library files**, not stand-alone deployable Bicep templates. They must be consumed by your own Bicep templates as described in [How to use the Bicep files](#how-to-use-the-bicep-files).

## Prerequisites

- **Bicep CLI ≥ 0.21** — required for compile-time `import` support.

## Generated files

Files are organised into cloud-specific directories. Each file contains exactly one `var` declaration for its service tag.

| Directory | Source cloud |
|-----------|-------------|
| `azure-public/` | Azure Public Cloud |
| `azure-china/` | Azure China Cloud |
| `azure-government/` | Azure US Government Cloud |
| `azure-germany/` | Azure Germany Cloud |

Each file is named after the service-tag identifier (dots and hyphens replaced by underscores), for example `azure-public/ActionGroup.bicep`:

```bicep
// azure-public/ActionGroup.bicep
var ActionGroup = [
  '4.145.74.52/30'
  '4.149.254.68/30'
  // …
]
```

## How to use the Bicep files

These files are **variable library files** — they contain only `var` declarations and are not deployable on their own. Import a specific service-tag file directly into your Bicep template using the compile-time `import` syntax.

```bicep
import * as actionGroup from './azure-public/ActionGroup.bicep'
import * as azureMonitor from './azure-public/AzureMonitor.bicep'

// actionGroup.ActionGroup is an array of CIDR strings
// azureMonitor.AzureMonitor is an array of CIDR strings
```

Adapt the import path to match where you have placed the files relative to your template.

## Using the modules from the registry

The Bicep files are published to the **GitHub Container Registry (GHCR)** as OCI artifacts after every update, so you can consume them directly from the registry without copying any files into your project.

Each service tag has its own module in the registry. The module path follows the pattern:

```
br:ghcr.io/rdeveen/azure-ip-addresses-bicep/<cloud>/<service-tag-kebab>:latest
```

Where `<cloud>` is one of `azure-public`, `azure-china`, `azure-government`, or `azure-germany`, and `<service-tag-kebab>` is the service-tag name converted to kebab-case (e.g. `ActionGroup` → `action-group`).

### Example registry references

| Service tag | Registry reference |
|------------|-------------------|
| ActionGroup (Public) | `br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/action-group:latest` |
| AzureMonitor (Public) | `br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-monitor:latest` |
| LogicApps (Public) | `br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/logic-apps:latest` |
| AzureActiveDirectory (Public) | `br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-active-directory:latest` |

Modules are also tagged by date (`YYYYMMDD`) for pinning to a specific release, e.g. `action-group:20260420`.

### Prerequisites

- **Bicep CLI ≥ 0.21** — required for `import` support and OCI registry consumption.
- The packages are public, so **no credentials are required** to pull them. You can reference these modules directly without any extra configuration.
- Optionally, add `ghcr.io` as a trusted registry in a `bicepconfig.json` (see the alias example below) to enable shorter import paths.

### Simple example

Import individual service-tag modules directly from the registry:

```bicep
// main.bicep
import * as actionGroup from 'br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/action-group:latest'
import * as azureMonitor from 'br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-monitor:latest'

// actionGroup.ActionGroup and azureMonitor.AzureMonitor are arrays of CIDR strings
```

The recommended approach for Bicep ≥ 0.21 is the `import` syntax with an alias. First, define an alias in `bicepconfig.json`:

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

Then import the modules using the alias:

```bicep
// With alias defined in bicepconfig.json:
import * as actionGroup from 'br/azureIpAddresses:azure-public/action-group:latest'
import * as azureMonitor from 'br/azureIpAddresses:azure-public/azure-monitor:latest'

var allowedRanges = concat(actionGroup.ActionGroup, azureMonitor.AzureMonitor)
```

### How it works (registry)

The GitHub Actions workflow re-publishes updated modules to GHCR automatically each week, right after committing the refreshed Bicep files. The `latest` tag always points to the most recent build, while dated tags (e.g. `20260420`) allow you to pin to a specific release for reproducible deployments.

## Sample — Logic App (Consumption) with firewall and IP whitelisting

This example deploys a Logic App (Consumption) inside an App Service Environment-style access restriction. An **IP restriction** on the Logic App allows inbound calls only from the Azure **LogicApps** service-tag prefixes (e.g. managed connector infrastructure) and from **AzureMonitor** (for alert webhooks). All other traffic is denied.

```bicep
import * as logicApps from 'br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/logic-apps:latest'
import * as azureMonitor from 'br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-monitor:latest'

param location string = resourceGroup().location
param logicAppName string = 'my-logic-app'

// Combine the IP ranges you want to whitelist
var allowedPrefixes = concat(logicApps.LogicApps, azureMonitor.AzureMonitor)

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

> **Tip:** Replace `logicApps.LogicApps` and `azureMonitor.AzureMonitor` with whichever service-tag modules your scenario requires. All available variable names match the Azure Service Tag names (dots and hyphens replaced by underscores).

## How it works

The workflow file [`.github/workflows/update-servicetags.yml`](.github/workflows/update-servicetags.yml):

1. Runs every **Monday at 06:00 UTC** (and can be triggered manually).
2. Fetches the latest Service Tags JSON for each cloud from the Microsoft Download Center.
3. Calls [`scripts/convert-to-bicep.py`](scripts/convert-to-bicep.py) to convert each JSON file into per-tag Bicep variable files inside a cloud-specific directory.
4. Commits and pushes any updated files back to the repository.
5. Publishes every per-tag Bicep module to GHCR as an OCI artifact (tagged with the current date and `latest`).

## Generating files locally

```bash
# Download the JSON (replace the URL with the current one from the Microsoft Download Center)
curl -L "https://download.microsoft.com/download/7/1/d/71d86715-5596-4529-9b13-da13a5de5b63/ServiceTags_Public_20260413.json" \
     -o ServiceTags_Public.json

# Convert to per-tag Bicep files (written to azure-public/)
python scripts/convert-to-bicep.py ServiceTags_Public.json azure-public/
```

## Source URLs (Microsoft Download Center)

| Cloud | Download page |
|-------|--------------|
| Public | <https://www.microsoft.com/en-us/download/details.aspx?id=56519> |
| China | <https://www.microsoft.com/en-us/download/details.aspx?id=57062> |
| US Government | <https://www.microsoft.com/en-us/download/details.aspx?id=57063> |
| Germany | <https://www.microsoft.com/en-us/download/details.aspx?id=57064> |
