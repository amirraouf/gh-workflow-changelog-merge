# gh-workflow-changelog-merge
This is a demonstrated project for gh actions to merge and generate the changelogs and app versions in a smooth way

The philosophy of our changelog is to clearly announce any breaking changes, new additions, modifications, removals, or deprecations in features. A changelog should not be a simple git reference log. Instead, it should provide meaningful context about changes. However, manually modifying the changelog file can be cumbersome, especially when pull requests conflict with each other.

The purpose of this repository is to streamline the process by allowing each developer to contribute their changes as separate fragments. These fragments will be merged and linked to the ticket board, ensuring that the changelog remains organized and up-to-date without conflicts.


This repository uses the following tools:

- [incremental](https://twisted.org/incremental/docs/index.html)
- [towncrier](https://towncrier.readthedocs.io/en/stable/index.html)

## Instructions for Developers
1. Use towncrier to create a changelog fragment. This will create a new file in the changelog.d directory. The file will be named using your ticket number and the type of change (e.g., added, deprecated).

```sh
towncrier create -c "Add cool button to say hello" <ticketnumber>.added.md
towncrier create -c "Pause the functionality of the bad code" <ticketnumber>.deprecated.md
```
Example commands will create two files in the `changelog.d` directory:

- `<ticketnumber>.added.md`
- `<ticketnumber>.deprecated.md`

2. The GitHub Action configured in this repository will automatically merge these fragments, append them to CHANGELOG.md, and link them to the corresponding ticket number when a new version is released.

By following this approach, we ensure that our changelog remains consistent, comprehensive, and free of merge conflicts.
