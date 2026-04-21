# ApiManagement Bicep Module

Azure service tag: **ApiManagement**

## Overview

This directory contains Bicep variable files for the **ApiManagement** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **ApiManagement.bicep** - Global/cloud-wide IP address ranges
- **region/ApiManagement_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global ApiManagement module to access all IP ranges for this service tag:

```bicep
import * as apimanagement from './ApiManagement.bicep'

// Use the variable in your template
var allowedIPs = apimanagement.ApiManagement
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as apimanagementEastUS from './region/ApiManagement_EastUS.bicep'

// Use the regional variable
var eastUSIPs = apimanagementEastUS.ApiManagement_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `ChinaEast`
- `ChinaEast2`
- `ChinaEast3`
- `ChinaNorth`
- `ChinaNorth2`
- `ChinaNorth3`

Total regional variants: 6


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: ApiManagement
- **Module Directory**: api-management
