# AzureDataLake Bicep Module

Azure service tag: **AzureDataLake**

## Overview

This directory contains Bicep variable files for the **AzureDataLake** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureDataLake.bicep** - Global/cloud-wide IP address ranges
- **region/AzureDataLake_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureDataLake module to access all IP ranges for this service tag:

```bicep
import * as azuredatalake from './AzureDataLake.bicep'

// Use the variable in your template
var allowedIPs = azuredatalake.AzureDataLake
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuredatalakeEastUS from './region/AzureDataLake_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuredatalakeEastUS.AzureDataLake_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `AustraliaSoutheast`
- `CentralUS`
- `EastUS2`
- `NorthEurope`
- `SoutheastAsia`
- `WestEurope`

Total regional variants: 6


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureDataLake
- **Module Directory**: azure-data-lake
