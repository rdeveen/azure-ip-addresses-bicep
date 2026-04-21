# CopilotActions Bicep Module

Azure service tag: **CopilotActions**

## Overview

This directory contains Bicep variable files for the **CopilotActions** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **CopilotActions.bicep** - Global/cloud-wide IP address ranges
- **region/CopilotActions_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global CopilotActions module to access all IP ranges for this service tag:

```bicep
import * as copilotactions from './CopilotActions.bicep'

// Use the variable in your template
var allowedIPs = copilotactions.CopilotActions
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as copilotactionsEastUS from './region/CopilotActions_EastUS.bicep'

// Use the regional variable
var eastUSIPs = copilotactionsEastUS.CopilotActions_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: CopilotActions
- **Module Directory**: copilot-actions
