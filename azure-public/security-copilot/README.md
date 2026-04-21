# SecurityCopilot Bicep Module

Azure service tag: **SecurityCopilot**

## Overview

This directory contains Bicep variable files for the **SecurityCopilot** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **SecurityCopilot.bicep** - Global/cloud-wide IP address ranges
- **region/SecurityCopilot_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global SecurityCopilot module to access all IP ranges for this service tag:

```bicep
import * as securitycopilot from './SecurityCopilot.bicep'

// Use the variable in your template
var allowedIPs = securitycopilot.SecurityCopilot
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as securitycopilotEastUS from './region/SecurityCopilot_EastUS.bicep'

// Use the regional variable
var eastUSIPs = securitycopilotEastUS.SecurityCopilot_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: SecurityCopilot
- **Module Directory**: security-copilot
