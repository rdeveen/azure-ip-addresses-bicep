# LogicAppsManagement Bicep Module

Azure service tag: **LogicAppsManagement**

## Overview

This directory contains Bicep variable files for the **LogicAppsManagement** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **LogicAppsManagement.bicep** - Global/cloud-wide IP address ranges
- **region/LogicAppsManagement_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global LogicAppsManagement module to access all IP ranges for this service tag:

```bicep
import * as logicappsmanagement from './LogicAppsManagement.bicep'

// Use the variable in your template
var allowedIPs = logicappsmanagement.LogicAppsManagement
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as logicappsmanagementEastUS from './region/LogicAppsManagement_EastUS.bicep'

// Use the regional variable
var eastUSIPs = logicappsmanagementEastUS.LogicAppsManagement_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: LogicAppsManagement
- **Module Directory**: logic-apps-management
