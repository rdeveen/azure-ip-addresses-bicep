# AzureEventGrid Bicep Module

Azure service tag: **AzureEventGrid**

## Overview

This directory contains Bicep variable files for the **AzureEventGrid** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureEventGrid.bicep** - Global/cloud-wide IP address ranges
- **region/AzureEventGrid_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureEventGrid module to access all IP ranges for this service tag:

```bicep
import * as azureeventgrid from './AzureEventGrid.bicep'

// Use the variable in your template
var allowedIPs = azureeventgrid.AzureEventGrid
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureeventgridEastUS from './region/AzureEventGrid_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureeventgridEastUS.AzureEventGrid_EastUS
```

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

Total regional variants: 71


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureEventGrid
- **Module Directory**: azure-event-grid
