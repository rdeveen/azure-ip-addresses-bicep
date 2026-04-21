# WindowsAdminCenter Bicep Module

Azure service tag: **WindowsAdminCenter**

## Overview

This directory contains Bicep variable files for the **WindowsAdminCenter** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **WindowsAdminCenter.bicep** - Global/cloud-wide IP address ranges
- **region/WindowsAdminCenter_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global WindowsAdminCenter module to access all IP ranges for this service tag:

```bicep
import * as windowsadmincenter from './WindowsAdminCenter.bicep'

// Use the variable in your template
var allowedIPs = windowsadmincenter.WindowsAdminCenter
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as windowsadmincenterEastUS from './region/WindowsAdminCenter_EastUS.bicep'

// Use the regional variable
var eastUSIPs = windowsadmincenterEastUS.WindowsAdminCenter_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: WindowsAdminCenter
- **Module Directory**: windows-admin-center
