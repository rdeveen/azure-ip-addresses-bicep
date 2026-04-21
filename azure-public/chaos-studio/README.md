# ChaosStudio Bicep Module

Azure service tag: **ChaosStudio**

## Overview

This directory contains Bicep variable files for the **ChaosStudio** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **ChaosStudio.bicep** - Global/cloud-wide IP address ranges
- **region/ChaosStudio_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global ChaosStudio module to access all IP ranges for this service tag:

```bicep
import * as chaosstudio from './ChaosStudio.bicep'

// Use the variable in your template
var allowedIPs = chaosstudio.ChaosStudio
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as chaosstudioEastUS from './region/ChaosStudio_EastUS.bicep'

// Use the regional variable
var eastUSIPs = chaosstudioEastUS.ChaosStudio_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: ChaosStudio
- **Module Directory**: chaos-studio
