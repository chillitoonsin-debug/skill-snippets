# Useful shell one-liners

```bash
# Find large files
find . -type f -size +10M -exec ls -lh {} \;

# Count lines of code by extension
find . -name '*.py' | xargs wc -l | tail -1

# Replace text across files
grep -rl "old" . | xargs sed -i 's/old/new/g'

# Watch a directory for changes
inotifywait -m -r -e modify,create,delete .
```
