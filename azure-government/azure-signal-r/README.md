# AzureSignalR Bicep Module

Azure service tag: **AzureSignalR**

## Overview

This directory contains Bicep variable files for the **AzureSignalR** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureSignalR.bicep** - Global/cloud-wide IP address ranges
- **region/AzureSignalR_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureSignalR module to access all IP ranges for this service tag:

```bicep
import * as azuresignalr from './AzureSignalR.bicep'

// Use the variable in your template
var allowedIPs = azuresignalr.AzureSignalR
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuresignalrEastUS from './region/AzureSignalR_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuresignalrEastUS.AzureSignalR_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `USDoDEast`
- `USGovArizona`
- `USGovIowa`
- `USGovVirginia`

Total regional variants: 4


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzureSignalR
- **Module Directory**: azure-signal-r
