# AzureActiveDirectory Bicep Module

Azure service tag: **AzureActiveDirectory**

## Overview

This directory contains Bicep variable files for the **AzureActiveDirectory** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureActiveDirectory.bicep** - Global/cloud-wide IP address ranges
- **region/AzureActiveDirectory_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureActiveDirectory module to access all IP ranges for this service tag:

```bicep
import * as azureactivedirectory from './AzureActiveDirectory.bicep'

// Use the variable in your template
var allowedIPs = azureactivedirectory.AzureActiveDirectory
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureactivedirectoryEastUS from './region/AzureActiveDirectory_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureactivedirectoryEastUS.AzureActiveDirectory_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `ServiceEndpoint`

Total regional variants: 1


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureActiveDirectory
- **Module Directory**: azure-active-directory
