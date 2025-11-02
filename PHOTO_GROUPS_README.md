# Photo Groups System

## How it works

Photos in `src/hiking_photos/` are automatically grouped by time:
- Photos within 3 days of each other are grouped together
- Groups are sorted most recent first
- Groups are displayed as collapsible sections on the hiking page
- Each group shows a count of photos
- Photos display in 2 columns at 80% page width

## Naming groups

1. Run the helper script to see all timestamps:
   ```bash
   source venv/bin/activate
   python print_timestamps.py
   ```

2. Copy the output timestamps to `src/photo_groups.yaml`

3. Replace the default names with your custom names:
   ```yaml
   "2025-06-12": "Mount Washington - June 2025"
   "2025-07-01": "White Mountains Day Hike"
   ```

4. Rebuild the site:
   ```bash
   python build.py
   ```

## Files

- `build.py`: Contains photo grouping logic
- `src/photo_groups.yaml`: Maps timestamps to group names
- `src/hiking_photos/`: Source photos directory
- `out/hiking/photos/`: Generated photo gallery
- `templates/post.html`: Photo gallery HTML template
- `templates/style.css`: Photo gallery styling
