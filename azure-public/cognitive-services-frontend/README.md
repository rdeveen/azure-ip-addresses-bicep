# CognitiveServicesFrontend Bicep Module

Azure service tag: **CognitiveServicesFrontend**

## Overview

This directory contains Bicep variable files for the **CognitiveServicesFrontend** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **CognitiveServicesFrontend.bicep** - Global/cloud-wide IP address ranges
- **region/CognitiveServicesFrontend_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global CognitiveServicesFrontend module to access all IP ranges for this service tag:

```bicep
import * as cognitiveservicesfrontend from './CognitiveServicesFrontend.bicep'

// Use the variable in your template
var allowedIPs = cognitiveservicesfrontend.CognitiveServicesFrontend
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as cognitiveservicesfrontendEastUS from './region/CognitiveServicesFrontend_EastUS.bicep'

// Use the regional variable
var eastUSIPs = cognitiveservicesfrontendEastUS.CognitiveServicesFrontend_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: CognitiveServicesFrontend
- **Module Directory**: cognitive-services-frontend
