# WindowsVirtualDesktop Bicep Module

Azure service tag: **WindowsVirtualDesktop**

## Overview

This directory contains Bicep variable files for the **WindowsVirtualDesktop** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **WindowsVirtualDesktop.bicep** - Global/cloud-wide IP address ranges
- **region/WindowsVirtualDesktop_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global WindowsVirtualDesktop module to access all IP ranges for this service tag:

```bicep
import * as windowsvirtualdesktop from './WindowsVirtualDesktop.bicep'

// Use the variable in your template
var allowedIPs = windowsvirtualdesktop.WindowsVirtualDesktop
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as windowsvirtualdesktopEastUS from './region/WindowsVirtualDesktop_EastUS.bicep'

// Use the regional variable
var eastUSIPs = windowsvirtualdesktopEastUS.WindowsVirtualDesktop_EastUS
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
- `SouthCentralUSSTG`
- `SouthIndia`
- `SoutheastAsia`
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

Total regional variants: 67


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: WindowsVirtualDesktop
- **Module Directory**: windows-virtual-desktop
