# AzureSentinel Bicep Module

Azure service tag: **AzureSentinel**

## Overview

This directory contains Bicep variable files for the **AzureSentinel** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureSentinel.bicep** - Global/cloud-wide IP address ranges
- **region/AzureSentinel_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureSentinel module to access all IP ranges for this service tag:

```bicep
import * as azuresentinel from './AzureSentinel.bicep'

// Use the variable in your template
var allowedIPs = azuresentinel.AzureSentinel
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuresentinelEastUS from './region/AzureSentinel_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuresentinelEastUS.AzureSentinel_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: AzureSentinel
- **Module Directory**: azure-sentinel
