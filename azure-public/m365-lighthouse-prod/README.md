# M365LighthouseProd Bicep Module

Azure service tag: **M365LighthouseProd**

## Overview

This directory contains Bicep variable files for the **M365LighthouseProd** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **M365LighthouseProd.bicep** - Global/cloud-wide IP address ranges
- **region/M365LighthouseProd_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global M365LighthouseProd module to access all IP ranges for this service tag:

```bicep
import * as m365lighthouseprod from './M365LighthouseProd.bicep'

// Use the variable in your template
var allowedIPs = m365lighthouseprod.M365LighthouseProd
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as m365lighthouseprodEastUS from './region/M365LighthouseProd_EastUS.bicep'

// Use the regional variable
var eastUSIPs = m365lighthouseprodEastUS.M365LighthouseProd_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: M365LighthouseProd
- **Module Directory**: m365-lighthouse-prod
