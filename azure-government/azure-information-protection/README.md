# AzureInformationProtection Bicep Module

Azure service tag: **AzureInformationProtection**

## Overview

This directory contains Bicep variable files for the **AzureInformationProtection** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureInformationProtection.bicep** - Global/cloud-wide IP address ranges
- **region/AzureInformationProtection_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureInformationProtection module to access all IP ranges for this service tag:

```bicep
import * as azureinformationprotection from './AzureInformationProtection.bicep'

// Use the variable in your template
var allowedIPs = azureinformationprotection.AzureInformationProtection
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureinformationprotectionEastUS from './region/AzureInformationProtection_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureinformationprotectionEastUS.AzureInformationProtection_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzureInformationProtection
- **Module Directory**: azure-information-protection
