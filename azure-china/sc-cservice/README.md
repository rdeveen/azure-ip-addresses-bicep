# SCCservice Bicep Module

Azure service tag: **SCCservice**

## Overview

This directory contains Bicep variable files for the **SCCservice** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **SCCservice.bicep** - Global/cloud-wide IP address ranges
- **region/SCCservice_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global SCCservice module to access all IP ranges for this service tag:

```bicep
import * as sccservice from './SCCservice.bicep'

// Use the variable in your template
var allowedIPs = sccservice.SCCservice
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as sccserviceEastUS from './region/SCCservice_EastUS.bicep'

// Use the regional variable
var eastUSIPs = sccserviceEastUS.SCCservice_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `ChinaEast`
- `ChinaEast2`
- `ChinaEast3`
- `ChinaNorth`
- `ChinaNorth2`

Total regional variants: 5


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: SCCservice
- **Module Directory**: sc-cservice
