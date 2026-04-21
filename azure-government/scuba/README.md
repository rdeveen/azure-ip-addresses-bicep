# Scuba Bicep Module

Azure service tag: **Scuba**

## Overview

This directory contains Bicep variable files for the **Scuba** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **Scuba.bicep** - Global/cloud-wide IP address ranges
- **region/Scuba_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global Scuba module to access all IP ranges for this service tag:

```bicep
import * as scuba from './Scuba.bicep'

// Use the variable in your template
var allowedIPs = scuba.Scuba
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as scubaEastUS from './region/Scuba_EastUS.bicep'

// Use the regional variable
var eastUSIPs = scubaEastUS.Scuba_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: Scuba
- **Module Directory**: scuba
