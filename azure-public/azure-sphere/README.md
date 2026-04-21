# AzureSphere Bicep Module

Azure service tag: **AzureSphere**

## Overview

This directory contains Bicep variable files for the **AzureSphere** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureSphere.bicep** - Global/cloud-wide IP address ranges
- **region/AzureSphere_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureSphere module to access all IP ranges for this service tag:

```bicep
import * as azuresphere from './AzureSphere.bicep'

// Use the variable in your template
var allowedIPs = azuresphere.AzureSphere
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuresphereEastUS from './region/AzureSphere_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuresphereEastUS.AzureSphere_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureSphere
- **Module Directory**: azure-sphere
