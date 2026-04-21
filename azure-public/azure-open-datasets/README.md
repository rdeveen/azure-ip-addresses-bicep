# AzureOpenDatasets Bicep Module

Azure service tag: **AzureOpenDatasets**

## Overview

This directory contains Bicep variable files for the **AzureOpenDatasets** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureOpenDatasets.bicep** - Global/cloud-wide IP address ranges
- **region/AzureOpenDatasets_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureOpenDatasets module to access all IP ranges for this service tag:

```bicep
import * as azureopendatasets from './AzureOpenDatasets.bicep'

// Use the variable in your template
var allowedIPs = azureopendatasets.AzureOpenDatasets
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureopendatasetsEastUS from './region/AzureOpenDatasets_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureopendatasetsEastUS.AzureOpenDatasets_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `AustraliaCentral`
- `AustraliaCentral2`
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
- `EastUSSTG`
- `FranceCentral`
- `FranceSouth`
- `GermanyNorth`
- `GermanyWestCentral`
- `JapanEast`
- `JapanWest`
- `JioIndiaCentral`
- `KoreaCentral`
- `KoreaSouth`
- `NorthCentralUS`
- `NorthEurope`
- `NorwayEast`
- `NorwayWest`
- `SouthAfricaNorth`
- `SouthAfricaWest`
- `SouthCentralUS`
- `SouthCentralUSSTG`
- `SouthIndia`
- `SoutheastAsia`
- `SwedenCentral`
- `SwedenSouth`
- `SwitzerlandNorth`
- `SwitzerlandWest`
- `UAECentral`
- `UAENorth`
- `UKSouth`
- `UKWest`
- `WestCentralUS`
- `WestEurope`
- `WestIndia`
- `WestUS`
- `WestUS2`
- `WestUS3`

Total regional variants: 48


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureOpenDatasets
- **Module Directory**: azure-open-datasets
