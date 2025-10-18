# Contributing

We'd love for you to contribute to our project and help make it even better than it is today! As a contributor, here are the guidelines we'd like you to follow:

 - [Code of Conduct](#coc)
 - [Issues and Bugs](#issue)
 - [Feature Requests](#feature)
 - [Submission Guidelines](#submit)
 - [Coding Rules](#rules)
 - [Commit Message Guidelines](#commit)

## <a name="coc"></a> Code of Conduct
Help us keep our project open and inclusive. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## <a name="issue"></a> Found a Bug?
If you find a bug in the source code, you can help us by
[submitting an issue](#submit-issue) to our [GitHub Repository][github]. Even better, you can
[submit a Pull Request](#submit-pr) with a fix.

## <a name="feature"></a> Missing a Feature?
You can *request* a new feature by [submitting an issue](#submit-issue) to our GitHub
Repository. If you would like to *implement* a new feature, please submit an issue with
a proposal for your work first, to be sure that we can use it.
Please consider what kind of change it is:

*   For a **Major Feature**, first open an issue and outline your proposal so that it can be
    discussed. This will also allow us to better coordinate our efforts, prevent duplication of work,
    and help you to craft the change so that it is successfully accepted into the project.
*   **Small Features** can be crafted and directly [submitted as a Pull Request](#submit-pr).

## <a name="submit"></a> Submission Guidelines

### <a name="submit-issue"></a> Submitting an Issue

Before you submit an issue, please search the issue tracker, maybe an issue for your problem already exists and the discussion might inform you of workarounds readily available.

We want to fix all the issues as soon as possible, but before fixing a bug we need to reproduce and confirm it. In order to reproduce bugs we will systematically ask you to provide a minimal reproduction scenario using a repository that can be cloned and run.

### <a name="submit-pr"></a> Submitting a Pull Request (PR)
Before you submit your Pull Request (PR) consider the following guidelines:

*   Search [GitHub](https://github.com/ksprashu/gemini-cli-mcp-servers/pulls) for an open or closed PR
    that relates to your submission. You don't want to duplicate effort.
*   Be sure that an issue describes the problem you're fixing, or documents the design for the feature you'd like to add.
    Discussing the design upfront helps to ensure that we're ready to accept your work.
*   [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the ksprashu/gemini-cli-mcp-servers repo.
*   Make your changes in a new git branch:

     ```shell
     git checkout -b my-fix-branch main
     ```

*   Create your patch, **including appropriate test cases**.
*   Follow our [Coding Rules](#rules).
*   Run the full test suite, as described in the [developer documentation][dev-doc],
    and ensure that all tests pass.
*   Commit your changes using a descriptive commit message that follows our
    [commit message conventions](#commit). Adherence to these conventions is necessary because release notes are automatically generated from these messages.

     ```shell
     git commit -a
     ```
    Note: the optional commit `-a` command line option will automatically "add" and "rm" edited files.

*   Push your branch to GitHub:

    ```shell
    git push origin my-fix-branch
    ```

*   In GitHub, send a pull request to `gemini-cli-mcp-servers:main`.
*   If we suggest changes then:
    *   Make the required updates.
    *   Re-run the test suite to ensure tests are still passing.
    *   Rebase your branch and force push to your GitHub repository (this will update your Pull Request):

        ```shell
        git rebase main -i
        git push -f origin my-fix-branch
        ```

That's it! Thank you for your contribution!

#### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes
from the main (upstream) repository:

*   Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:

    ```shell
    git push origin --delete my-fix-branch
    ```

*   Check out the main branch:

    ```shell
    git checkout main -f
    ```

*   Delete the local branch:

    ```shell
    git branch -D my-fix-branch
    ```

*   Update your main with the latest upstream version:

    ```shell
    git pull --ff upstream main
    ```

## <a name="rules"></a> Coding Rules
To ensure consistency throughout the source code, keep these rules in mind as you are working:

*   All features or bug fixes **must be tested** by one or more specs (unit-tests).
*   All public API methods **must be documented**.

## <a name="commit"></a> Commit Message Guidelines

We have very precise rules over how our git commit messages can be formatted.  This leads to **more
readable messages** that are easy to follow when looking through the **project history**.  But also,
we use the git commit messages to **generate the change log**.

### Commit Message Format
Each commit message consists of a **header**, a **body** and a **footer**.  The header has a special
format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

Any line of the commit message cannot be longer 100 characters! This allows the message to be easier
to read on GitHub as well as in various git tools.

The footer should contain a [closing reference to an issue](https://help.github.com/articles/closing-issues-via-commit-messages/) if any.

Samples:

```
docs(changelog): update changelog to beta.5
```
```
fix(release): need to depend on latest rxjs and zone.js

The version in our package.json gets copied to the one we publish, and users need the latest of these.
```

[github]: https://github.com/ksprashu/gemini-cli-mcp-servers
[dev-doc]: https://github.com/ksprashu/gemini-cli-mcp-servers/blob/main/docs/DEVELOPER.md
