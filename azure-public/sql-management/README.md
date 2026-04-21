# SqlManagement Bicep Module

Azure service tag: **SqlManagement**

## Overview

This directory contains Bicep variable files for the **SqlManagement** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **SqlManagement.bicep** - Global/cloud-wide IP address ranges
- **region/SqlManagement_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global SqlManagement module to access all IP ranges for this service tag:

```bicep
import * as sqlmanagement from './SqlManagement.bicep'

// Use the variable in your template
var allowedIPs = sqlmanagement.SqlManagement
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as sqlmanagementEastUS from './region/SqlManagement_EastUS.bicep'

// Use the regional variable
var eastUSIPs = sqlmanagementEastUS.SqlManagement_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: SqlManagement
- **Module Directory**: sql-management
