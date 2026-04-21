# AzureKeyVault Bicep Module

Azure service tag: **AzureKeyVault**

## Overview

This directory contains Bicep variable files for the **AzureKeyVault** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureKeyVault.bicep** - Global/cloud-wide IP address ranges
- **region/AzureKeyVault_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureKeyVault module to access all IP ranges for this service tag:

```bicep
import * as azurekeyvault from './AzureKeyVault.bicep'

// Use the variable in your template
var allowedIPs = azurekeyvault.AzureKeyVault
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurekeyvaultEastUS from './region/AzureKeyVault_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurekeyvaultEastUS.AzureKeyVault_EastUS
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
- **Service Tag**: AzureKeyVault
- **Module Directory**: azure-key-vault
