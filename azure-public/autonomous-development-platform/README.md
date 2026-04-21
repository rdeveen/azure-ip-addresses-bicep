# AutonomousDevelopmentPlatform Bicep Module

Azure service tag: **AutonomousDevelopmentPlatform**

## Overview

This directory contains Bicep variable files for the **AutonomousDevelopmentPlatform** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AutonomousDevelopmentPlatform.bicep** - Global/cloud-wide IP address ranges
- **region/AutonomousDevelopmentPlatform_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AutonomousDevelopmentPlatform module to access all IP ranges for this service tag:

```bicep
import * as autonomousdevelopmentplatform from './AutonomousDevelopmentPlatform.bicep'

// Use the variable in your template
var allowedIPs = autonomousdevelopmentplatform.AutonomousDevelopmentPlatform
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as autonomousdevelopmentplatformEastUS from './region/AutonomousDevelopmentPlatform_EastUS.bicep'

// Use the regional variable
var eastUSIPs = autonomousdevelopmentplatformEastUS.AutonomousDevelopmentPlatform_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AutonomousDevelopmentPlatform
- **Module Directory**: autonomous-development-platform
