# AppConfiguration Bicep Module

Azure service tag: **AppConfiguration**

## Overview

This directory contains Bicep variable files for the **AppConfiguration** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AppConfiguration.bicep** - Global/cloud-wide IP address ranges
- **region/AppConfiguration_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AppConfiguration module to access all IP ranges for this service tag:

```bicep
import * as appconfiguration from './AppConfiguration.bicep'

// Use the variable in your template
var allowedIPs = appconfiguration.AppConfiguration
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as appconfigurationEastUS from './region/AppConfiguration_EastUS.bicep'

// Use the regional variable
var eastUSIPs = appconfigurationEastUS.AppConfiguration_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AppConfiguration
- **Module Directory**: app-configuration
