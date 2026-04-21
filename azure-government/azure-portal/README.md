# AzurePortal Bicep Module

Azure service tag: **AzurePortal**

## Overview

This directory contains Bicep variable files for the **AzurePortal** service tag in the **Azure US Government Cloud**.

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

## Available Regions

This module includes regional variants for the following Azure regions:

- `AzureAppServiceUx`
- `USDoDCentral`
- `USDoDEast`
- `USGovArizona`
- `USGovIowa`
- `USGovTexas`
- `USGovVirginia`

Total regional variants: 7


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzurePortal
- **Module Directory**: azure-portal
