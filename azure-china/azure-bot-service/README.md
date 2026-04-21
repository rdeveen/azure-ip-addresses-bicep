# AzureBotService Bicep Module

Azure service tag: **AzureBotService**

## Overview

This directory contains Bicep variable files for the **AzureBotService** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureBotService.bicep** - Global/cloud-wide IP address ranges
- **region/AzureBotService_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureBotService module to access all IP ranges for this service tag:

```bicep
import * as azurebotservice from './AzureBotService.bicep'

// Use the variable in your template
var allowedIPs = azurebotservice.AzureBotService
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurebotserviceEastUS from './region/AzureBotService_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurebotserviceEastUS.AzureBotService_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `ChinaEast`
- `ChinaEast2`
- `ChinaEast3`
- `ChinaNorth`
- `ChinaNorth2`
- `ChinaNorth3`

Total regional variants: 6


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: AzureBotService
- **Module Directory**: azure-bot-service
