# AzureQuantum Bicep Module

Azure service tag: **AzureQuantum**

## Overview

This directory contains Bicep variable files for the **AzureQuantum** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureQuantum.bicep** - Global/cloud-wide IP address ranges
- **region/AzureQuantum_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureQuantum module to access all IP ranges for this service tag:

```bicep
import * as azurequantum from './AzureQuantum.bicep'

// Use the variable in your template
var allowedIPs = azurequantum.AzureQuantum
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurequantumEastUS from './region/AzureQuantum_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurequantumEastUS.AzureQuantum_EastUS
```

### From GitHub Container Registry (GHCR)

You can also import this module directly from GHCR:

`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/azure-quantum/azure-quantum:latest`



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureQuantum
- **Module Directory**: azure-quantum
