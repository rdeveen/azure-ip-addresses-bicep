# Windows365 Bicep Module

Azure service tag: **Windows365**

## Overview

This directory contains Bicep variable files for the **Windows365** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **Windows365.bicep** - Global/cloud-wide IP address ranges
- **region/Windows365_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global Windows365 module to access all IP ranges for this service tag:

```bicep
import * as windows365 from './Windows365.bicep'

// Use the variable in your template
var allowedIPs = windows365.Windows365
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as windows365EastUS from './region/Windows365_EastUS.bicep'

// Use the regional variable
var eastUSIPs = windows365EastUS.Windows365_EastUS
```

### From GitHub Container Registry (GHCR)

You can also import this module directly from GHCR:

`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/windows365/windows365:latest`



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: Windows365
- **Module Directory**: windows365
