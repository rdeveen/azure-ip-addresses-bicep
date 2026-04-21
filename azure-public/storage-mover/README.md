# StorageMover Bicep Module

Azure service tag: **StorageMover**

## Overview

This directory contains Bicep variable files for the **StorageMover** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **StorageMover.bicep** - Global/cloud-wide IP address ranges
- **region/StorageMover_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global StorageMover module to access all IP ranges for this service tag:

```bicep
import * as storagemover from './StorageMover.bicep'

// Use the variable in your template
var allowedIPs = storagemover.StorageMover
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as storagemoverEastUS from './region/StorageMover_EastUS.bicep'

// Use the regional variable
var eastUSIPs = storagemoverEastUS.StorageMover_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: StorageMover
- **Module Directory**: storage-mover
