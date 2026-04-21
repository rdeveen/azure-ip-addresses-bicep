# AzureSpringCloud Bicep Module

Azure service tag: **AzureSpringCloud**

## Overview

This directory contains Bicep variable files for the **AzureSpringCloud** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureSpringCloud.bicep** - Global/cloud-wide IP address ranges
- **region/AzureSpringCloud_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureSpringCloud module to access all IP ranges for this service tag:

```bicep
import * as azurespringcloud from './AzureSpringCloud.bicep'

// Use the variable in your template
var allowedIPs = azurespringcloud.AzureSpringCloud
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurespringcloudEastUS from './region/AzureSpringCloud_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurespringcloudEastUS.AzureSpringCloud_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzureSpringCloud
- **Module Directory**: azure-spring-cloud
