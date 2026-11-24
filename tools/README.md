# tools/

The `color/*.xml` draw.io libraries are generated from the `src/` source tree.

1. **Extract** existing libraries into `src/` (SVGs + manifests):

   ```sh
   python3 tools/extract.py
   ```

2. **Edit** icons/groups by changing files under `src/icons/` or `src/groups/`
   and updating `src/manifest.json` / `src/groups/manifest.json` as needed.

3. **Rebuild** every `color/*.xml` library from `src/`:

   ```sh
   python3 tools/build.py
   ```

4. **Check** for drift between `src/` and `color/` without writing:

   ```sh
   python3 tools/build.py --check
   ```
