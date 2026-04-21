# EOPExternalPublishedIPs Bicep Module

Azure service tag: **EOPExternalPublishedIPs**

## Overview

This directory contains Bicep variable files for the **EOPExternalPublishedIPs** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **EOPExternalPublishedIPs.bicep** - Global/cloud-wide IP address ranges
- **region/EOPExternalPublishedIPs_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global EOPExternalPublishedIPs module to access all IP ranges for this service tag:

```bicep
import * as eopexternalpublishedips from './EOPExternalPublishedIPs.bicep'

// Use the variable in your template
var allowedIPs = eopexternalpublishedips.EOPExternalPublishedIPs
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as eopexternalpublishedipsEastUS from './region/EOPExternalPublishedIPs_EastUS.bicep'

// Use the regional variable
var eastUSIPs = eopexternalpublishedipsEastUS.EOPExternalPublishedIPs_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: EOPExternalPublishedIPs
- **Module Directory**: eop-external-published-i-ps
