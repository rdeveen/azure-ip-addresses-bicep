# Dynamics365ForMarketingEmail Bicep Module

Azure service tag: **Dynamics365ForMarketingEmail**

## Overview

This directory contains Bicep variable files for the **Dynamics365ForMarketingEmail** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **Dynamics365ForMarketingEmail.bicep** - Global/cloud-wide IP address ranges
- **region/Dynamics365ForMarketingEmail_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global Dynamics365ForMarketingEmail module to access all IP ranges for this service tag:

```bicep
import * as dynamics365formarketingemail from './Dynamics365ForMarketingEmail.bicep'

// Use the variable in your template
var allowedIPs = dynamics365formarketingemail.Dynamics365ForMarketingEmail
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as dynamics365formarketingemailEastUS from './region/Dynamics365ForMarketingEmail_EastUS.bicep'

// Use the regional variable
var eastUSIPs = dynamics365formarketingemailEastUS.Dynamics365ForMarketingEmail_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `AustraliaSoutheast`
- `BrazilSouth`
- `CanadaCentral`
- `CentralIndia`
- `EastAsia`
- `EastUS`
- `FranceCentral`
- `GermanyWestCentral`
- `JapanEast`
- `KoreaCentral`
- `NorthEurope`
- `NorwayEast`
- `SouthAfricaNorth`
- `SoutheastAsia`
- `SwedenCentral`
- `SwitzerlandNorth`
- `UAENorth`
- `UKSouth`
- `WestUS2`

Total regional variants: 19


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: Dynamics365ForMarketingEmail
- **Module Directory**: dynamics365-for-marketing-email
