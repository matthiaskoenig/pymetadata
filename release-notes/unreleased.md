# Unreleased

## Fixes

- Write web service caches atomically so concurrent Python test environments and application processes do not read partial JSON. Failed writes preserve the previous cache.
