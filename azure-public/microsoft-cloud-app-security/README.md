# MicrosoftCloudAppSecurity Bicep Module

Azure service tag: **MicrosoftCloudAppSecurity**

## Overview

This directory contains Bicep variable files for the **MicrosoftCloudAppSecurity** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **MicrosoftCloudAppSecurity.bicep** - Global/cloud-wide IP address ranges
- **region/MicrosoftCloudAppSecurity_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global MicrosoftCloudAppSecurity module to access all IP ranges for this service tag:

```bicep
import * as microsoftcloudappsecurity from './MicrosoftCloudAppSecurity.bicep'

// Use the variable in your template
var allowedIPs = microsoftcloudappsecurity.MicrosoftCloudAppSecurity
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as microsoftcloudappsecurityEastUS from './region/MicrosoftCloudAppSecurity_EastUS.bicep'

// Use the regional variable
var eastUSIPs = microsoftcloudappsecurityEastUS.MicrosoftCloudAppSecurity_EastUS
```

### From GitHub Container Registry (GHCR)

You can also import this module directly from GHCR:

`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/microsoft-cloud-app-security/microsoft-cloud-app-security:latest`

Example regional module:
`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/microsoft-cloud-app-security/region/microsoft-cloud-app-security-australia-east:latest`

## Available Regions

This module includes regional variants for the following Azure regions:

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
- `FranceCentral`
- `FranceSouth`
- `GermanyWestCentral`
- `JapanEast`
- `NorthEurope`
- `SouthCentralUS`
- `SoutheastAsia`
- `UKSouth`
- `UKWest`
- `WestCentralUS`
- `WestEurope`
- `WestUS`
- `WestUS2`
- `WestUS3`

Total regional variants: 26


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: MicrosoftCloudAppSecurity
- **Module Directory**: microsoft-cloud-app-security
