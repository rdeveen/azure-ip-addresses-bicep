# AzureDigitalTwins Bicep Module

Azure service tag: **AzureDigitalTwins**

## Overview

This directory contains Bicep variable files for the **AzureDigitalTwins** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureDigitalTwins.bicep** - Global/cloud-wide IP address ranges
- **region/AzureDigitalTwins_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureDigitalTwins module to access all IP ranges for this service tag:

```bicep
import * as azuredigitaltwins from './AzureDigitalTwins.bicep'

// Use the variable in your template
var allowedIPs = azuredigitaltwins.AzureDigitalTwins
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuredigitaltwinsEastUS from './region/AzureDigitalTwins_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuredigitaltwinsEastUS.AzureDigitalTwins_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `USDoDCentral`
- `USGovArizona`
- `USGovTexas`

Total regional variants: 3


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzureDigitalTwins
- **Module Directory**: azure-digital-twins
