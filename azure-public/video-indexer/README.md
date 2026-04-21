# VideoIndexer Bicep Module

Azure service tag: **VideoIndexer**

## Overview

This directory contains Bicep variable files for the **VideoIndexer** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **VideoIndexer.bicep** - Global/cloud-wide IP address ranges
- **region/VideoIndexer_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global VideoIndexer module to access all IP ranges for this service tag:

```bicep
import * as videoindexer from './VideoIndexer.bicep'

// Use the variable in your template
var allowedIPs = videoindexer.VideoIndexer
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as videoindexerEastUS from './region/VideoIndexer_EastUS.bicep'

// Use the regional variable
var eastUSIPs = videoindexerEastUS.VideoIndexer_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: VideoIndexer
- **Module Directory**: video-indexer
