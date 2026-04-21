# AzureAdvancedThreatProtection Bicep Module

Azure service tag: **AzureAdvancedThreatProtection**

## Overview

This directory contains Bicep variable files for the **AzureAdvancedThreatProtection** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureAdvancedThreatProtection.bicep** - Global/cloud-wide IP address ranges
- **region/AzureAdvancedThreatProtection_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureAdvancedThreatProtection module to access all IP ranges for this service tag:

```bicep
import * as azureadvancedthreatprotection from './AzureAdvancedThreatProtection.bicep'

// Use the variable in your template
var allowedIPs = azureadvancedthreatprotection.AzureAdvancedThreatProtection
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureadvancedthreatprotectionEastUS from './region/AzureAdvancedThreatProtection_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureadvancedthreatprotectionEastUS.AzureAdvancedThreatProtection_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: AzureAdvancedThreatProtection
- **Module Directory**: azure-advanced-threat-protection
