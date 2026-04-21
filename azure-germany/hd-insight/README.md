# HDInsight Bicep Module

Azure service tag: **HDInsight**

## Overview

This directory contains Bicep variable files for the **HDInsight** service tag in the **Azure Germany Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **HDInsight.bicep** - Global/cloud-wide IP address ranges
- **region/HDInsight_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global HDInsight module to access all IP ranges for this service tag:

```bicep
import * as hdinsight from './HDInsight.bicep'

// Use the variable in your template
var allowedIPs = hdinsight.HDInsight
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as hdinsightEastUS from './region/HDInsight_EastUS.bicep'

// Use the regional variable
var eastUSIPs = hdinsightEastUS.HDInsight_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `GermanyCentral`
- `GermanyNorthEast`

Total regional variants: 2


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Germany Cloud
- **Service Tag**: HDInsight
- **Module Directory**: hd-insight
