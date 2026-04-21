# AzureDeviceUpdate Bicep Module

Azure service tag: **AzureDeviceUpdate**

## Overview

This directory contains Bicep variable files for the **AzureDeviceUpdate** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureDeviceUpdate.bicep** - Global/cloud-wide IP address ranges
- **region/AzureDeviceUpdate_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureDeviceUpdate module to access all IP ranges for this service tag:

```bicep
import * as azuredeviceupdate from './AzureDeviceUpdate.bicep'

// Use the variable in your template
var allowedIPs = azuredeviceupdate.AzureDeviceUpdate
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuredeviceupdateEastUS from './region/AzureDeviceUpdate_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuredeviceupdateEastUS.AzureDeviceUpdate_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureDeviceUpdate
- **Module Directory**: azure-device-update
