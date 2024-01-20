# Contributing

Contributions are welcome, and greatly appreciated! Every little bit helps, and credit will always be given.

Read on if you want to learn about how our team contributes to our package's development (Internal Contributions) and how you can get involved (External Contributions).

## Internal Contributions

Our team follows the [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow). This includes creating new branches to work on changes. When the changes are ready a Pull Request (PR) is made, accompanied by linked issues to facilitate discussion and review. After approval, the changes are merged to incorporate the new feature or fix to our package. The branch is then deleted to maintain a tidy repository.

## External Contributions

Here are the different types of contributions you can make!

### Report Bugs

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any part of the documentation, such as the official docs, docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope narrow, so its easier to implement.
* Remember that this is a volunteer-driven project, and that contributions  are welcome :)

### Get Started!

Here's how to set up `eda_mds` for local development.

1. Download a copy of `eda_mds` locally.
2. Create/activate new `conda` environment and install poetry

    ```console
    $ conda create -n eda_mds_dev python=3.9 poetry
    ```

    ```console
    $ conda activate eda_mds_dev 
    ```

3. Install `eda_mds` using `poetry`:

    ```console
    $ poetry install
    ```

4. Use `git` (or similar) to create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

5. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

6. Commit your changes and open a pull request.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the `eda_mds` project is released with a [Code of Conduct](https://github.com/UBC-MDS/eda_mds/blob/main/CONDUCT.md). By contributing to the development of this package you agree to abide by its terms.
