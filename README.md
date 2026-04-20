# azure-ip-addresses-bicep

Azure IP Addresses in Bicep format — automatically kept up to date.

## Overview

This repository contains Bicep variable files that list every Azure IP address prefix, grouped by [Azure Service Tag](https://learn.microsoft.com/azure/virtual-network/service-tags-overview).  
The files are re-generated automatically each week as Microsoft publishes updated Service Tag lists.

> **Important:** These are **variable library files**, not stand-alone deployable Bicep templates. They must be consumed by your own Bicep templates using one of the patterns described in [How to use the Bicep files](#how-to-use-the-bicep-files).

## Prerequisites

- **Bicep CLI ≥ 0.21** — required for compile-time `import` support (Pattern B and Pattern C below).
- For older Bicep versions, use the copy-paste / inline approach (Pattern A).

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

These files are **variable library files** — they contain only `var` declarations and are not deployable on their own. Choose one of the following patterns to consume them in your Bicep templates.

### Pattern A — Copy-paste / inline the variables

Copy the relevant `var` block from the file directly into your own Bicep template and reference it inline. This approach works with any Bicep version.

```bicep
// main.bicep – copy the var block you need from ServiceTags_Public.bicep
var AzureActiveDirectory = [
  '20.190.128.0/18'
  '40.126.0.0/18'
  // … paste remaining prefixes here
]

resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = {
  name: 'my-nsg'
  location: resourceGroup().location
  properties: {
    securityRules: [
      {
        name: 'Allow-AAD-Outbound'
        properties: {
          priority: 100
          direction: 'Outbound'
          access: 'Allow'
          protocol: '*'
          sourceAddressPrefix: '*'
          sourcePortRange: '*'
          destinationAddressPrefixes: AzureActiveDirectory
          destinationPortRange: '443'
        }
      }
    ]
  }
}
```

### Pattern B — Use as a Bicep module (wrapper approach)

Because the files only contain `var` declarations, they cannot be used as modules directly. Create a thin wrapper module that exposes the needed variables as `output` values, then call that module from your parent template.

**Step 1 — Create a wrapper module** (`modules/servicetags-public.bicep`):

```bicep
// Thin wrapper so the vars can be consumed as a Bicep module output
import * as st from '../ServiceTags_Public.bicep'  // Bicep compile-time import (Bicep ≥ 0.21)

output actionGroup array = st.ActionGroup
output azureActiveDirectory array = st.AzureActiveDirectory
output applicationInsightsAvailability array = st.ApplicationInsightsAvailability
```

**Step 2 — Call the wrapper from your parent template** (`main.bicep`):

```bicep
module serviceTags './modules/servicetags-public.bicep' = {
  name: 'serviceTags'
}

resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = {
  name: 'my-nsg'
  location: resourceGroup().location
  properties: {
    securityRules: [
      {
        name: 'Allow-AAD-Outbound'
        properties: {
          priority: 100
          direction: 'Outbound'
          access: 'Allow'
          protocol: '*'
          sourceAddressPrefix: '*'
          sourcePortRange: '*'
          destinationAddressPrefixes: serviceTags.outputs.azureActiveDirectory
          destinationPortRange: '443'
        }
      }
    ]
  }
}
```

> **Note:** Bicep compile-time imports (`import`) require **Bicep CLI ≥ 0.21** / **Azure Bicep extension ≥ 0.21**.

### Pattern C — Direct compile-time import (Bicep ≥ 0.21, preferred)

Import the variable file directly into your consuming template using the `import` syntax. This is the simplest and most direct approach.

```bicep
import * as serviceTags from './ServiceTags_Public.bicep'

// Use AzureActiveDirectory prefixes in an NSG rule
resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = {
  name: 'my-nsg'
  location: resourceGroup().location
  properties: {
    securityRules: [
      {
        name: 'Allow-AAD-Outbound'
        properties: {
          priority: 100
          direction: 'Outbound'
          access: 'Allow'
          protocol: '*'
          sourceAddressPrefix: '*'
          sourcePortRange: '*'
          destinationAddressPrefixes: serviceTags.AzureActiveDirectory
          destinationPortRange: '443'
        }
      }
    ]
  }
}
```

## Samples

The examples below all use Pattern C (direct compile-time import). Adapt the import path to match where you have placed `ServiceTags_Public.bicep` relative to your template.

### Sample 1 — NSG rule allowing outbound to Azure Active Directory

```bicep
import * as serviceTags from './ServiceTags_Public.bicep'

resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = {
  name: 'my-nsg'
  location: resourceGroup().location
  properties: {
    securityRules: [
      {
        name: 'Allow-AAD-Outbound'
        properties: {
          priority: 100
          direction: 'Outbound'
          access: 'Allow'
          protocol: '*'
          sourceAddressPrefix: '*'
          sourcePortRange: '*'
          destinationAddressPrefixes: serviceTags.AzureActiveDirectory
          destinationPortRange: '443'
        }
      }
    ]
  }
}
```

### Sample 2 — NSG rule allowing inbound from Action Group (Azure Monitor alerts)

```bicep
import * as serviceTags from './ServiceTags_Public.bicep'

resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = {
  name: 'my-nsg'
  location: resourceGroup().location
  properties: {
    securityRules: [
      {
        name: 'Allow-ActionGroup-Inbound'
        properties: {
          priority: 200
          direction: 'Inbound'
          access: 'Allow'
          protocol: 'Tcp'
          sourceAddressPrefixes: serviceTags.ActionGroup
          sourcePortRange: '*'
          destinationAddressPrefix: '*'
          destinationPortRange: '443'
        }
      }
    ]
  }
}
```

### Sample 3 — Azure Firewall policy rule collection using Application Insights Availability prefixes

```bicep
import * as serviceTags from './ServiceTags_Public.bicep'

resource firewallPolicy 'Microsoft.Network/firewallPolicies@2023-09-01' = {
  name: 'my-firewall-policy'
  location: resourceGroup().location
  properties: {
    sku: { tier: 'Standard' }
  }
}

resource ruleCollectionGroup 'Microsoft.Network/firewallPolicies/ruleCollectionGroups@2023-09-01' = {
  parent: firewallPolicy
  name: 'DefaultNetworkRuleCollectionGroup'
  properties: {
    priority: 200
    ruleCollections: [
      {
        ruleCollectionType: 'FirewallPolicyFilterRuleCollection'
        name: 'Allow-AppInsights-Availability'
        priority: 100
        action: { type: 'Allow' }
        rules: [
          {
            ruleType: 'NetworkRule'
            name: 'AppInsightsAvailabilityTest'
            ipProtocols: [ 'TCP' ]
            sourceAddresses: [ '*' ]
            destinationAddresses: serviceTags.ApplicationInsightsAvailability
            destinationPorts: [ '443' ]
          }
        ]
      }
    ]
  }
}
```

### Sample 4 — Passing prefixes as a parameter to a child module

```bicep
import * as serviceTags from './ServiceTags_Public.bicep'

module webAppFirewall './modules/waf-rules.bicep' = {
  name: 'waf-rules'
  params: {
    allowedSourcePrefixes: serviceTags.AzureActiveDirectory
  }
}
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
