# AzureStack Bicep Module

Azure service tag: **AzureStack**

## Overview

This directory contains Bicep variable files for the **AzureStack** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureStack.bicep** - Global/cloud-wide IP address ranges
- **region/AzureStack_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureStack module to access all IP ranges for this service tag:

```bicep
import * as azurestack from './AzureStack.bicep'

// Use the variable in your template
var allowedIPs = azurestack.AzureStack
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurestackEastUS from './region/AzureStack_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurestackEastUS.AzureStack_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureStack
- **Module Directory**: azure-stack
