# AzurePortal Bicep Module

Azure service tag: **AzurePortal**

## Overview

This directory contains Bicep variable files for the **AzurePortal** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzurePortal.bicep** - Global/cloud-wide IP address ranges
- **region/AzurePortal_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzurePortal module to access all IP ranges for this service tag:

```bicep
import * as azureportal from './AzurePortal.bicep'

// Use the variable in your template
var allowedIPs = azureportal.AzurePortal
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureportalEastUS from './region/AzurePortal_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureportalEastUS.AzurePortal_EastUS
```

### From GitHub Container Registry (GHCR)

You can also import this module directly from GHCR:

`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-portal/azure-portal:latest`

Example regional module:
`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-portal/region/azure-portal-australia-central:latest`

## Available Regions

This module includes regional variants for the following Azure regions:

- `AustraliaCentral`
- `AustraliaCentral2`
- `AustraliaEast`
- `AustraliaSoutheast`
- `AustriaEast`
- `BelgiumCentral`
- `BrazilSouth`
- `BrazilSoutheast`
- `CanadaCentral`
- `CanadaEast`
- `CentralIndia`
- `CentralUS`
- `CentralUSEUAP`
- `ChileCentral`
- `DenmarkEast`
- `EastAsia`
- `EastUS`
- `EastUS2`
- `EastUS2EUAP`
- `EastUS3`
- `EastUSSTG`
- `FranceCentral`
- `FranceSouth`
- `GermanyNorth`
- `GermanyWestCentral`
- `IndiaSouthCentral`
- `IndonesiaCentral`
- `IsraelCentral`
- `IsraelNorthwest`
- `ItalyNorth`
- `JapanEast`
- `JapanWest`
- `JioIndiaCentral`
- `JioIndiaWest`
- `KoreaCentral`
- `KoreaSouth`
- `MalaysiaSouth`
- `MalaysiaWest`
- `MexicoCentral`
- `NewZealandNorth`
- `NorthCentralUS`
- `NorthEurope`
- `NortheastUS5`
- `NorwayEast`
- `NorwayWest`
- `PolandCentral`
- `QatarCentral`
- `SouthAfricaNorth`
- `SouthAfricaWest`
- `SouthCentralUS`
- `SouthCentralUS2`
- `SouthCentralUSSTG`
- `SouthIndia`
- `SoutheastAsia`
- `SoutheastUS`
- `SoutheastUS3`
- `SoutheastUS5`
- `SouthwestUS`
- `SpainCentral`
- `SwedenCentral`
- `SwedenSouth`
- `SwitzerlandNorth`
- `SwitzerlandWest`
- `TaiwanNorth`
- `TaiwanNorthwest`
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

Total regional variants: 75


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzurePortal
- **Module Directory**: azure-portal
