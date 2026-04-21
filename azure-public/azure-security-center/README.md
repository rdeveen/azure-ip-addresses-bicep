# AzureSecurityCenter Bicep Module

Azure service tag: **AzureSecurityCenter**

## Overview

This directory contains Bicep variable files for the **AzureSecurityCenter** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureSecurityCenter.bicep** - Global/cloud-wide IP address ranges
- **region/AzureSecurityCenter_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureSecurityCenter module to access all IP ranges for this service tag:

```bicep
import * as azuresecuritycenter from './AzureSecurityCenter.bicep'

// Use the variable in your template
var allowedIPs = azuresecuritycenter.AzureSecurityCenter
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuresecuritycenterEastUS from './region/AzureSecurityCenter_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuresecuritycenterEastUS.AzureSecurityCenter_EastUS
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

Total regional variants: 62


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureSecurityCenter
- **Module Directory**: azure-security-center
