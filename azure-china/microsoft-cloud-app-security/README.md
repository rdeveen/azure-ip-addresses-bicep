# MicrosoftCloudAppSecurity Bicep Module

Azure service tag: **MicrosoftCloudAppSecurity**

## Overview

This directory contains Bicep variable files for the **MicrosoftCloudAppSecurity** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **MicrosoftCloudAppSecurity.bicep** - Global/cloud-wide IP address ranges
- **region/MicrosoftCloudAppSecurity_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global MicrosoftCloudAppSecurity module to access all IP ranges for this service tag:

```bicep
import * as microsoftcloudappsecurity from './MicrosoftCloudAppSecurity.bicep'

// Use the variable in your template
var allowedIPs = microsoftcloudappsecurity.MicrosoftCloudAppSecurity
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as microsoftcloudappsecurityEastUS from './region/MicrosoftCloudAppSecurity_EastUS.bicep'

// Use the regional variable
var eastUSIPs = microsoftcloudappsecurityEastUS.MicrosoftCloudAppSecurity_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `ChinaEast`
- `ChinaEast2`
- `ChinaNorth`
- `ChinaNorth2`

Total regional variants: 4


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: MicrosoftCloudAppSecurity
- **Module Directory**: microsoft-cloud-app-security
