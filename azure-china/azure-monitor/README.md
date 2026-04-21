# AzureMonitor Bicep Module

Azure service tag: **AzureMonitor**

## Overview

This directory contains Bicep variable files for the **AzureMonitor** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureMonitor.bicep** - Global/cloud-wide IP address ranges
- **region/AzureMonitor_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureMonitor module to access all IP ranges for this service tag:

```bicep
import * as azuremonitor from './AzureMonitor.bicep'

// Use the variable in your template
var allowedIPs = azuremonitor.AzureMonitor
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuremonitorEastUS from './region/AzureMonitor_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuremonitorEastUS.AzureMonitor_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `ChinaEast`
- `ChinaEast2`
- `ChinaEast3`
- `ChinaNorth`
- `ChinaNorth2`
- `ChinaNorth3`
- `Core`

Total regional variants: 7


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: AzureMonitor
- **Module Directory**: azure-monitor
