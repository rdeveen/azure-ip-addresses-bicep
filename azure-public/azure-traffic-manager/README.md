# AzureTrafficManager Bicep Module

Azure service tag: **AzureTrafficManager**

## Overview

This directory contains Bicep variable files for the **AzureTrafficManager** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureTrafficManager.bicep** - Global/cloud-wide IP address ranges
- **region/AzureTrafficManager_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureTrafficManager module to access all IP ranges for this service tag:

```bicep
import * as azuretrafficmanager from './AzureTrafficManager.bicep'

// Use the variable in your template
var allowedIPs = azuretrafficmanager.AzureTrafficManager
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuretrafficmanagerEastUS from './region/AzureTrafficManager_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuretrafficmanagerEastUS.AzureTrafficManager_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureTrafficManager
- **Module Directory**: azure-traffic-manager
