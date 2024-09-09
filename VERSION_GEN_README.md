# VERSION GENERATOR README.md

## What It Does

This Python script is designed to generate version information for your project by leveraging Git metadata. It retrieves details such as the current Git tag, commit count, and branch name, then writes this information into a TypeScript file. This is useful for including version information within your application.

## How It Works

1. **Retrieve Version Information**: The script executes Git commands to fetch the current tag, commit count, and branch name.
   - `git describe --tags --long`: Gets the most recent tag and the number of commits since that tag.
   - `git rev-parse --abbrev-ref HEAD`: Retrieves the current branch name.

2. **Process Version Data**: 
   - Extracts and cleans up the version name from the Git tag.
   - Calculates a version code by combining the major, minor, and patch versions with the commit count.

3. **Write Version Information**: 
   - Creates or updates the `src/version.tsx` file with the version details in TypeScript format.

## How To Use It

### Running the Script

To generate the version information and write it to a TypeScript file, execute the script with:

```bash
python versionGenerator.py
```

### What Happens When You Run It

- The script will fetch the latest version information from your Git repository.
- It will calculate the version code and prepare the version details.
- It will then write this information to `src/version.tsx`.

### Example Output

After running the script, `src/version.tsx` will contain something like:

```typescript
export const versionInfo = {
    versionCode: 1234567,
    versionName: "1.0.0",
    fullVersionName: "v1.0.0-5-gabc123@main",
    updated: "2024-09-09 12:34:56"
};
```

Here:
- `versionCode` is a unique code representing the version.
- `versionName` is extracted from the latest Git tag.
- `fullVersionName` includes the tag, commit count, and branch name.
- `updated` shows the date and time when the version was generated.

## Important Notes

- **Git Tags**: Ensure your repository has Git tags. The script relies on these tags to determine the version name.
- **File Location**: The TypeScript file (`src/version.tsx`) needs to be writable. Make sure the `src/` directory exists and has the right permissions.

## Troubleshooting

- **Git Errors**: If there are issues with Git commands, confirm that Git is installed and that your repository contains tags and commits.
- **File Write Errors**: Ensure that the `src/` directory is present and accessible.

---
