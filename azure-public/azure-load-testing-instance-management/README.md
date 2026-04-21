# AzureLoadTestingInstanceManagement Bicep Module

Azure service tag: **AzureLoadTestingInstanceManagement**

## Overview

This directory contains Bicep variable files for the **AzureLoadTestingInstanceManagement** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureLoadTestingInstanceManagement.bicep** - Global/cloud-wide IP address ranges
- **region/AzureLoadTestingInstanceManagement_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureLoadTestingInstanceManagement module to access all IP ranges for this service tag:

```bicep
import * as azureloadtestinginstancemanagement from './AzureLoadTestingInstanceManagement.bicep'

// Use the variable in your template
var allowedIPs = azureloadtestinginstancemanagement.AzureLoadTestingInstanceManagement
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureloadtestinginstancemanagementEastUS from './region/AzureLoadTestingInstanceManagement_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureloadtestinginstancemanagementEastUS.AzureLoadTestingInstanceManagement_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureLoadTestingInstanceManagement
- **Module Directory**: azure-load-testing-instance-management
