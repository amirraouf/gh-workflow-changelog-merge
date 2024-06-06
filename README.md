# gh-workflow-changelog-merge
This is a demonstrated project for gh actions to merge and generate the changelogs and app versions in a smooth way

The philosophy of changelog is to announce any breaking changes or what been added/modified/removed/deprecated at the feature 
Changelog should not be git reference log but on the other side modifying changelog file manually has a lot of pain in the ass as pull requests conflict with each other much so the purpose of this repo is to isolate every developer working on the changelog by adding his great work to be added as separate fragments and all of them will be merged and linked to the ticket board

The tech stack used
- [incremental](https://twisted.org/incremental/docs/index.html)
- [towncrier](https://towncrier.readthedocs.io/en/stable/index.html)

All what you need to do as developer

```sh
towncrier create -c "Add cool button to say hello" <ticketnumber>.added.md
towncrier create -c "Pause the functionality of the bad code" <ticketnumber>.deprecated.md
```
which will create at `changelog.d` two files and the github action will merge, append to `CHANGELOG.md` and link them to the new version with the ticket number