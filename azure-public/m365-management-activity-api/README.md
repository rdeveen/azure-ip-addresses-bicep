# M365ManagementActivityApi Bicep Module

Azure service tag: **M365ManagementActivityApi**

## Overview

This directory contains Bicep variable files for the **M365ManagementActivityApi** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **M365ManagementActivityApi.bicep** - Global/cloud-wide IP address ranges
- **region/M365ManagementActivityApi_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global M365ManagementActivityApi module to access all IP ranges for this service tag:

```bicep
import * as m365managementactivityapi from './M365ManagementActivityApi.bicep'

// Use the variable in your template
var allowedIPs = m365managementactivityapi.M365ManagementActivityApi
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as m365managementactivityapiEastUS from './region/M365ManagementActivityApi_EastUS.bicep'

// Use the regional variable
var eastUSIPs = m365managementactivityapiEastUS.M365ManagementActivityApi_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: M365ManagementActivityApi
- **Module Directory**: m365-management-activity-api
