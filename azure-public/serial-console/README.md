# SerialConsole Bicep Module

Azure service tag: **SerialConsole**

## Overview

This directory contains Bicep variable files for the **SerialConsole** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **SerialConsole.bicep** - Global/cloud-wide IP address ranges
- **region/SerialConsole_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global SerialConsole module to access all IP ranges for this service tag:

```bicep
import * as serialconsole from './SerialConsole.bicep'

// Use the variable in your template
var allowedIPs = serialconsole.SerialConsole
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as serialconsoleEastUS from './region/SerialConsole_EastUS.bicep'

// Use the regional variable
var eastUSIPs = serialconsoleEastUS.SerialConsole_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: SerialConsole
- **Module Directory**: serial-console
