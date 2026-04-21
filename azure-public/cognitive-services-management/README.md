# CognitiveServicesManagement Bicep Module

Azure service tag: **CognitiveServicesManagement**

## Overview

This directory contains Bicep variable files for the **CognitiveServicesManagement** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **CognitiveServicesManagement.bicep** - Global/cloud-wide IP address ranges
- **region/CognitiveServicesManagement_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global CognitiveServicesManagement module to access all IP ranges for this service tag:

```bicep
import * as cognitiveservicesmanagement from './CognitiveServicesManagement.bicep'

// Use the variable in your template
var allowedIPs = cognitiveservicesmanagement.CognitiveServicesManagement
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as cognitiveservicesmanagementEastUS from './region/CognitiveServicesManagement_EastUS.bicep'

// Use the regional variable
var eastUSIPs = cognitiveservicesmanagementEastUS.CognitiveServicesManagement_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: CognitiveServicesManagement
- **Module Directory**: cognitive-services-management
