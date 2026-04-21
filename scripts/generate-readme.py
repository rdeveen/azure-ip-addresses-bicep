#!/usr/bin/env python3
"""
Generate README.md files for Bicep modules.
Creates documentation for all service tag modules across all cloud regions.
"""

import os
import re
from pathlib import Path

# Get the workspace root directory (one level up from scripts)
WORKSPACE_ROOT = Path(__file__).parent.parent

# Define cloud regions and their descriptions
CLOUDS = {
    'azure-public': {
        'name': 'Azure Public Cloud',
        'description': 'Microsoft Azure public cloud infrastructure'
    },
    'azure-government': {
        'name': 'Azure US Government Cloud',
        'description': 'Azure Government cloud for US Government agencies and their partners'
    },
    'azure-china': {
        'name': 'Azure China Cloud',
        'description': 'Azure operated by 21Vianet in China'
    },
    'azure-germany': {
        'name': 'Azure Germany Cloud',
        'description': 'Azure cloud in Germany'
    }
}


def get_service_tag_from_bicep_file(module_path):
    """Derive the service tag name from the actual main .bicep filename in the module directory.

    The main bicep file (no underscore in stem) preserves the original casing
    used by convert-to-bicep.py, e.g. 'EOPExternalPublishedIPs.bicep' -> 'EOPExternalPublishedIPs'.
    Returns None if no such file is found.
    """
    for bicep_file in Path(module_path).glob('*.bicep'):
        if '_' not in bicep_file.stem:
            return bicep_file.stem
    return None


def extract_region_from_filename(filename, service_tag):
    """Extract region name from regional bicep filename.
    
    Example: ActionGroup_EastUS.bicep -> EastUS
    """
    # Pattern: ServiceTag_RegionName.bicep
    pattern = rf'{service_tag}_(.+)\.bicep$'
    match = re.match(pattern, filename)
    return match.group(1) if match else None


def get_regional_variants(module_path, service_tag):
    """Get list of all regional variants for the module.
    
    Returns list of tuples: [(region_name, filename), ...]
    """
    region_path = module_path / 'region'
    if not region_path.exists():
        return []
    
    regional_files = sorted([f for f in region_path.iterdir() if f.suffix == '.bicep'])
    variants = []
    
    for bicep_file in regional_files:
        region = extract_region_from_filename(bicep_file.name, service_tag)
        if region:
            variants.append((region, bicep_file.name))
    
    return variants


def generate_readme_content(cloud_name, module_dir, service_tag, module_path):
    """Generate README.md content for a service tag module."""
    
    regional_variants = get_regional_variants(module_path, service_tag)
    
    # Format regional variants into a nice list
    regions_section = ""
    if regional_variants:
        regions_section = "## Available Regions\n\n"
        regions_section += "This module includes regional variants for the following Azure regions:\n\n"
        
        # Group regions for better readability
        regions_list = [f"- `{region}`" for region, _ in regional_variants]
        regions_section += "\n".join(regions_list)
        regions_section += f"\n\nTotal regional variants: {len(regional_variants)}\n"
    
    readme_content = f"""# {service_tag} Bicep Module

Azure service tag: **{service_tag}**

## Overview

This directory contains Bicep variable files for the **{service_tag}** service tag in the **{cloud_name}**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **{service_tag}.bicep** - Global/cloud-wide IP address ranges
- **region/{service_tag}_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global {service_tag} module to access all IP ranges for this service tag:

```bicep
import * as {service_tag.lower()} from './{service_tag}.bicep'

// Use the variable in your template
var allowedIPs = {service_tag.lower()}.{service_tag}
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as {service_tag.lower()}EastUS from './region/{service_tag}_EastUS.bicep'

// Use the regional variable
var eastUSIPs = {service_tag.lower()}EastUS.{service_tag}_EastUS
```

{regions_section}

## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: {cloud_name}
- **Service Tag**: {service_tag}
- **Module Directory**: {module_dir}
"""
    
    return readme_content


def create_readme_files():
    """Create README.md files for all modules across all cloud regions."""
    
    created_files = []
    skipped_dirs = []
    
    for cloud_dir, cloud_info in CLOUDS.items():
        cloud_path = WORKSPACE_ROOT / cloud_dir
        
        # Check if cloud directory exists
        if not cloud_path.exists():
            print(f"⚠️  Cloud directory not found: {cloud_path}")
            continue
        
        print(f"\n📁 Processing {cloud_info['name']}...")
        
        # Iterate through all module directories
        for module_dir_path in sorted(cloud_path.iterdir()):
            if not module_dir_path.is_dir():
                continue
            
            module_dir = module_dir_path.name
            
            # Derive service tag name from the actual .bicep filename on disk
            # so casing matches what convert-to-bicep.py produced.
            service_tag = get_service_tag_from_bicep_file(module_dir_path)
            if service_tag is None:
                skipped_dirs.append(f"{cloud_dir}/{module_dir} (no main .bicep file found)")
                continue
            
            # Generate README content
            readme_content = generate_readme_content(
                cloud_info['name'],
                module_dir,
                service_tag,
                module_dir_path
            )
            
            # Write README.md
            readme_path = module_dir_path / 'README.md'
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            
            created_files.append(str(readme_path))
            print(f"  ✅ {module_dir}")
    
    return created_files, skipped_dirs


if __name__ == '__main__':
    print("🔄 Generating README.md files for all Bicep modules...\n")
    
    files, skipped = create_readme_files()
    
    print(f"\n✨ Complete!")
    print(f"✅ Created {len(files)} README.md files")
    
    if skipped:
        print(f"\n⚠️  Skipped {len(skipped)} directories:")
        for skip in skipped[:10]:  # Show first 10
            print(f"  - {skip}")
        if len(skipped) > 10:
            print(f"  ... and {len(skipped) - 10} more")
