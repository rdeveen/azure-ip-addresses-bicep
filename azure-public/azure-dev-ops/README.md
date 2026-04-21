# AzureDevOps Bicep Module

Azure service tag: **AzureDevOps**

## Overview

This directory contains Bicep variable files for the **AzureDevOps** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureDevOps.bicep** - Global/cloud-wide IP address ranges
- **region/AzureDevOps_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureDevOps module to access all IP ranges for this service tag:

```bicep
import * as azuredevops from './AzureDevOps.bicep'

// Use the variable in your template
var allowedIPs = azuredevops.AzureDevOps
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuredevopsEastUS from './region/AzureDevOps_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuredevopsEastUS.AzureDevOps_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `AustraliaEast`
- `AustraliaSoutheast`
- `BrazilSouth`
- `CanadaCentral`
- `CanadaEast`
- `CentralIndia`
- `CentralUS`
- `CentralUSEUAP`
- `EastAsia`
- `EastUS`
- `EastUS2`
- `EastUS2EUAP`
- `NorthCentralUS`
- `NorthEurope`
- `SouthCentralUS`
- `SouthIndia`
- `SoutheastAsia`
- `SwedenCentral`
- `SwedenSouth`
- `UAENorth`
- `UKSouth`
- `UKWest`
- `WestCentralUS`
- `WestEurope`
- `WestUS`
- `WestUS2`
- `WestUS3`

Total regional variants: 27


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureDevOps
- **Module Directory**: azure-dev-ops
