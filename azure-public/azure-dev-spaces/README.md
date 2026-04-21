# AzureDevSpaces Bicep Module

Azure service tag: **AzureDevSpaces**

## Overview

This directory contains Bicep variable files for the **AzureDevSpaces** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureDevSpaces.bicep** - Global/cloud-wide IP address ranges
- **region/AzureDevSpaces_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureDevSpaces module to access all IP ranges for this service tag:

```bicep
import * as azuredevspaces from './AzureDevSpaces.bicep'

// Use the variable in your template
var allowedIPs = azuredevspaces.AzureDevSpaces
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuredevspacesEastUS from './region/AzureDevSpaces_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuredevspacesEastUS.AzureDevSpaces_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `AustraliaEast`
- `AustraliaSoutheast`
- `CanadaCentral`
- `CanadaEast`
- `CentralUS`
- `EastAsia`
- `EastUS`
- `EastUS2`
- `EastUS2EUAP`
- `JapanEast`
- `NorthEurope`
- `SouthCentralUS`
- `SoutheastAsia`
- `UKSouth`
- `WestCentralUS`
- `WestEurope`
- `WestUS`
- `WestUS2`

Total regional variants: 18


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureDevSpaces
- **Module Directory**: azure-dev-spaces
