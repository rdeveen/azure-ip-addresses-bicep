# AzureSiteRecovery Bicep Module

Azure service tag: **AzureSiteRecovery**

## Overview

This directory contains Bicep variable files for the **AzureSiteRecovery** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureSiteRecovery.bicep** - Global/cloud-wide IP address ranges
- **region/AzureSiteRecovery_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureSiteRecovery module to access all IP ranges for this service tag:

```bicep
import * as azuresiterecovery from './AzureSiteRecovery.bicep'

// Use the variable in your template
var allowedIPs = azuresiterecovery.AzureSiteRecovery
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuresiterecoveryEastUS from './region/AzureSiteRecovery_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuresiterecoveryEastUS.AzureSiteRecovery_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureSiteRecovery
- **Module Directory**: azure-site-recovery
