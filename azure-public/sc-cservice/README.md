# SCCservice Bicep Module

Azure service tag: **SCCservice**

## Overview

This directory contains Bicep variable files for the **SCCservice** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **SCCservice.bicep** - Global/cloud-wide IP address ranges
- **region/SCCservice_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global SCCservice module to access all IP ranges for this service tag:

```bicep
import * as sccservice from './SCCservice.bicep'

// Use the variable in your template
var allowedIPs = sccservice.SCCservice
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as sccserviceEastUS from './region/SCCservice_EastUS.bicep'

// Use the regional variable
var eastUSIPs = sccserviceEastUS.SCCservice_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `AustraliaCentral`
- `AustraliaCentral2`
- `AustraliaEast`
- `AustraliaSoutheast`
- `BrazilSouth`
- `BrazilSoutheast`
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
- `JioIndiaWest`
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

Total regional variants: 50


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: SCCservice
- **Module Directory**: sc-cservice
