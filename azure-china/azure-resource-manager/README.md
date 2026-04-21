# AzureResourceManager Bicep Module

Azure service tag: **AzureResourceManager**

## Overview

This directory contains Bicep variable files for the **AzureResourceManager** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureResourceManager.bicep** - Global/cloud-wide IP address ranges
- **region/AzureResourceManager_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureResourceManager module to access all IP ranges for this service tag:

```bicep
import * as azureresourcemanager from './AzureResourceManager.bicep'

// Use the variable in your template
var allowedIPs = azureresourcemanager.AzureResourceManager
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureresourcemanagerEastUS from './region/AzureResourceManager_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureresourcemanagerEastUS.AzureResourceManager_EastUS
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
- **Service Tag**: AzureResourceManager
- **Module Directory**: azure-resource-manager
