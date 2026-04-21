# DataFactoryManagement Bicep Module

Azure service tag: **DataFactoryManagement**

## Overview

This directory contains Bicep variable files for the **DataFactoryManagement** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **DataFactoryManagement.bicep** - Global/cloud-wide IP address ranges
- **region/DataFactoryManagement_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global DataFactoryManagement module to access all IP ranges for this service tag:

```bicep
import * as datafactorymanagement from './DataFactoryManagement.bicep'

// Use the variable in your template
var allowedIPs = datafactorymanagement.DataFactoryManagement
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as datafactorymanagementEastUS from './region/DataFactoryManagement_EastUS.bicep'

// Use the regional variable
var eastUSIPs = datafactorymanagementEastUS.DataFactoryManagement_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: DataFactoryManagement
- **Module Directory**: data-factory-management
