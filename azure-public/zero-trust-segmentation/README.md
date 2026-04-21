# ZeroTrustSegmentation Bicep Module

Azure service tag: **ZeroTrustSegmentation**

## Overview

This directory contains Bicep variable files for the **ZeroTrustSegmentation** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **ZeroTrustSegmentation.bicep** - Global/cloud-wide IP address ranges
- **region/ZeroTrustSegmentation_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global ZeroTrustSegmentation module to access all IP ranges for this service tag:

```bicep
import * as zerotrustsegmentation from './ZeroTrustSegmentation.bicep'

// Use the variable in your template
var allowedIPs = zerotrustsegmentation.ZeroTrustSegmentation
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as zerotrustsegmentationEastUS from './region/ZeroTrustSegmentation_EastUS.bicep'

// Use the regional variable
var eastUSIPs = zerotrustsegmentationEastUS.ZeroTrustSegmentation_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: ZeroTrustSegmentation
- **Module Directory**: zero-trust-segmentation
