# OneDsCollector Bicep Module

Azure service tag: **OneDsCollector**

## Overview

This directory contains Bicep variable files for the **OneDsCollector** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **OneDsCollector.bicep** - Global/cloud-wide IP address ranges
- **region/OneDsCollector_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global OneDsCollector module to access all IP ranges for this service tag:

```bicep
import * as onedscollector from './OneDsCollector.bicep'

// Use the variable in your template
var allowedIPs = onedscollector.OneDsCollector
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as onedscollectorEastUS from './region/OneDsCollector_EastUS.bicep'

// Use the regional variable
var eastUSIPs = onedscollectorEastUS.OneDsCollector_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: OneDsCollector
- **Module Directory**: one-ds-collector
