# AzureSignalR Bicep Module

Azure service tag: **AzureSignalR**

## Overview

This directory contains Bicep variable files for the **AzureSignalR** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureSignalR.bicep** - Global/cloud-wide IP address ranges
- **region/AzureSignalR_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureSignalR module to access all IP ranges for this service tag:

```bicep
import * as azuresignalr from './AzureSignalR.bicep'

// Use the variable in your template
var allowedIPs = azuresignalr.AzureSignalR
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuresignalrEastUS from './region/AzureSignalR_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuresignalrEastUS.AzureSignalR_EastUS
```

### From GitHub Container Registry (GHCR)

You can also import this module directly from GHCR:

`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-signal-r/azure-signal-r:latest`

Example regional module:
`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-signal-r/region/azure-signal-r-australia-central:latest`

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
- `EastAsia`
- `EastUS`
- `EastUS2`
- `EastUS2EUAP`
- `EastUSSTG`
- `FranceCentral`
- `FranceSouth`
- `GermanyNorth`
- `GermanyWestCentral`
- `IndonesiaCentral`
- `IsraelCentral`
- `ItalyNorth`
- `JapanEast`
- `JapanWest`
- `JioIndiaCentral`
- `JioIndiaWest`
- `KoreaCentral`
- `KoreaSouth`
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
- `SouthCentralUSSTG`
- `SouthIndia`
- `SoutheastAsia`
- `SpainCentral`
- `SwedenCentral`
- `SwedenSouth`
- `SwitzerlandNorth`
- `SwitzerlandWest`
- `TaiwanNorth`
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

Total regional variants: 63


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureSignalR
- **Module Directory**: azure-signal-r
