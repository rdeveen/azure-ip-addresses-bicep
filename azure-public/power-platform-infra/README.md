# PowerPlatformInfra Bicep Module

Azure service tag: **PowerPlatformInfra**

## Overview

This directory contains Bicep variable files for the **PowerPlatformInfra** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **PowerPlatformInfra.bicep** - Global/cloud-wide IP address ranges
- **region/PowerPlatformInfra_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global PowerPlatformInfra module to access all IP ranges for this service tag:

```bicep
import * as powerplatforminfra from './PowerPlatformInfra.bicep'

// Use the variable in your template
var allowedIPs = powerplatforminfra.PowerPlatformInfra
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as powerplatforminfraEastUS from './region/PowerPlatformInfra_EastUS.bicep'

// Use the regional variable
var eastUSIPs = powerplatforminfraEastUS.PowerPlatformInfra_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `AustraliaEast`
- `AustraliaSoutheast`
- `BrazilSouth`
- `BrazilSoutheast`
- `CanadaCentral`
- `CanadaEast`
- `CentralIndia`
- `CentralUS`
- `EastAsia`
- `EastUS`
- `EastUS2`
- `FranceCentral`
- `FranceSouth`
- `GermanyNorth`
- `GermanyWestCentral`
- `IndonesiaCentral`
- `IsraelCentral`
- `ItalyNorth`
- `JapanEast`
- `JapanWest`
- `KoreaCentral`
- `KoreaSouth`
- `NewZealandNorth`
- `NorthEurope`
- `NorwayEast`
- `NorwayWest`
- `PolandCentral`
- `QatarCentral`
- `SouthAfricaNorth`
- `SouthAfricaWest`
- `SouthCentralUS`
- `SouthIndia`
- `SoutheastAsia`
- `SpainCentral`
- `SwedenCentral`
- `SwitzerlandNorth`
- `SwitzerlandWest`
- `UAECentral`
- `UAENorth`
- `UKSouth`
- `UKWest`
- `WestCentralUS`
- `WestEurope`
- `WestUS`
- `WestUS2`

Total regional variants: 45


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: PowerPlatformInfra
- **Module Directory**: power-platform-infra
