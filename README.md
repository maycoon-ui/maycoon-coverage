# Coverage Report for Maycoon

![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmaycoon-ui%2Fmaycoon-coverage%2Frefs%2Fheads%2Fmaster%2Fcoverage-percentage.json&query=coverage&suffix=%25&label=coverage&color=beige)

This repository is used to generate coverage reports for the Maycoon project.
It is updated automatically via GitHub Actions every day and generates coverage reports on pushes.

It uses the [tarpaulin](https://github.com/xd009642/tarpaulin) tool to generate coverage reports
and runs a python script in order to convert the coverage report into a "clean" integer rounded coverage output.

The output can then be used as a badge with [shields.io](https://shields.io).

If you want to create a similar setup for any of your projects,
you are free to clone this repo and adapt the workflow!
