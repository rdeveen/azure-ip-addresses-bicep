# AzureHealthcareAPIs Bicep Module

Azure service tag: **AzureHealthcareAPIs**

## Overview

This directory contains Bicep variable files for the **AzureHealthcareAPIs** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureHealthcareAPIs.bicep** - Global/cloud-wide IP address ranges
- **region/AzureHealthcareAPIs_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureHealthcareAPIs module to access all IP ranges for this service tag:

```bicep
import * as azurehealthcareapis from './AzureHealthcareAPIs.bicep'

// Use the variable in your template
var allowedIPs = azurehealthcareapis.AzureHealthcareAPIs
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurehealthcareapisEastUS from './region/AzureHealthcareAPIs_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurehealthcareapisEastUS.AzureHealthcareAPIs_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureHealthcareAPIs
- **Module Directory**: azure-healthcare-ap-is
