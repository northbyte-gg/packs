# Lint fixtures

`clean/` is a mini pack that passes every check. Every other directory is named after one lint
check and holds only the files that differ from `clean/`: `tools/test-lint` copies `clean/`,
lays the directory over it, and expects the lint to fail with that check's name.

`removed-id/` is the exception: its `previous/` files are added to a copy of `clean/` that is
zipped as the "previous release", and `clean/` itself is linted against it.
